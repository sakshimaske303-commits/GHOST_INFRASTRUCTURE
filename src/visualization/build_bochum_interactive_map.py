"""build_bochum_interactive_map.py — folium rebuild of the Bochum overlay map, replacing the old QGIS2Web export. Matches the Essen map's style (dark tiles, orange/lightblue markers, low-access heatmap)."""
import geopandas as gpd
import folium
from folium.plugins import HeatMap

OUT = "outputs/maps/bochum_interactive_map.html"

TILE_URL = "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
TILE_ATTR = (
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors '
    '&copy; <a href="https://carto.com/attributions">CARTO</a>'
)
BOUNDARY_STYLE = {"color": "#7FB8BE", "fillColor": "#F5EFD8", "fillOpacity": 0.06, "weight": 2}


def load_layers():
    boundary = gpd.read_file("data/boundaries/gadm41_DEU.gpkg", layer="ADM_ADM_4")
    boundary = boundary[boundary["NAME_4"] == "Bochum"][["NAME_4", "geometry"]]

    acc = gpd.read_file("data/accessibility/bochum_accessibility_with_distance.gpkg").to_crs(4326)
    low_access = acc[acc["within_15min"] == False]

    mines = gpd.read_file("data/historical_georeferenced/bochum_coal_mines.gpkg").to_crs(4326)
    colonies = gpd.read_file("data/historical_georeferenced/bochum_zechensiedlungen.gpkg").to_crs(4326)

    return boundary, low_access, mines, colonies


def build():
    boundary, low_access, mines, colonies = load_layers()

    center = boundary.geometry.iloc[0].centroid
    m = folium.Map(location=[center.y, center.x], zoom_start=12, tiles=None)
    folium.TileLayer(TILE_URL, attr=TILE_ATTR, min_zoom=0, max_zoom=20, max_native_zoom=20).add_to(m)

    folium.GeoJson(
        boundary.__geo_interface__,
        name="Bochum City Boundary",
        style_function=lambda f: BOUNDARY_STYLE,
    ).add_to(m)

    heat_data = [[pt.y, pt.x] for pt in low_access.geometry]
    HeatMap(heat_data, name=f"Low 15-Min Accessibility (heatmap, n={len(heat_data):,})").add_to(m)

    mine_years = f"{int(mines['opening_year'].min())}-{int(mines['closing_year'].max())}"
    mines_group = folium.FeatureGroup(name=f"Coal Mines ({mine_years})")
    for _, row in mines.iterrows():
        popup_html = (
            f"<b>{row['mine_name']}</b><br>"
            f"District: {row['district']}<br>"
            f"Active: {int(row['opening_year'])}–{int(row['closing_year'])}"
        )
        folium.Marker(
            [row.geometry.y, row.geometry.x],
            tooltip=row["mine_name"],
            popup=folium.Popup(popup_html, max_width=280),
            icon=folium.Icon(color="orange", icon="industry", prefix="fa"),
        ).add_to(mines_group)
    mines_group.add_to(m)

    col_years = f"{int(colonies['construction_start'].min())}-{int(colonies['construction_end'].max())}"
    colonies_group = folium.FeatureGroup(name=f"Worker Colonies ({col_years})")
    for _, row in colonies.iterrows():
        popup_html = (
            f"<b>{row['settlement_name']}</b><br>"
            f"Associated Mine: {row['associated_mine']}<br>"
            f"District: {row['district']}<br>"
            f"Built: {int(row['construction_start'])}–{int(row['construction_end'])}"
        )
        folium.Marker(
            [row.geometry.y, row.geometry.x],
            tooltip=row["settlement_name"],
            popup=folium.Popup(popup_html, max_width=280),
            icon=folium.Icon(color="lightblue", icon="home", prefix="fa"),
        ).add_to(colonies_group)
    colonies_group.add_to(m)

    folium.LayerControl(collapsed=False).add_to(m)

    m.save(OUT)
    print("Saved:", OUT)
    print(f"Coal mines: {len(mines)} | Worker colonies: {len(colonies)} | Low-access heatmap points: {len(heat_data):,}")


if __name__ == "__main__":
    build()

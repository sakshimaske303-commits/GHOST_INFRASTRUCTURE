var wms_layers = [];


        var lyr_DarkMatter_0 = new ol.layer.Tile({
            'title': 'Dark Matter',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
            attributions: '<a href="https://cartodb.com/basemaps/">Map tiles by CartoDB, under CC BY 4.0. Data by OpenStreetMap, under ODbL.</a>',
                url: 'https://a.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png'
            })
        });
var format_bochum_city_1 = new ol.format.GeoJSON();
var features_bochum_city_1 = format_bochum_city_1.readFeatures(json_bochum_city_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_bochum_city_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_bochum_city_1.addFeatures(features_bochum_city_1);
var lyr_bochum_city_1 = new ol.layer.Vector({
                declutter: false,
                source:jsonSource_bochum_city_1, 
                style: style_bochum_city_1,
                popuplayertitle: 'bochum_city',
                interactive: false,
                title: '<img src="styles/legend/bochum_city_1.png" /> bochum_city'
            });
var format_bochum_accessibility_with_distance_2 = new ol.format.GeoJSON();
var features_bochum_accessibility_with_distance_2 = format_bochum_accessibility_with_distance_2.readFeatures(json_bochum_accessibility_with_distance_2, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_bochum_accessibility_with_distance_2 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_bochum_accessibility_with_distance_2.addFeatures(features_bochum_accessibility_with_distance_2);
var lyr_bochum_accessibility_with_distance_2 = new ol.layer.Vector({
                declutter: false,
                source:jsonSource_bochum_accessibility_with_distance_2, 
                style: style_bochum_accessibility_with_distance_2,
                popuplayertitle: 'bochum_accessibility_with_distance',
                interactive: false,
    title: 'bochum_accessibility_with_distance<br />\
    <img src="styles/legend/bochum_accessibility_with_distance_2_0.png" /> 0<br />\
    <img src="styles/legend/bochum_accessibility_with_distance_2_1.png" /> 1<br />' });
var format_bochum_coal_mines_3 = new ol.format.GeoJSON();
var features_bochum_coal_mines_3 = format_bochum_coal_mines_3.readFeatures(json_bochum_coal_mines_3, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_bochum_coal_mines_3 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_bochum_coal_mines_3.addFeatures(features_bochum_coal_mines_3);
var lyr_bochum_coal_mines_3 = new ol.layer.Vector({
                declutter: false,
                source:jsonSource_bochum_coal_mines_3, 
                style: style_bochum_coal_mines_3,
                popuplayertitle: 'bochum_coal_mines',
                interactive: false,
                title: '<img src="styles/legend/bochum_coal_mines_3.png" /> bochum_coal_mines'
            });
var format_bochum_zechensiedlungen_4 = new ol.format.GeoJSON();
var features_bochum_zechensiedlungen_4 = format_bochum_zechensiedlungen_4.readFeatures(json_bochum_zechensiedlungen_4, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_bochum_zechensiedlungen_4 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_bochum_zechensiedlungen_4.addFeatures(features_bochum_zechensiedlungen_4);
var lyr_bochum_zechensiedlungen_4 = new ol.layer.Vector({
                declutter: false,
                source:jsonSource_bochum_zechensiedlungen_4, 
                style: style_bochum_zechensiedlungen_4,
                popuplayertitle: 'bochum_zechensiedlungen',
                interactive: false,
                title: '<img src="styles/legend/bochum_zechensiedlungen_4.png" /> bochum_zechensiedlungen'
            });

lyr_DarkMatter_0.setVisible(true);lyr_bochum_city_1.setVisible(true);lyr_bochum_accessibility_with_distance_2.setVisible(true);lyr_bochum_coal_mines_3.setVisible(true);lyr_bochum_zechensiedlungen_4.setVisible(true);
var layersList = [lyr_DarkMatter_0,lyr_bochum_city_1,lyr_bochum_accessibility_with_distance_2,lyr_bochum_coal_mines_3,lyr_bochum_zechensiedlungen_4];
lyr_bochum_city_1.set('fieldAliases', {'fid': 'fid', 'GID_4': 'GID_4', 'GID_0': 'GID_0', 'COUNTRY': 'COUNTRY', 'GID_1': 'GID_1', 'NAME_1': 'NAME_1', 'GID_2': 'GID_2', 'NAME_2': 'NAME_2', 'GID_3': 'GID_3', 'NAME_3': 'NAME_3', 'NAME_4': 'NAME_4', 'VARNAME_4': 'VARNAME_4', 'TYPE_4': 'TYPE_4', 'ENGTYPE_4': 'ENGTYPE_4', 'CC_4': 'CC_4', });
lyr_bochum_accessibility_with_distance_2.set('fieldAliases', {'fid': 'fid', 'osmid': 'osmid', 'y': 'y', 'x': 'x', 'street_count': 'street_count', 'highway': 'highway', 'junction': 'junction', 'railway': 'railway', 'ref': 'ref', 'within_15min': 'within_15min', 'dist_to_historical_m': 'dist_to_historical_m', 'within_15_num': 'within_15_num', });
lyr_bochum_coal_mines_3.set('fieldAliases', {'fid': 'fid', 'mine_name': 'mine_name', 'district': 'district', 'latitude': 'latitude', 'longitude': 'longitude', 'opening_year': 'opening_year', 'closing_year': 'closing_year', });
lyr_bochum_zechensiedlungen_4.set('fieldAliases', {'fid': 'fid', 'settlement_name': 'settlement_name', 'associated_mine': 'associated_mine', 'district': 'district', 'latitude': 'latitude', 'longitude': 'longitude', 'construction_start': 'construction_start', 'construction_end': 'construction_end', });
lyr_bochum_city_1.set('fieldImages', {'fid': 'TextEdit', 'GID_4': 'TextEdit', 'GID_0': 'TextEdit', 'COUNTRY': 'TextEdit', 'GID_1': 'TextEdit', 'NAME_1': 'TextEdit', 'GID_2': 'TextEdit', 'NAME_2': 'TextEdit', 'GID_3': 'TextEdit', 'NAME_3': 'TextEdit', 'NAME_4': 'TextEdit', 'VARNAME_4': 'TextEdit', 'TYPE_4': 'TextEdit', 'ENGTYPE_4': 'TextEdit', 'CC_4': 'TextEdit', });
lyr_bochum_accessibility_with_distance_2.set('fieldImages', {'fid': 'TextEdit', 'osmid': 'TextEdit', 'y': 'TextEdit', 'x': 'TextEdit', 'street_count': 'TextEdit', 'highway': 'TextEdit', 'junction': 'TextEdit', 'railway': 'TextEdit', 'ref': 'TextEdit', 'within_15min': 'CheckBox', 'dist_to_historical_m': 'TextEdit', 'within_15_num': 'Range', });
lyr_bochum_coal_mines_3.set('fieldImages', {'fid': 'TextEdit', 'mine_name': 'TextEdit', 'district': 'TextEdit', 'latitude': 'TextEdit', 'longitude': 'TextEdit', 'opening_year': 'TextEdit', 'closing_year': 'TextEdit', });
lyr_bochum_zechensiedlungen_4.set('fieldImages', {'fid': 'TextEdit', 'settlement_name': 'TextEdit', 'associated_mine': 'TextEdit', 'district': 'TextEdit', 'latitude': 'TextEdit', 'longitude': 'TextEdit', 'construction_start': 'TextEdit', 'construction_end': 'TextEdit', });
lyr_bochum_city_1.set('fieldLabels', {'fid': 'no label', 'GID_4': 'no label', 'GID_0': 'no label', 'COUNTRY': 'no label', 'GID_1': 'no label', 'NAME_1': 'no label', 'GID_2': 'no label', 'NAME_2': 'no label', 'GID_3': 'no label', 'NAME_3': 'no label', 'NAME_4': 'no label', 'VARNAME_4': 'no label', 'TYPE_4': 'no label', 'ENGTYPE_4': 'no label', 'CC_4': 'no label', });
lyr_bochum_accessibility_with_distance_2.set('fieldLabels', {'fid': 'no label', 'osmid': 'no label', 'y': 'no label', 'x': 'no label', 'street_count': 'no label', 'highway': 'no label', 'junction': 'no label', 'railway': 'no label', 'ref': 'no label', 'within_15min': 'no label', 'dist_to_historical_m': 'no label', 'within_15_num': 'no label', });
lyr_bochum_coal_mines_3.set('fieldLabels', {'fid': 'no label', 'mine_name': 'no label', 'district': 'no label', 'latitude': 'no label', 'longitude': 'no label', 'opening_year': 'no label', 'closing_year': 'no label', });
lyr_bochum_zechensiedlungen_4.set('fieldLabels', {'fid': 'no label', 'settlement_name': 'no label', 'associated_mine': 'no label', 'district': 'no label', 'latitude': 'no label', 'longitude': 'no label', 'construction_start': 'no label', 'construction_end': 'no label', });
lyr_bochum_zechensiedlungen_4.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});
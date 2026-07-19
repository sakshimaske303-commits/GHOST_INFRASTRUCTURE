from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat, dlon = radians(lat2-lat1), radians(lon2-lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(dlon/2)**2
    return R * 2 * atan2(sqrt(a), sqrt(1-a))

d1 = haversine(51.47467, 7.29851, 51.49036, 7.29750)
print(f"Mansfeld-Heinrich Gustav distance: {d1:.2f} km")

d2 = haversine(51.5033, 7.1611, 51.5042, 7.1656)
print(f"Kolonie Hannover-Am Ruebenkamp distance: {d2:.2f} km")
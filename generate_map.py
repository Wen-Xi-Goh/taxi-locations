import json
import folium
from folium.plugins import LocateControl

# Load the taxi-data.json
with open("taxi-data.json", "r") as f:
    responsedict = json.load(f)

# Center the map on Singapore
singapore_center = [1.3521, 103.8198]
map_sg = folium.Map(location=singapore_center, zoom_start=12)

# Add user location button
LocateControl(auto_start=False).add_to(map_sg)

# Plot taxi locations
for taxi in responsedict['value']:
    folium.CircleMarker(
        location=[taxi['Latitude'], taxi['Longitude']],
        radius=3,
        color='blue',
        fill=True,
        fill_opacity=0.7
    ).add_to(map_sg)

# Save the map to HTML
map_sg.save("singapore_taxi_map.html")
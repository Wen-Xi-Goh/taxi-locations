import json
import folium
from folium.plugins import LocateControl

# Load taxi data JSON file
with open("taxi-data.json", "r") as f:
    responsedict = json.load(f)

# Singapore center coordinates
singapore_center = [1.3521, 103.8198]

# Create folium map centered on Singapore
map_sg = folium.Map(location=singapore_center, zoom_start=12)

# Add a location button (shows user's location on click)
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

# Add meta refresh tag to reload page every 60 seconds
refresh_meta = '<meta http-equiv="refresh" content="60">'
map_sg.get_root().header.add_child(folium.Element(refresh_meta))

# Save the generated map as index.html
map_sg.save("index.html")

print("index.html generated successfully")

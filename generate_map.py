import json
import folium
from folium.plugins import LocateControl

# Load the taxi data
with open("taxi-data.json", "r") as f:
    responsedict = json.load(f)

# Create the map centered on Singapore
singapore_center = [1.3521, 103.8198]
map_sg = folium.Map(location=singapore_center, zoom_start=12)

# Add the locate control button
LocateControl(auto_start=False).add_to(map_sg)

# Add taxi locations
for taxi in responsedict['value']:
    folium.CircleMarker(
        location=[taxi['Latitude'], taxi['Longitude']],
        radius=3,
        color='blue',
        fill=True,
        fill_opacity=0.7
    ).add_to(map_sg)

# Add meta refresh tag by injecting into the HTML <head>
refresh_html = """
<meta http-equiv="refresh" content="60">
"""

# Another way: Add JavaScript reload script
# refresh_script = """
# <script>
#   setTimeout(() => { window.location.reload(); }, 60000);
# </script>
# """

# Inject meta tag into map HTML
map_sg.get_root().header.add_child(folium.Element(refresh_html))

# Save the map as index.html
map_sg.save("index.html")

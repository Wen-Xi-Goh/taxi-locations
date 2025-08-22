import json
import folium
from folium.plugins import LocateControl
from datetime import datetime

# Load taxi data JSON file
with open("taxi-data.json", "r") as f:
    responsedict = json.load(f)

# Singapore center coordinates
singapore_center = [1.3521, 103.8198]

# Create folium map centered on Singapore
map_sg = folium.Map(location=singapore_center, zoom_start=12)

# Add a location button (shows user's location on click)
LocateControl(auto_start=False).add_to(map_sg)

# Plot initial taxi locations
marker_layer = folium.FeatureGroup(name="Taxis", show=True)
for taxi in responsedict['value']:
    folium.CircleMarker(
        location=[taxi['Latitude'], taxi['Longitude']],
        radius=3,
        color='blue',
        fill=True,
        fill_opacity=0.7
    ).add_to(marker_layer)
marker_layer.add_to(map_sg)

# Add a timestamp footer
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
footer_html = f"""
<div id="timestamp" style="position: fixed; bottom: 10px; left: 10px; z-index:9999;
            background-color: white; padding: 5px; font-size: 12px;
            border: 1px solid #ccc;">
    Last updated: {timestamp}
</div>
"""
map_sg.get_root().html.add_child(folium.Element(footer_html))

# Add JavaScript for auto-refreshing only the markers
refresh_script = """
<script>
  const taxiLayer = L.layerGroup().addTo(window.map);

  async function refreshTaxiMarkers() {
    try {
      const res = await fetch('taxi-data.json');
      const data = await res.json();
      taxiLayer.clearLayers();

      for (const taxi of data.value) {
        L.circleMarker([taxi.Latitude, taxi.Longitude], {
          radius: 3,
          color: 'blue',
          fillOpacity: 0.7
        }).addTo(taxiLayer);
      }

      const timestamp = new Date().toLocaleString();
      document.getElementById('timestamp').innerText = 'Last updated: ' + timestamp;
    } catch (err) {
      console.error("Taxi data refresh failed:", err);
    }
  }

  // Refresh every 60 seconds
  setInterval(refreshTaxiMarkers, 60000);
</script>
"""
map_sg.get_root().html.add_child(folium.Element(refresh_script))

# Save the generated map as index.html
map_sg.save("index.html")

print("index.html generated successfully")

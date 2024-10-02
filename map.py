

import folium

# Define map center coordinates
map_center = [-1.2869, 36.8181]

# Create the map object
mymap = folium.Map(location=map_center, zoom_start=16)

# Add a marker to the map
folium.Marker(
    [-1.2869, 36.8181],
    popup="Nyayo Hse, Nairobi",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mymap)

# Save the map as an HTML file
mymap.save("my_map.html")
print("Map has been saved as 'my_map.html'.")

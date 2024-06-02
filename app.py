import folium
from folium import plugins

def main():
    # Get the dimensions of the viewport (assuming full screen)
    viewport_width = 1920  # Width of the viewport in pixels (example)
    viewport_height = 1080  # Height of the viewport in pixels (example)

    # Create a map centered at a specific location with width and height matching the viewport
    my_map = folium.Map(location=[0, 0], zoom_start=2, control_scale=True, attr=None, width=viewport_width, height=viewport_height, no_wrap=True)

    # Calculate the maximum zoom level to fit the entire screen
    max_zoom = calculate_max_zoom(viewport_width, viewport_height)

    # Set the maximum zoom level
    my_map.options['maxZoom'] = max_zoom

    # Add a custom pane for the search icon
    search_icon_pane = folium.map.CustomPane('search-icon-pane', z_index=200)
    my_map.add_child(search_icon_pane)

    # Add a search icon
    search_icon_html = '<i class="fas fa-search" style="font-size: 24px; color: blue;"></i>'
    search_icon = plugins.FloatImage(search_icon_html, bottom=80, left=40)
    search_icon.add_to(search_icon_pane)

    # Save the map to an HTML file
    my_map.save("my_map.html")

    # Open the map in the default web browser
    import webbrowser
    webbrowser.open("my_map.html")

def calculate_max_zoom(viewport_width, viewport_height):
    # Calculate the maximum zoom level to fit the entire screen
    max_zoom_width = calculate_zoom_level(viewport_width)
    max_zoom_height = calculate_zoom_level(viewport_height)
    max_zoom = min(max_zoom_width, max_zoom_height)

    return max_zoom

def calculate_zoom_level(viewport_dimension):
    # Calculate the zoom level required to fit the entire map within the viewport
    map_size_at_zoom_0 = 256  # Size of the map at zoom level 0
    zoom_level = 0
    while map_size_at_zoom_0 < viewport_dimension:
        zoom_level += 1
        map_size_at_zoom_0 *= 2

    return zoom_level

if __name__ == "__main__":
    main()

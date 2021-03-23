import folium
import json
from shapely.geometry import shape, Point
from bs4 import BeautifulSoup
from folium.plugins import LocateControl, MarkerCluster
import base64
from dictionary import sales

# Create the map
MyMap = folium.Map(location=[43.61092, 3.87723], tiles='OpenStreetMap', zoom_start=2, max_zoom=19, control_scale=True)
folium.TileLayer('cartodbpositron').add_to(MyMap)

for person, details in sales.items():
    # Define marker variables
    name = person
    coordinates = (details['lat'], details['lon'])
    title = details['title']
    skills = details['skills']
    phone = details['phone']
    email = details['email']
    picture = details['picture']

    # Picture try again
    apic = base64.b64encode(open(picture, 'rb').read()).decode()
    
    # Define icons
    redicon = folium.Icon(icon="user", prefix="glyphicon", color='red')
    
    all_html = f'''
        <div class="content">
            <img border="0" align="Left" style="padding-right: 15px" src="data:image/jpg;base64,{apic}">
            <div class="text">
                <p>
                    <b><span style="font-family: Arial; font-size: 17px;">{name}</span></b><br>
                    <span style="font-family: Arial; font-size: 14px;">{title}</span><br><br>
                    <span style="font-family: Arial; font-size: 12px;">{skills}</span><br><br>
                    <span style="font-family: Arial; font-size: 12px;">{phone}</span><br>
                    <a href={email}><span style="font-family: Arial; font-size: 12px;">{email}</span></a>
                </p>
            </div>
        </div>'''
 
    # Create a marker
    iframe = folium.IFrame(all_html, width = 320, height = 170)
    popup = folium.Popup(iframe, max_width=1000)

    custom_marker = folium.Marker(location=coordinates, popup=popup, tooltip=name, icon=redicon)

    # Add marker to map
    custom_marker.add_to(MyMap)

# Save the map
MyMap.save('MyMap.html')

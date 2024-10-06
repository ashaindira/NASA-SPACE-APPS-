from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Sentinel Hub credentials (replace with your credentials)
SENTINEL_HUB_INSTANCE_ID = "ee0cb4f8-8cf6-4a98-9c1e-8549146b51a2"  # Replace with your Sentinel Hub instance ID
SENTINEL_HUB_WMS_URL = f"https://services.sentinel-hub.com/configuration/v1/wms/instances/ee0cb4f8-8cf6-4a98-9c1e-8549146b51a2"
@app.route('/', methods=['GET', 'POST'])
def index():
    print("Accessed the index page")
    satellite_image_url = None

    if request.method == 'POST':
        print("Form submitted")
        # Get the user inputs from the form
        lat = request.form['lat']
        lon = request.form['lon']
        date = request.form['date']
        layer = request.form['layer']
        platform = request.form['platform']

        # Define WMS parameters for the request
        params = {
            'SERVICE': 'WMS',
            'REQUEST': 'GetMap',
            'LAYERS': layer,  # Sentinel layer for NDVI
            'FORMAT': 'image/png',
            'BBOX': f'{float(lat)-0.1},{float(lon)-0.1},{float(lat)+0.1},{float(lon)+0.1}',
            'CRS': 'EPSG:4326',
            'WIDTH': 512,
            'HEIGHT': 512,
            'TIME': date,
            'MAXCC': '20'  # Maximum cloud coverage
        }

        # Make the request to Sentinel Hub
        response = requests.get(SENTINEL_HUB_WMS_URL, params=params)
        print(f"Response Status Code: {response.status_code}")

        if response.status_code == 200:
             print(f"Response Content: {response.content}")
             satellite_image_url = response.url

    return render_template('index.html', satellite_image_url=satellite_image_url)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
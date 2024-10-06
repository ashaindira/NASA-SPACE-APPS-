Crop Health Monitoring

This is a Flask-based web application that allows users to monitor crop health using satellite data. The application fetches NDVI (Normalized Difference Vegetation Index), EVI (Enhanced Vegetation Index), or True Color imagery for a specific location and date using Sentinel Hub.

## Features
- Input geographical coordinates (latitude, longitude) and date to fetch satellite imagery.
- Select different layers such as NDVI, True Color, or EVI.
- Fetch satellite imagery data from Sentinel Hub.

## Requirements

- Python 3.x
- Flask
- Flask-Cors
- Requests
- Sentinel Hub instance with WMS capabilities

## Installation

1. Clone this repository:

    bash
    git clone git@github.com:ashaindira/NASA-SPACE-APPS-.git
    cd crop-health-monitoring
    

2. Create a virtual environment 
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3.3. Install the required packages:

    bash
    pip install -r requirements.txt
    

4. Replace the SENTINEL_HUB_INSTANCE_ID in the app.py with your actual Sentinel Hub instance ID:

    python
    SENTINEL_HUB_INSTANCE_ID = "your_instance_id"
    

5. Run the application:

    bash
    python app.py
    

6. Open your browser and go to http://127.0.0.1:5001 to use the application.

The application depends on the following Python libraries, listed in the requirements.txt:

Flask==2.2.2
Flask-Cors==3.0.10
numpy==1.23.3
pandas==1.5.0
rasterio==1.3.5
requests==2.28.1

install them using pip install -r requirements.txt

## Usage

1. Enter the latitude and longitude of the area of interest.
2. Select the date in the format YYYY-MM-DD.
3. Choose the desired satellite layer (NDVI, True Color, or EVI).
4. Click on "Fetch Crop Health Data" to view the satellite image.






   


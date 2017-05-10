import arcgis_license_processor
from flask import Flask, jsonify
from config import settings

# Flask Details
app = Flask(__name__)

@app.route('/')
def return_json():

    # Read in licenses
    license_status = arcgis_license_processor.process_licenses(settings=settings)

    # Return JSON to Browser
    return jsonify(license_status)






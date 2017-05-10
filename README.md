# arcgis_license_processor
A Python module that returns a dictionary object from your ArcGIS License Manager output.

# Overview
This code will give you a python dictionary that can be used for various purposes.  I am providing two examples (command line and Flask) that reads the logfile output and outputs to their respective environment. 

I currently have an internal Flask app that I populate with the license data for reference.

<div style="width: 100%; text-align: center"><a href="extras/example.png" target="_new"><img src="extras/example.png" width="640"></a></div>

# Windows Server Installation
1. Setup a scheduled task to run the following command to export your license manager.  Make sure to update the target path with a proper path on your server. 

    `"C:\Program Files (x86)\ArcGIS\License10.5\bin\lmutil.exe" lmstat -a -c "C:\Program Files (x86)\ArcGIS\License10.5\bin\service.txt" > C:\export\path\CheckLicenses.log`

     _*This example is using ArcGIS 10.5's license manager. If you want the scheduled task to export at an interval less than 1 minute, you will need multiple scheduled tasks that start at different times (e.g. offset by 15 seconds) that overwrite the same file.*_

2. Update config.py with the appropriate paths, licenses and counts.  Search for `{server}` in case the line #'s change for paths to update.
3. From a command line... `python Python\PrettyPrint_Dict.py` to view a pretty-printed output from the dictionary object.

## Flask Example
1. Create a virtual environment and install Flask with the provided requirements.txt.
2. Activate the virtual environment and then run 'Run_Flask.bat'
3. Open in your browser (http://127.0.0.1:5000)

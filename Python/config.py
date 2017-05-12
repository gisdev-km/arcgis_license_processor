"""
    MAKE SURE TO UPDATE LINES 8, 35 AND 36 WITH THE CORRECT SERVER PATH
"""

settings = {
    # License Server Related
    "licenseServer": "license_server/27000", # License Server & Port
    "input": r".\..\extras\CheckLicenses.log",
    "licenses": {
        # ArcGIS Desktop
        "Viewer": {"name": "ArcGIS Desktop Basic", "count": 10, "display": True,  "order": 1 },
        "Editor": { "name": "ArcGIS Desktop Standard", "count": 10, "display": True,  "order": 2 },
        "ARC/INFO": { "name": "ArcGIS Desktop Advanced", "count": 10, "display": True,  "order": 3 },
        # ArcGIS Pro
        "desktopBasicP": { "name": "ArcGIS Pro Basic", "count": 10, "display": False, "order": 4 },
        "desktopStdP": { "name": "ArcGIS Pro Standard", "count": 10, "display": False,  "order": 5 },
        "desktopAdvP": { "name": "ArcGIS Pro Advanced", "count": 10, "display": False,  "order": 6 },
        # City Engine
        "CityEngAdv": { "name": "CityEngine Advanced", "count": 10, "display": True,  "order": 7 },
		# Extensions - ArcGIS Desktop
        "TIN": { "name": "3D Analyst", "count": 10, "display": True, "order": 5 },
        "Grid": { "name": "Spatial Analyst", "count": 10, "display": True, "order": 6 },
        "Network": { "name": "Network Analyst", "count": 10, "display": True, "order": 7 },
        "MrSID": { "name": "Mr SID", "count": 10, "display": True, "order": 8 },
        "Plotting": { "name": "Plotting", "count": 10, "display": True, "order": 9 },
        "TIFFLZW": { "name": "TIFFLZW","count": 10, "display": True, "order": 10 },
        "Video": { "name": "Full Motion Video", "count": 10, "display": True, "order": 11 },
        "Video": { "name": "Full Motion Video", "count": 10, "display": True, "order": 11 },
        # Extensions - ArcGIS Pro
        "networkAnalystP": { "name": "Network Analyst (Pro)", "count": 10, "display": False,  "order": 12 },
        "spatialAnalystP": { "name": "Spatial Analyst (Pro)", "count": 10, "display": False,  "order": 13 },
        "3DAnalystP": { "name": "3D Analyst (Pro)", "count": 10, "display": False, "order": 14 }
    },
    "extensions": ["Grid", "MrSID", "Network", "Plotting", "TIFFLZW", "TIN", "Video", "networkAnalystP", "spatialAnalystP",  "3DAnalystP"],
    "lmutilPath": r"\\{server}\c$\Program Files (x86)\ArcGIS\License10.5\bin\lmutil.exe",
    "licenseFile": r"\\{server}\c$\Program Files (x86)\ArcGIS\License10.5\bin\service.txt"
}

import codecs
from datetime import datetime
from config import settings
from classes import License

def process_licenses(settings=None):
    """ Read and report license information from raw license file """
    licenseServer = settings["licenseServer"]
    
    with codecs.open(settings["input"],"r", "utf-8") as f: # have experienced weird uf-8 characters in text file
        licenseRaw = f.readlines()

    status = {
        "timestamp": None,
        "serverStatus": "DOWN",
        "licenses": {},
        "extensions": {}
    }

    licenseType = None
    license = None

    for i, line in enumerate(licenseRaw):
        line = line.replace("\n","").replace("\r","")
        line = line.encode("ascii", "ignore")

        if i == 1:
            # Get timestamp of export
            strTimestamp = line.split(" status on ")[1]
            timestamp = datetime.strptime(strTimestamp, "%a %m/%d/%Y %H:%M")
            status["timestamp"] = timestamp.strftime("%m/%d/%Y %I:%M %p")
            
            del strTimestamp
            del timestamp

        if "license server " in line and "UP" in line:
            # Check if server is up or down
            status["serverStatus"] = "UP"

        if "Users of " in line or (i+1 == len(licenseRaw)):
            # Build license object
            if not licenseType == None and not license == None:

                dictTarget = "licenses"

                if licenseType in settings["extensions"]:
                    dictTarget = "extensions"

                license.calcValues()

                status[dictTarget][licenseType] = license.__dict__
                license = None

            parensStart = line.find("(")
            licenseType = line[9:parensStart-3]

            if licenseType in settings["licenses"]:

                license = License(name=settings["licenses"][licenseType]["name"], 
                                  total=settings["licenses"][licenseType]["count"], 
                                  id=licenseType,
                                  display=settings["licenses"][licenseType]["display"],
                                  order=settings["licenses"][licenseType]["order"])

        if licenseServer in line:
            line = line.strip().split(" ")
            license.addUser(hash=line[2], user=line[0], machine=line[1])

    for type in ["licenses", "extensions"]:
        # Exclude any licenses from being reported
        licenseRemove = []
        for key in status[type]:
            license = status[type][key]
            if license["display"] == False:
                licenseRemove.append(key)

        for license in licenseRemove:
            del status[type][license]

    return status

    
if __name__ == "__main__":
    status = process_licenses(settings=settings)
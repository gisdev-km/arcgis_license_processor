from config import settings
import arcgis_license_processor
import pprint

if __name__ == "__main__":
    """
        Example script to read in licenses

        MAKE SURE TO UPDATE THE CONFIG SERVER PATH!
    """
    # Read in licenses
    license_status = arcgis_license_processor.process_licenses(settings=settings)
    
    # Display Output
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(license_status)
def run(apiurl, apikey, currentlat, currentlong, currentalt):
    import requests
    import json
    newapi = apiurl + "visualpasses/"
    newkey = "&apiKey=" + apikey
    lat = currentlat + "/"
    lon = currentlong + "/"
    alt = currentalt + "/"
    print("Enter NORAD ID of Sat.".center(45, " "))
    noradid = input("> ")
    print("Enter Number Of Days Of Prediction (Max. 10)".center(45, " "))
    days = input("> ")
    print("Enter Min. # of Sec. for Visibility".center(45, " "))
    minvis = input("> ")
    query = newapi+noradid+"/"+lat+lon+alt+days+"/"+minvis+"/"+newkey
    r = requests.get(query).text
    resp = json.loads(r)
    try:
        passescount = resp['info']['passescount']
        if passescount == 0:
            print("No Results Found".center(45, " "))
        else:
            for x in resp['passes']:
                print("")
                print("=== Start ===".center(45, " "))
                print("Starting Azimuth: %g".center(45, " ") % x['startAz'])
                print("Starting Compass Direction: %s".center(45, " ") % x['startAzCompass'])
                print("Starting Elevation: %g".center(45, " ") % x['startEl'])
                print("Starting Time (UTC): %d".center(45, " ") % x['startUTC'])
                print("=== End ===".center(45, " "))
                print("Ending Azimuth: %g".center(45, " ") % x['endAz'])
                print("Ending Compass Direction: %s".center(45, " ") % x['endAzCompass'])
                print("Ending Elevation: %g".center(45, " ") % x['endEl'])
                print("Ending Time (UTC): %d".center(45, " ") % x['endUTC'])
                print("=== Maximum ===".center(45, " "))
                print("Maximum Azimuth: %g".center(45, " ") % x['maxAz'])
                print("Maximum Compass Direction: %s".center(45, " ") % x['maxAzCompass'])
                print("Maximum Elevation: %g".center(45, " ") % x['maxEl'])
                print("Maximum Time (UTC): %d".center(45, " ") % x['maxUTC'])
                print("Magnitude of Pass: %g".center(45, " ") % x['mag'])
                print("Duration of Pass: %g".center(45, " ") % x['duration'])
            print("")
    except KeyError:
        print("No Results Found".center(45, " "))

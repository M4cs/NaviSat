def run(apiurl, apikey, currentlat, currentlong, currentalt):
    import requests
    import json
    newapi = apiurl + "radiopasses/"
    newkey = "&apiKey=" + apikey
    lat = currentlat + "/"
    lon = currentlong + "/"
    alt = currentalt + "/"
    print("Enter NORAD ID of Sat.".center(45, " "))
    noradid = input("> ")
    print("Enter Number Of Days Of Prediction (Max. 10)".center(45, " "))
    days = input("> ")
    print("Enter Min. Elevation (Degrees)".center(45, " "))
    minvis = input("> ")
    query = newapi+noradid+"/"+lat+lon+alt+days+"/"+minvis+"/"+newkey
    r = requests.get(query).text
    resp = json.loads(r)
    try:
        passescount = resp['info']['passescount']
        if passescount == 0:
            print("No Results Found".center(45, " "))
        else:
            satname = resp['info']['satname']
            print("Sat. Name: %s".center(40, " ") % satname)
            print("Number of Results: %d".center(45, " ") % passescount)
            print("")
            for x in resp['passes']:
                print("")
                print("=== Start ===".center(45, " "))
                print("Starting Azimuth: %g".center(40, " ") % x['startAz'])
                print("Starting Compass Direction: %s".center(40, " ") % x['startAzCompass'])
                print("Starting Time (UTC): %d".center(40, " ") % x['startUTC'])
                print("=== End ===".center(45, " "))
                print("Ending Azimuth: %g".center(40, " ") % x['endAz'])
                print("Ending Compass Direction: %s".center(40, " ") % x['endAzCompass'])
                print("Ending Time (UTC): %d".center(40, " ") % x['endUTC'])
                print("=== Maximum ===".center(45, " "))
                print("Maximum Azimuth: %g".center(40, " ") % x['maxAz'])
                print("Maximum Compass Direction: %s".center(40, " ") % x['maxAzCompass'])
                print("Maximum Time (UTC): %d".center(40, " ") % x['maxUTC'])
            print("")
    except KeyError:
        print("No Results Found".center(45, " "))

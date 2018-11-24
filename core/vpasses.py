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
    passescount = resp['info']['passescount']
    if passescount == 0:
        print("No Results Found".center(45, " "))
    else:
        startAz = resp['passes'][0]['startAz']
        startAzDir = resp['passes'][0]['startAzCompass']
        startEl = resp['passes'][0]['startEl']
        startUTC = resp['passes'][0]['startUTC']
        maxAz = resp['passes'][0]['maxAz']
        maxAzDir = resp['passes'][0]['maxAzCompass']
        maxEl = resp['passes'][0]['maxEl']
        maxUTC = resp['passes'][0]['maxUTC']
        endAz = resp['passes'][0]['endAz']
        endAzDir = resp['passes'][0]['endAzCompass']
        endEl = resp['passes'][0]['endEl']
        endUTC = resp['passes'][0]['endUTC']
        mag = resp['passes'][0]['mag']
        duration = resp['passes'][0]['duration']
        satname = resp['info']['satname']
        print("Sat. Name: %s".center(45, " ") % satname)
        print("Number of Results: %d".center(45, " ") % passescount)
        for i in range(passescount):
            print("")
            print("Pass #%d".center(45, " ") % int(int(i)+1))
            print("=== Start ===".center(45, " "))
            print("Starting Azimuth: %g".center(45, " ") % startAz)
            print("Starting Compass Direction: %s".center(45, " ") % startAzDir)
            print("Starting Elevation: %g".center(45, " ") % startEl)
            print("Starting Time (UTC): %d".center(45, " ") % startUTC)
            print("=== End ===".center(45, " "))
            print("Ending Azimuth: %g".center(45, " ") % endAz)
            print("Ending Compass Direction: %s".center(45, " ") % endAzDir)
            print("Ending Elevation: %g".center(45, " ") % endEl)
            print("Ending Time (UTC): %d".center(45, " ") % endUTC)
            print("=== Maximum ===".center(45, " "))
            print("Maximum Azimuth: %g".center(45, " ") % maxAz)
            print("Maximum Compass Direction: %s".center(45, " ") % maxAzDir)
            print("Maximum Elevation: %g".center(45, " ") % maxEl)
            print("Maximum Time (UTC): %d".center(45, " ") % maxUTC)
            print("Magnitude of Pass: %g".center(45, " ") % mag)
            print("Duration of Pass: %g".center(45, " ") % duration)
        print("")

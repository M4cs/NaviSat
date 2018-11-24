def run(apiurl, apikey, currentlat, currentlong, currentalt, sradius, catid):
    import requests, json
    newapi = apiurl + "above/"
    newkey = "&apiKey=" + apikey
    lat = currentlat + "/"
    lon = currentlong + "/"
    alt = currentalt + "/"
    sr = sradius + "/"
    cat = catid + "/"
    query = newapi+lat+lon+alt+sr+cat+newkey
    print("Grabbing Results")
    r = requests.get(query).text
    resp = json.loads(r)
    satcount = resp['info']['satcount']
    if satcount == 0:
        print("No Results Found".center(45, " "))
        exit()
    else:
        print("Number of Results: %d".center(45, " ") % satcount)
        print("Would You Like To Display Results?".center(45, " "))
        ans = str(input("[y\\n] "))
        if ans == "y":
            for i in range(satcount):
                print("=" * 35)
                print("Sat. Name:   %s" % resp['above'][0]['satname'])
                print("Sat. ID:     %s" % resp['above'][0]['satid'])
                print("Launch Date: %s" % resp['above'][0]['launchDate'])
            print("=" * 35)
        else:
            pass
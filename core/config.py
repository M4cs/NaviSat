from configparser import ConfigParser

def createuser():
    config = ConfigParser()
    config['DEFAULT'] = {
        'apikey': '',
        'currentlong': '',
        'currentlat': '',
        'currentalt': ''
    }
    print("Enter n2yo.com API Key".center(45, " "))
    print("Sign up at n2yo.com and Sign in to obtain API Key".center(39, " "))
    print("[!] API Key Format: XXXXXX-XXXXXX-XXXXXX-XXXX [!]".center(39, " "))
    apikey = str(input("> "))
    print("[!] Confirm API Key: %s [!]".center(45, " ") % apikey)
    ans = str(input("[y\\n] ").lower())
    if ans == "y":
        pass
    else:
        createuser()
    loop = True
    while loop:
        print("\nEnter Your Current Longitude".center(45, " "))
        print("[!] This can be obtained on the n2yo.com homepage [!]".center(45, " "))
        longitude = str(input("> "))
        print("\nEnter Your Current Latitude".center(45, " "))
        print("[!] This can be obtained on the n2yo.com homepage [!]".center(45, " "))
        latitude = str(input("> "))
        print("\nEnter Your Current Altitude in Meters".center(45, " "))
        print("[!] This can be obtained many ways. Google it [!]".center(45, " "))
        altitude = str(input("> "))
        print("Confirm Configuration".center(45, " "))
        print("Longitude: %s".center(45, " ") % longitude)
        print("Latitude: %s".center(45, " ") % latitude)
        print("Altitude: %s".center(45, " ") % altitude)
        ans2 = str(input("[y\\n] ").lower())
        if ans2 == "y":
            loop = False
        elif ans2 == "n":
            loop = True
        config['DEFAULT']['apikey'] = apikey
        config['DEFAULT']['currentlong'] = longitude
        config['DEFAULT']['currentlat'] = latitude
        config['DEFAULT']['currentalt'] = altitude
        with open("core/config.ini", "w") as f:
            config.write(f)




def checkuser():
    import os
    if os.path.exists("core/config.ini") == True:
        pass
    else:
        createuser()
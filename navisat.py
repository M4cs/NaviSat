#!/usr/bin/python3
from core import config, above, helpmenu, categories, vpasses, rpasses
import os, pip
import requests, json
from configparser import ConfigParser
os.system("clear")
config.checkuser()
configuration = ConfigParser()
configuration.read("core/config.ini")
print("NaviSat | Satellite Info Tool".center(45, " "))
print("Developed by @maxbridgland".center(45, " "))
print("")
apiurl = "https://www.n2yo.com/rest/v1/satellite/"
apikey = configuration['DEFAULT']['apikey']
currentlat = configuration['DEFAULT']['currentlat']
currentlong = configuration['DEFAULT']['currentlong']
currentalt = configuration['DEFAULT']['currentalt']
pref = "[navisat]: "
helpmenu.displayhelp()
def main():
    inpoot = input(pref)
    if inpoot[0:6] == "search":
        catid = categories.display()
        print("Enter Search Radius (0-90)".center(45, " "))
        sradius = input("> ")
        above.run(apiurl, apikey, currentlat, currentlong, currentalt, sradius, catid)
        main()
    elif inpoot[0:7] == "vpasses":
        vpasses.run(apiurl, apikey, currentlat, currentlong, currentalt)
        main()
    elif inpoot[0:7] == "rpasses":
        rpasses.run(apiurl, apikey, currentlat, currentlong, currentalt)
        main()
    elif inpoot[0:5] == "reset":
        os.system("rm -rf core/config.ini")
        config.checkuser()
        print("Restarting Program...")
        os.system("./navisat.py")
    elif inpoot[0:4] == "exit":
        exit()
    else:
        print("Error Unknown Command...")
        main()
main()
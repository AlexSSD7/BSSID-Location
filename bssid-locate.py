import requests
import sys

args = sys.argv
args.pop(0)

def usage():
    print("Usage:\nbssid-locate.py [MAC ADDRESS/BSSID]")
    exit()

if sys.argv == []:
    usage()

bssid = args[0]
out = requests.get("http://api.mylnikov.org/geolocation/wifi?bssid=" + bssid).json()

if out['result'] == 400:
    print("Wrong BSSID")
    usage()

print("\n")

print("Location Found!\n")
latlon = str(out['data']['lat']) + " " + str(out['data']['lon'])
print("https://www.google.com/maps/search/" + latlon.replace(" ", "%20"))
print("(Lat, Lon)")
print(latlon)

print("\n")
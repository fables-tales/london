import urllib
import pprint
import json
import time
import os

south = 51.416
north = 51.623
west = -0.415
east = 0.179

url1 = "https://api.foursquare.com/v2/venues/explore?"
url2 = "&client_id=0XUU2AT1ZSPMIGEHF23EDFCMQV4VMTFQOABPMCVDUCEPQAYM&client_secret=XY2QFQF0QSNI04DAXMKTQQT3LHPHPFLLOXTRVRZ1YQWO0ORX&v=20120228&limit=50"



if __name__ == "__main__":
    loopcount = 0    
    venues = {}
    while True:
        if loopcount == 0:
            res = 4
        else:
            res = 16
        print loopcount,res
        for i in range(0, res):
            ydiff = (north-south) / float(res)
            for j in range(0, res):
                print i,j
                xdiff = (east-west) / float(res)    
                y = south + ydiff * i
                x = west + xdiff * j
                sw = str(y) + "," + str(x)
                ne = str(y+ydiff) + "," + str(x+xdiff)
                print sw
                print ne
                x = json.loads(urllib.urlopen(url1 + "sw=" + sw + "&ne=" + ne + url2).read())
                pp = pprint.PrettyPrinter()
                if (x["response"].has_key("groups")):
                    for k in range(0, len(x["response"]["groups"][0]["items"])):
                        venue = x["response"]["groups"][0]["items"][k]["venue"]
                        venues[venue["id"]] = {"name":venue["name"], "count":venue["hereNow"]["count"], "lat":venue["location"]["lat"], "long":venue["location"]["lng"]}
                
                 
                f = open("loc2.json", "w") 
                f.write(json.dumps(venues))
                f.write("\n")
                f.flush()
                f.close()
                
        print "rendering"
        os.system("python csv.py > csv_data  && ./munge && python render.py")
        loopcount += 1

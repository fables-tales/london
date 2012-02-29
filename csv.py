import json
import Image
south = 51.416;
north = 51.623;
west = -0.415;
east = 0.179;
if __name__ == "__main__":
    im = Image.open("map.png")
    w = im.size[0]
    h = im.size[1]
    obj = json.loads(open("loc2.json").read())
    for venue in obj:
        value = obj[venue]
        if value["count"] != 0:
            lightradius = value["count"]*255 
            offsetlat = value["lat"] - south
            offsetlong = value["long"] - west
            offsetlongPixels = int(offsetlong / (east-west) * w )
            offsetlatPixels = int(offsetlat / (north-south) * h)

            print lightradius,offsetlongPixels,offsetlatPixels
    f = open("output_image", "w")
    f.write(im.tostring())
    f.flush()
    f.close()

import Image
import json

south = 51.416;
north = 51.623;
west = -0.415;
east = 0.179;
if __name__ == "__main__":
    x = Image.fromstring("RGBA", (2668,1494), open("output_pixel_data").read())
    x.save("lit-map.png", "PNG")
    

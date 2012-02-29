import json
import time

if __name__ == "__main__":
    while True:
        try:
            time.sleep(1)
            f = open("loc.json").read()    
            f2 = open("loc2.json").read()
            o1 = json.loads(f)
            o2 = json.loads(f2)
            x = [o1,o2] 
            f = open("result.json", "w")
            f.write(json.dumps(x))
            f.write("\n")
            f.flush()
            f.close()
       
        except:
            print "fail"

from VoTTConfigurationGenerator import *

if __name__ == "__main__":
    print("Hello")
    obj = VoTTConfiguration()
    obj.CreateDummy()
    print (obj.GetJson())
    
    with open("Image_Source.json", "w") as f:
        f.write(obj.GetJson())
    
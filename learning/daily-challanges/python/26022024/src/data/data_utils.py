import json

class Data:
    path = "../src/data/data.json"
    short_path = "data.json"
    
class Control():
    def __init__(self):
        self.file_name = Data().short_path
    
        with open(self.file_name, "r+", encoding="utf-8") as dfile:
            if len(dfile.read()) == 0:
                with open(self.file_name, "w+", encoding="utf-8") as dfile:
                    json.dump({}, dfile, ensure_ascii=False, indent=4)
            else:
                print("Data load correct.")

class StorageUtils:
    def __init__(self):
        self.dfile = Data().short_path
    
    def path(self):
        return self.dfile
    
    def save_data(self, *args):
        args = list(args)
        result = {
            "name": args[0],
            "unit_price": args[1],
            "quantity": args[3]
        }
        with open()
        
        
        

        
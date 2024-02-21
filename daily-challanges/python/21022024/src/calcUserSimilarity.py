import json

class UserRatingSimilarity():
    
    def __init__(self): 
        self.dataFileName = "../data/usr_movie_rating_data.json"
    
    def _importData(self):
        with open(self.dataFileName, "r") as data_file:
            data = json.load(data_file)
        
        
        for i in data:
            print(data.get(i))

    
    def cosine_similarity(self): 
        
        return 
    
x = UserRatingSimilarity()
print(x._importData())
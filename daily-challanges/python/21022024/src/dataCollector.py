"""
ZBIERANIE DANYCH
- wprowadzanie ocen od uzytkownikow w skali od 1 do 5, gdzie 5 to najwyzsza ocena a 1 to najnizsza

Lista filmow:
-pobieranie uzytkownika
-input od uzytkownika
    -film, ocena
    
Przyklad:
ocena = {
    User1: {
        "nazwa_filmu": "ocena",
        .
        .
    }
}
"""
import json

class dataUtils:
    def __init__(self): pass 
    
    def dumpData(self, data: dict):
        
        dataFileName = "../data/usr_movie_rating_data.json"
        
        try:
            with open(dataFileName, "r+") as dataFile:
                exist_data = json.load(dataFile)
        except FileNotFoundError:
            exist_data = {}
        
        exist_data.update(data)
            
        with open(dataFileName, "w+") as write_data:
            json.dump(exist_data, write_data, indent=4)

class Collection(dataUtils):
    
    def __init__(self, user: str):
        if not isinstance(user, str):
            raise TypeError("Uzytkownik powinien byc typu str.")
        self.user = user.capitalize()
        self.rating = {}
        
    def add_rating(self, movie: str, rate: int):
        if not isinstance(movie, str):
            raise TypeError("")

        if not isinstance(rate, int) or rate < 1 or rate > 5:
            raise ValueError("")
        
        movie = movie.capitalize()
        
        self.rating[movie] = rate

        data = {
            self.user: self.rating
        }
        
        self.dumpData(data)

"""
PRZYKLAD UZYCIA
x = Collection("Marek")
x.add_rating("wladca pierscieni", 2)
x.add_rating("myszka mikki", 3)
"""


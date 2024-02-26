import json
from itertools import combinations
from collections import defaultdict
import math

class UserRatingSimilarity():
    
    def __init__(self, data_file="../data/usr_movie_rating_data.json"):
        self.dataFileName = data_file
        
    def dot_product(self, A: list, B: list):
        if isinstance(A, list) and isinstance(B, list):
            if len(A) != len(B): 
                raise ValueError("Długość wektorów powinna być taka sama")
            
            return sum(a*b for a,b in zip(A, B))
    
    def _importData(self):
        with open(self.dataFileName, "r") as data_file:
            data = json.load(data_file)
        
        self.users = list(data.keys())  # Poprawna inicjalizacja listy użytkowników
    
        oceny_uzytkownikow = []
        for user_ratings in data.values():  # Iteracja po słowniku ocen użytkowników
            oceny_uzytkownikow.append(list(user_ratings.values()))  # Dodanie ocen do listy ocen użytkowników
        
        # Znajdowanie filmów ocenionych przez wszystkich użytkowników
        filmy_ocenione_przez_wszystkich = {}
        for film in filmy_ocenione_przez_wszystkich:
            oceny_dla_wszystkich_filmow[film] = [oceny_uzytkownika.get(film, 0) for oceny_uzytkownika in oceny_uzytkownikow]


        # Zwracanie ocen tylko dla filmów ocenionych przez wszystkich użytkowników
        oceny_dla_wszystkich_filmow = {}
        for film in filmy_ocenione_przez_wszystkich:
            oceny_dla_wszystkich_filmow[film] = [oceny_uzytkownika[film] for oceny_uzytkownika in oceny_uzytkownikow]

        dot_product_result = {}
        vector_len = {}
        similarity = {}
        
        for usr1_idx, usr2_idx in combinations(range(len(self.users)), 2):
            usr1 = self.users[usr1_idx]
            usr2 = self.users[usr2_idx]
            
            usr_rates1 = oceny_uzytkownikow[usr1_idx]
            usr_rates2 = oceny_uzytkownikow[usr2_idx]
            
            product = self.dot_product(usr_rates1, usr_rates2)
            dot_product_result[usr1, usr2] = product
            
            usr1Len = math.sqrt(sum(rate**2 for rate in usr_rates1))
            usr2Len = math.sqrt(sum(rate**2 for rate in usr_rates2))
                
            vector_len[(usr1, usr2)] = (usr1Len, usr2Len)
            
            if usr1Len != 0 and usr2Len != 0:
                similarity[(usr1, usr2)] = product / (usr1Len * usr2Len)
            else:
                similarity[(usr1, usr2)] = 0
        """
        # Wydruk wyników
        print("Iloczyn skalarny dla każdej pary ocen użytkowników:")
        for para, iloczyn in dot_product_result.items():
            print(f"{para}: {iloczyn}")
        print("\n\n")
        
        print("Długości (normy) wektorów dla każdej pary ocen użytkowników:")
        for para, (dlugosc1, dlugosc2) in vector_len.items():
            print(f"{para}: Użytkownik 1 - {dlugosc1}, Użytkownik 2 - {dlugosc2}")
        print("\n\n")
        
        print("Podobieństwo kosinusowe między użytkownikami:")
        for para, podobienstwo in similarity.items():
            print(f"{para}: {podobienstwo}")
        """
        """
        Iloczyn skalarny dla każdej pary ocen użytkowników:
        ('Marek', 'Arek'): 83
        ('Marek', 'Kasia'): 61
        ('Marek', 'Wojtek'): 48
        ('Marek', 'Kuba'): 67
        ('Marek', 'Aneta'): 52
        ('Arek', 'Kasia'): 81
        ('Arek', 'Wojtek'): 65
        ('Arek', 'Kuba'): 90
        ('Arek', 'Aneta'): 74
        ('Kasia', 'Wojtek'): 73
        ('Kasia', 'Kuba'): 77
        ('Kasia', 'Aneta'): 60
        ('Wojtek', 'Kuba'): 61
        ('Wojtek', 'Aneta'): 42
        ('Kuba', 'Aneta'): 68



        Długości (normy) wektorów dla każdej pary ocen użytkowników:
        ('Marek', 'Arek'): Użytkownik 1 - 8.54400374531753, Użytkownik 2 - 10.392304845413264
        ('Marek', 'Kasia'): Użytkownik 1 - 8.54400374531753, Użytkownik 2 - 9.539392014169456
        ('Marek', 'Wojtek'): Użytkownik 1 - 8.54400374531753, Użytkownik 2 - 8.366600265340756
        ('Marek', 'Kuba'): Użytkownik 1 - 8.54400374531753, Użytkownik 2 - 10.0
        ('Marek', 'Aneta'): Użytkownik 1 - 8.54400374531753, Użytkownik 2 - 7.874007874011811
        ('Arek', 'Kasia'): Użytkownik 1 - 10.392304845413264, Użytkownik 2 - 9.539392014169456
        ('Arek', 'Wojtek'): Użytkownik 1 - 10.392304845413264, Użytkownik 2 - 8.366600265340756
        ('Arek', 'Kuba'): Użytkownik 1 - 10.392304845413264, Użytkownik 2 - 10.0
        ('Arek', 'Aneta'): Użytkownik 1 - 10.392304845413264, Użytkownik 2 - 7.874007874011811
        ('Kasia', 'Wojtek'): Użytkownik 1 - 9.539392014169456, Użytkownik 2 - 8.366600265340756
        ('Kasia', 'Kuba'): Użytkownik 1 - 9.539392014169456, Użytkownik 2 - 10.0
        ('Kasia', 'Aneta'): Użytkownik 1 - 9.539392014169456, Użytkownik 2 - 7.874007874011811
        ('Wojtek', 'Kuba'): Użytkownik 1 - 8.366600265340756, Użytkownik 2 - 10.0
        ('Wojtek', 'Aneta'): Użytkownik 1 - 8.366600265340756, Użytkownik 2 - 7.874007874011811
        ('Kuba', 'Aneta'): Użytkownik 1 - 10.0, Użytkownik 2 - 7.874007874011811



        Podobieństwo kosinusowe między użytkownikami:
        ('Marek', 'Arek'): 0.9347700401192889
        ('Marek', 'Kasia'): 0.7484240052572747
        ('Marek', 'Wojtek'): 0.6714764524710394
        ('Marek', 'Kuba'): 0.7841756862140749
        ('Marek', 'Aneta'): 0.7729405090241419
        ('Arek', 'Kasia'): 0.8170571691028833
        ('Arek', 'Wojtek'): 0.7475710226208838
        ('Arek', 'Kuba'): 0.8660254037844386
        ('Arek', 'Aneta'): 0.904323875965012
        ('Kasia', 'Wojtek'): 0.9146462201344733
        ('Kasia', 'Kuba'): 0.8071793242758771
        ('Kasia', 'Aneta'): 0.7987938443763455
        ('Wojtek', 'Kuba'): 0.7290894516939801
        ('Wojtek', 'Aneta'): 0.6375355777548621
        ('Kuba', 'Aneta'): 0.8636008636012954
        None

        """
        
        return dot_product_result, vector_len, similarity


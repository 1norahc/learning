import random

from dataCollector import Collection


fUsers = [
    "Marek",
    "Arek",
    "Kasia",
    "Wojtek",
    "Kuba",
    "Aneta"
]

fMovies = [
    "Władca pierścieni",
    "Arielka",
    "Szybcy i wściekli 3",
    "Myszka Mikki",
    "Pan Kleks",
    "Diuna",
    "Iron Man",
    "Avengers: Czas Ultrona"
]

fRate = [
    1,2,3,4,5
]

def _initFakeUsers():
    for user in fUsers:
        z = Collection(user)
        for i in range(5):
            z.add_rating(random.choice(fMovies), random.choice(fRate))
            
if __name__ == "__main__":
    for _ in range(5): 
        _initFakeUsers()
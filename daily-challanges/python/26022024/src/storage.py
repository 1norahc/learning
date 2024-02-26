# Zarzadzanie magazynem

"""
TODO:
1. Dodawanie nowych produktow do magazynu
2. Usuwanie produktow z magazynu
3. Aktualizacja ilosci produktow w magazynie
4. Wyswietlanie aktulanego stanu magazynu

"""

from data.data_utils import Control, Data, StorageUtils

try:
    Control()
except Exception as e:
    print(e)

class Storage(StorageUtils):
    def __init__(self, data_file_name=self.path()):
        self.dfile = data_file_name
        
    def add_product(self, name: str, unit_price: float, quantity: int):
        if isinstance(name, str):
            raise ValueError("`name` varible should be an string.")
        if isinstance(unit_price, float):
            raise ValueError("`name` varible should be an float.")
        if isinstance(quantity, int):
            raise ValueError("`name` varible should be an int.")
        
        
        
        
        return
    
    def remove(self, product_name):
        # Usun produkt z magazynu
        return
    
    def update(self, name, quantity, T=None):
        # zaaktualizuj ilosc produktu w magazynie
        # jesli T=Q wtedy zaaktualizuj ilosc, jesli T=P, zaaktualizuj cene produktu
        return
    
    def find(self, product_name):
        # znajdz produkt
        return
    
    def stock_status(self):
        # ilosc produktow w magazynie
        return


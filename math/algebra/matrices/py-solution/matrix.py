


import random

def combineRandomMatrix(rows=3, cols=3):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(-50, 50))  # Zakres losowych wartości - zakładamy liczby całkowite od 1 do 10, można zmienić
        matrix.append(row)
    return matrix





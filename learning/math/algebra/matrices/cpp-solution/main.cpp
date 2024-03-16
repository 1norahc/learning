#include <iostream>
#include <vector>
#include <cstdlib> // zawiera funkcję rand()

using namespace std;

// Funkcja do generowania losowej macierzy
vector<vector<int>> generateRandomMatrix(int rows, int cols) {
    vector<vector<int>> matrix;
    for (int i = 0; i < rows; ++i) {
        vector<int> row;
        for (int j = 0; j < cols; ++j) {
            row.push_back(rand() % 10 + 1); // Zakres losowych wartości - zakładamy liczby całkowite od 1 do 10, można zmienić
        }
        matrix.push_back(row);
    }
    return matrix;
}

// Funkcja do drukowania macierzy
void printMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int value : row) {
            cout << value << " ";
        }
        cout << endl;
    }
}

int main() {
    srand(time(NULL)); // Inicjalizacja generatora liczb pseudolosowych
    int rows, cols;
    cout << "Podaj liczbe wierszy macierzy: ";
    cin >> rows;
    cout << "Podaj liczbe kolumn macierzy: ";
    cin >> cols;

    vector<vector<int>> randomMatrix = generateRandomMatrix(rows, cols);

    cout << "Wygenerowana losowa macierz:" << endl;
    printMatrix(randomMatrix);

    return 0;
}

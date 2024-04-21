public class lab1_zadania {
    public static int srednia(int ocena1, int ocena2, int ocena3) {
        double srednia_ocen;
        srednia_ocen = (ocena1 + ocena2 + ocena3 ) / 3;
        System.out.println("Srednia ocen wynosi " + srednia_ocen);
        return 0;
    }

    public static int liczba_calkowita(int x) {
        if (x % 2 == 0) {
            System.out.println("Podana liczba jest calkowita");
        } else {
            System.out.println("Podana liczba nie jest calkowita");
        }
        return 0;
    }

    public static int czy_liczba(int a, int b) {
        boolean sprawdz = a <= b;
        System.out.println(sprawdz);
        return 0;
    }

    public static int pole(int a, int h) {
        double p = (a*h)/2;
        System.out.println("Pole wynosi " + p);
        return 0;
    }

    public static int reszta(int x, int y) {
        int reszta = x % y;
        System.out.println("Reszta z dzielenia liczb " + x + " i " + y + " wynosi " + reszta);
        return 0; 
    }

    public static void main(String[] args) {
        System.out.println("Zadanie 1:");
        srednia(3, 5, 6);

        System.out.println("Zadanie 2: ");
        liczba_calkowita(6);

        System.out.println("Zadanie 3: ");
        czy_liczba(3, 8);

        System.out.println("Zadanie 4:");
        pole(2, 4);

        System.out.println("Zadanie 5");
        reszta(5, 2);
    }
}
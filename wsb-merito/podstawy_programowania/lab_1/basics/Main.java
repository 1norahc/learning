public class Main {
    public static int isEqual(int x, int y) {
        if(x==y) {
            return 1;
        }else {
            return 0;
        }
    }
    public static int _for_test(int x) {
        for(int i=1; i<x; i++) {
            System.out.println(i);
        }
        return 0;
    }
    public static void main(String[] args) {
        int liczba = 10; liczba = 12;

        float liczba2 = 10.10F; liczba2 = 12.1F;

        double l3 = 10.10; l3 = 12.12;

        boolean b = true; b = false;

        char znak = 'a';
        String d = "Hello World";

        liczba = 2+2;
        System.out.println(liczba);

        liczba = 6 - 1;
        System.out.println(liczba);

        liczba = 2*2;
        System.out.println(liczba);

        liczba = 4/2;
        System.out.println(liczba);

        liczba = 100/5;
        liczba /= 2;
        System.out.println(liczba);

        liczba = 11%2;
        System.out.println(liczba);

        int l1; int l2;
        l1 = 10; l2 = 20;
        if (l1 == l2) {
            System.out.println(true);
        }else {
            System.out.println(false);
        }

        System.out.println("Test funckji sprawdzajacej czy liczby sa rowne, 1-tak, 0-nie");
        System.out.println(isEqual(3, 3));

        System.out.println("Test petli for:");
        System.out.println(_for_test(10));

        // rzutowanie
        int rz = (int)10;
        System.out.println(rz);

        double test = (double)rz;
        System.out.println(test);

        System.out.println();

        //wyrazenie warunkowe
        System.out.println("wyrazenie warunkowe");
        int liczba_testowa = 11;
        int ww = liczba_testowa == 10 ? 5 : 2;
        System.out.println(ww);

        if (liczba == 10) {
            ww = 5;
        }else {
            ww = 2;
        }
        System.out.println(ww);

        int liczba_s = 10;
        switch(liczba_s) {
            case 1:
                System.out.println(1);
                break;
            case 2:
                System.out.println(2);
                break;
            case 9:
                System.out.println(10);
                break;
            default:
                System.out.println("inna liczba");
                break;
        }

    }
}
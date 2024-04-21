package zad1;

public class lab2_z1 {

    // 1. Obliczy liczbę słów w tekście.

    public static int sposob1(String text) {
        return text.length();
    }

    public static int sposob2(String text) {
        int sum = 0;
        for(int i=0; i<text.length(); i++){
            sum++;
        }
        return sum;
    }

    public static int sposob2_1(String text) {
        int sum = 0;
        for(int i = 0; i<text.length(); i++) {
            if (text.charAt(i) != ' ') { 
                sum++;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println("Ilość słów w twoim tekście wynosi:");

        System.out.println();

        System.out.println("Sposób 1:");
        System.out.println(sposob1("To jest przykładowy tekst")); // poprawny wynik - 25

        System.out.println();

        System.out.println("Sposób 2:");
        System.out.println(sposob2("To jest przykładowy tekst")); // poprawny wynik - 25

        System.out.println();

        System.out.println("Sposób 2 (bez spacji):");
        System.out.println(sposob2_1("To jest przykładowy tekst")); // poprawny wynik - 22
    }
}

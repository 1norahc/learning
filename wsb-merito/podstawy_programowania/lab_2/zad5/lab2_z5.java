package zad5;

public class lab2_z5 {
    
    //  5. Zliczy ilość wystąpień każdej litery w tekście.

    public static void foo(String text) {
        text = text.toLowerCase();

        int[] iloscLiter = new int[26];

        int index;
        
        for(int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c >= 'a' && c <= 'z') {
                index = c - 'a';
                iloscLiter[index]++;
            }
        }

        for (char c='a'; c<='z'; c++) {
            index = c - 'a';
            if (iloscLiter[index] > 0) { 
                System.out.println("Litera " + c + " wystąpiła " + iloscLiter[index] + " razy.");
            }
        }
    }

    public static void main(String[] args) {
        foo("To jest przykładowy tekst z którego będą zczytywane litery");
    }
}
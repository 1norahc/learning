package zad3;

public class lab2_z3 {
    
    // 3. Sprawdzi, czy tekst zawiera określone słowo (np. "Java") i wyświetli informację o jego wystąpieniu.

    public static void foo(String text) {
        int count_java = 0;

        String[] words = text.split(" ");

        for (String word : words) {
            if (word.equals("Java")) {
                count_java++;
            }
        }
        System.out.println("W podanym tekście słowo 'Java' wystąpiło tyle razy:");
        System.out.println(count_java);
    }

    public static void main(String[] args) {
        foo("W tym tekście nie znajduje się ŻADNE słowo Java i nikt nie powinien się tutaj słowa takiego jak Java spodziewać!");
    }
}

package zad2;

public class lab2_z2 {
    
    //  2. Znajdzie najdłuższe i najkrótsze słowo w tekście.

    public static void foo(String text) {
        String[] words = text.split(" ");

    String shortest = words[0];
    String longest = words[0];

    for (String word : words) {
        if (word.length() < shortest.length()) {
            shortest = word;
        }
        if (word.length() > longest.length()) {
            longest = word;
        }
    }

    System.out.println("Najkrótsze słowo: " + shortest);
    System.out.println("Najdłuższe słowo: " + longest);
    }

    public static void main(String[] args) {
        foo("To jest przykładowy tekst do sprawdzenia które słowo w nim jest nadłusze, a które najkrótsze.");
    }
}

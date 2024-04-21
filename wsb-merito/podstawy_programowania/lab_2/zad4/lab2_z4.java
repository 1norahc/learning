package zad4;

public class lab2_z4 {

    // 4. Zamieni wszystkie litery w tekście na małe litery.

    public static void foo(String text) {
        System.out.println("To jest tekst z zamienionymi wszystkimi literami na małe: ");
        System.out.println(text.toLowerCase());
    }

    public static void main(String[] args) {
        foo("Czy w tym TEKŚCIE ZnajDUJA sIĘ DUŻE literY?");
    }
}

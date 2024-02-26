
// Write a function that takes in the radius as input and returns the
// circumference of a circle(c = 2*3.14*radius).
import java.util.*;

public class circumferencefunction {
    public static void circumFerenceCirlce(int radius) {
        double x = 2 * 22 / 7 * radius;
        System.out.println(x);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the radius");
        int radius = sc.nextInt();
        circumFerenceCirlce(radius);
    }
}

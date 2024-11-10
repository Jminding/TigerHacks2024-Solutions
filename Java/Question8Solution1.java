import java.util.Scanner;

public class Question8Solution1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double a = sc.nextDouble();
		double b = sc.nextDouble();
		double c = sc.nextDouble();
		double d = sc.nextDouble();

		double x = c / (1 - a + c);
		System.out.println(roundTo6(x) + " " + roundTo6(1 - x));
	}

	static double roundTo6(double value) {
		return Math.round(value * 1e6) / 1e6;
	}
}

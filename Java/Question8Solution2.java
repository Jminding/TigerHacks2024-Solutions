import java.util.Scanner;

public class Question8Solution2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double a = sc.nextDouble();
		double b = sc.nextDouble();
		double c = sc.nextDouble();
		double d = sc.nextDouble();

		double[][] m = new double[][] {{a, b}, {c, d}};

		double[][] m2 = m;

		for (int i = 0; i < 10000; i++) {
			m2 = mm(m2, m);
		}

		System.out.println(roundTo6(m2[0][0]) + " " + roundTo6(m2[0][1]));
	}

	static double roundTo6(double value) {
		return Math.round(value * 1e6) / 1e6;
	}

	static double[][] mm(double[][] a, double[][] b) {
		return new double[][] {
			{a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]},
			{a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]}
		};
	}
}

import java.util.Scanner;

public class Question6 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		int[] x = new int[n];
		int[] y = new int[n];

		for (int i = 0; i < n; i++) {
			x[i] = sc.nextInt();
			y[i] = sc.nextInt();
		}

		double area = 0;
		for (int i = 0; i < n ; i++) {
			int j = (i + 1) % n;
			area += x[i] * y[j] - x[j] * y[i];
		}

		area = Math.abs(area) / 2;
		System.out.println((int) Math.round(area));
	}
}

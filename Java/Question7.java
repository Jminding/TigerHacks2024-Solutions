import java.util.Scanner;

public class Question7 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();

		byte[] b = new byte[10];
		int p = 0;

		for (int i = 0; i < n; i++) {
			String[] s = sc.nextLine().split(" ");
			int c = Integer.parseInt(s[1], Integer.parseInt(s[0]));
			switch(c) {
				case '>': p = (p + 1) % 10; break;
				case '<': p = (p + 9) % 10; break;
				case '+': b[p]++; break;
				case '-': b[p]--; break;
				case '.': System.out.print((char) b[p]); break;
			}
		}
	}
}

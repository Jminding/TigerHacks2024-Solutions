import java.util.Scanner;

public class Question9 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String t = sc.nextLine();
		int n = sc.nextInt();
		sc.nextLine();

		for (int i = 0; i < n; i++) {
			if(t.contains(sc.nextLine())) {
				System.out.println(i + " ");
			}
		}
	}
}

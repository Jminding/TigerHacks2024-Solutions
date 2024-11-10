import java.util.Scanner;

public class Question2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] input = sc.nextLine().split(" ");
		int n = Integer.parseInt(input[1]);

		char[] s = sc.nextLine().toCharArray();

		for(int x = 0; x < n; x++) {
			String[] line = sc.nextLine().split(" ");
			int i = Integer.parseInt(line[0]);
			int j = Integer.parseInt(line[1]);

			char temp = s[i];
			s[i] = s[j];
			s[j] = temp;
		}

		System.out.println(new String(s));
	}
}

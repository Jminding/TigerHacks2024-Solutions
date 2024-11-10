import java.util.Scanner;

public class Question4 {
	public static void main(String[] args) {
		final int shift = 16;
		char[] s = new Scanner(System.in).nextLine().toCharArray();
		String r = "";
		for(char c : s) {
			if(c == ' ') r += c;
			else r += (char) ((c - (shift - 65)) % 26 + 65);
		}

		System.out.println(r);
	}
}

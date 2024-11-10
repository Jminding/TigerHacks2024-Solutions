import java.util.Scanner;

public class Question5 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		scanner.nextLine();

		int[][][] arr = new int[n][5][5];

		for (int k = 0; k < n; k++) {
			for (int i = 0; i < 5; i++) {
				String[] row = scanner.nextLine().split(" ");
				for (int j = 0; j < 5; j++) {
					if (row[j].equals("?")) {
						arr[k][i][j] = i + j + 2 * k + 1;
					} else {
						arr[k][i][j] = Integer.parseInt(row[j]);
					}
				}
			}
		}

		int maxK = 0, maxI = 0, maxSum = 0;

		for (int k = 0; k < n; k++) {
			for (int i = 0; i < 5; i++) {
				int currSum = 0;
				for (int j = 0; j < 5; j++) {
					currSum += arr[k][i][j];
				}
				if (currSum > maxSum) {
					maxK = k;
					maxI = i;
					maxSum = currSum;
				}
			}
		}

		System.out.println(maxK + " " + maxI);
	}
}

import java.util.Scanner;

public class Question3 {
	static class Node {
		final int data;
		Node left, right;

		Node(int d) {
			data = d;
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Node root = new Node(sc.nextInt());

		for(int i = 1; i < n; i++) {
			int data = sc.nextInt();
			Node c = root;
			while(true) {
				if(data <= c.data) {
					if(c.left == null) {
						c.left = new Node(data);
						break;
					} else {
						c = c.left;
					}
				} else {
					if(c.right == null) {
						c.right = new Node(data);
						break;
					} else {
						c = c.right;
					}
				}
			}
		}

		System.out.println(countNoChildren(root));
	}

	static int countNoChildren(Node root) {
		if(root == null) return 0;
		if(root.left == root.right) return root.data;
		return countNoChildren(root.left) + countNoChildren(root.right);
	}
}

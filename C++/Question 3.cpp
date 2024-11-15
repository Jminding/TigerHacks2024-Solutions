#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class node {
    public:
        int data;
        node* left;
        node* right;

        node(int value) : data(value), left(nullptr), right(nullptr) {}
};

int sumNoChildren(node* root) {
    if (root == nullptr) {
        return 0;
    } else if (root->left == nullptr && root->right == nullptr) {
        return root->data;
    }
    return sumNoChildren(root->left) + sumNoChildren(root->right);
}

int main() {
    int n;
    cin >> n;
    n -= 1;
    node* root = new node(0);
    int initial_root;
    cin >> initial_root;
    root->data = initial_root;

    for (int i = 0; i < n; i++) {
        int data;
        cin >> data;
        node* current = root;
        while (true) {
            if (data <= current->data) {
                if (current->left == nullptr) {
                    node* n = new node(0);
                    n->data = data;
                    current->left = n;
                    break;
                } else {
                    current = current->left;
                }
            } else {
                if (current->right == nullptr) {
                    current->right = new node(data);
                    break;
                } else {
                    current = current->right;
                }
            }
        }
    }

    cout << sumNoChildren(root) << endl;

    return 0;
}
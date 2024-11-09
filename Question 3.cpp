// #include <iostream>
// #include <string>
// #include <algorithm>

// using namespace std;

// class node {
//     public:
//         int data;
//         node* left;
//         node* right;
// };

// int main() {
//     int n;
//     cin >> n;
//     n -= 1;
//     node root;
//     int initial_root;
//     cin >> initial_root;
//     root.data = initial_root;

//     for (int i = 0; i < n; i++) {
//         int data;
//         cin >> data;
//         node current = root;
//         while (true) {
//             if (data <= current.data) {
//                 if (current.left == NULL) {
//                     node n;
//                     n.data = data;
//                     current.left = n;
//                     break;
//                 } else {
//                     current = current.left;
//                 }
//             }
//         }
//     }
// }
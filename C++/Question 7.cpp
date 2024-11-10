#include <iostream>
#include <vector>
#include <string>

#define vi vector<int>

using namespace std;

int main() {
    vi arr(10, 0);
    int p = 0;
    int n;
    
    cin >> n;
    cin.ignore();

    for (int x = 0; x < n; x++) {
        string input;
        getline(cin, input);

        int base = stoi(input.substr(0, input.find(":")));
        int value = stoi(input.substr(input.find(":") + 1), nullptr, base);
        char i = static_cast<char>(value);

        if (i == '>') {
            p = (p + 1) % arr.size();
        } else if (i == '<') {
            p = (p - 1 + arr.size()) % arr.size();
        } else if (i == '+') {
            arr[p] = (arr[p] + 1) % 256;
        } else if (i == '-') {
            arr[p] = (arr[p] - 1 + 256) % 256;
        } else if (i == '.') {
            cout << static_cast<char>(arr[p]);
        }
    }

    return 0;
}

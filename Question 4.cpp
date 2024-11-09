#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define SHIFT 16

using namespace std;

int main() {
    string s;
    getline(cin, s); // just using cin >> s will skip spaces, so use this instead

    string out;

    for (char c : s) {
        if (c == ' ') {
            out += ' ';
        } else {
            out += static_cast<char>((((c - 'A' - SHIFT) + 26) % 26) + 'A');
        }
    }

    cout << out << endl;
    
    return 0;
}
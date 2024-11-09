#include <iostream>
#include <string>

using namespace std;

int main() {
    int L, n;
    cin >> L >> n;
    string s;
    cin >> s;

    for (int x = 0; x < n; x++) {
        int i, j;
        cin >> i >> j;
        int temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }

    cout << s << endl;
    return 0;
}
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define vi vector<int>

using namespace std;

int main() {
    string t;
    cin >> t;
    int n;
    cin >> n;
    string words[n];
    for (int i = 0; i < n; i++) {
        cin >> words[i];
    }
    vi ret;

    for (int i = 0; i < n; i++) {
        if (t.find(words[i]) != string::npos) {
            ret.push_back(i);
        }
    }

    sort(ret.begin(), ret.end());

    for (int i = 0; i < ret.size(); i++) {
        cout << ret[i] << " ";
    }

    return 0;
}
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin >> n;
    int x[n], y[n];

    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i];
    }

    double area = 0;
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        area += (x[i] * y[j] - x[j] * y[i]);
    }

    area = abs(area) / 2;
    if (n == 2) {
        area = 0;
    }
    cout << static_cast<int>(area + 0.5) << endl;

    return 0;
}
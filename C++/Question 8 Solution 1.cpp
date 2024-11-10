#include <iostream>
#include <cmath>

using namespace std;

double round_to_six(double value) {
    return round(value * 1e6) / 1e6;
}

int main() {
    double a, b, c, d;
    cin >> a >> b >> c >> d;

    double x = c / (1 - a + c);
    double y = 1 - x;

    cout << round_to_six(x) << " " << round_to_six(y) << endl;

    return 0;
}

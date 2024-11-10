#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

#define vvd vector<vector<double>>

using namespace std;

vvd matrix_multiply(const vvd& a, const vvd& b) {
    vvd ret(2, vector<double>(2));

    ret[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0];
    ret[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1];
    ret[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0];
    ret[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1];

    return ret;
}

int main() {
    double a, b, c, d;
    cin >> a >> b >> c >> d;

    vvd matrix = {{a, b}, {c, d}};
    vvd original_matrix = {{a, b}, {c, d}};

    for (int i = 0; i < 20000; i++) {  // practically infinite loop
        matrix = matrix_multiply(matrix, original_matrix);
    }

    double ans_a = round(matrix[0][0] * 1e6) / 1e6;
    double ans_b = round((1 - ans_a) * 1e6) / 1e6;

    cout << ans_a << " " << ans_b << endl;

    return 0;
}

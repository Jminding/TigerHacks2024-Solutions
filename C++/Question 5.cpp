#include <iostream>
#include <string>
#include <numeric>

using namespace std;

int main() {
    int n;
    cin >> n;
    int ans[n][5][5];
    string arr[n][5][5];

    for (int x = 0; x < n; x++) {
        for (int i = 0; i < 5; i++) {
            cin >> arr[x][i][0] >> arr[x][i][1] >> arr[x][i][2] >> arr[x][i][3] >> arr[x][i][4];
        }
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (arr[k][i][j] == "?") {
                    ans[k][i][j] = i + j + 2 * k + 1;
                } else {
                    ans[k][i][j] = stoi(arr[k][i][j]);
                }
            }
        }
    }

    int max_k = 0;
    int max_i = 0;
    int max_sum = 0;

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                int curr_sum = 0;
                for(auto& num : ans[k][i]) curr_sum += num;
                if (curr_sum > max_sum) {
                    max_k = k;
                    max_i = i;
                    max_sum = curr_sum;
                }
            }
        }
    }

    cout << max_k << " " << max_i << endl;

    return 0;
}
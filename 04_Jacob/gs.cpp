#include <bits/stdc++.h>
using namespace std;

double answer[50][3];

double B[3][3] = {0, -0.4, -0.2, 0, 0.1, -0.45, 0, -0.11, 0.095 };
double b[3] = { -2.4, 5.6, -1.86};

int main() {
    int n;
    cin >> n;
    answer[0][0] = 0, answer[0][1] = 0, answer[0][2] = 0;
    // answer.push_back(sol);
    for (int cnt = 0; cnt < n; ++ cnt) {
        // float temp[3];
        answer[cnt+1][0] = B[0][0] * answer[cnt][0] + B[0][1] * answer[cnt][1] + B[0][2] * answer[cnt][2] + b[0];
        answer[cnt+1][1] = B[1][0] * answer[cnt][0] + B[1][1] * answer[cnt][1] + B[1][2] * answer[cnt][2] + b[1];
        answer[cnt+1][2] = B[2][0] * answer[cnt][0] + B[2][1] * answer[cnt][1] + B[2][2] * answer[cnt][2] + b[2];
        // answer.push_back(temp);
    }

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cout << B[i][j] << " ";
        }
        cout << endl;
    }

    for(int i = 0; i< 3; ++i) {
        cout << b[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < n; ++ i) {
        cout << "[" << i << "]: " << answer[i][0] << " " << answer[i][1] << " " << answer[i][2] << endl;
    }
}
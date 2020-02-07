#include <bits/stdc++.h>
using namespace std;

double H[20][20];
double L[20][20];s

void hilbert(int n) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            H[i][j] = 1.0 / (i + j + 1);
        }
    }
}

void chol() {
    
} 


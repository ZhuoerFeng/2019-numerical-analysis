#include <bits/stdc++.h>
using namespace std;

float series1(int n) {
    float sum = 0;
    for (int i = 1; i <= n; ++i) {
        sum += (float) (1.0 / i);
    }
    return sum;
}

double series2(long long n) {
    double sum = 0;
    for (long long i = 1; i <= n; ++i) {
        sum += (double) (1.0 / i);
    }
    return sum;
}

int main() {
    for (int i = 2097100; i < 2097300; i++) {
        printf("single: input %d, output... %.20f\n", i, series1(i));
    }

    for (long long i = 2097100; i < 2097300; i++) {
        printf("double: input %lld, output... %.20lf\n", i, series2(i));
    }

    cout << series2(2097152) - series1(2097152) << endl;

    return 0;
}
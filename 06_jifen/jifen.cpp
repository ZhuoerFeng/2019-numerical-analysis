#include <bits/stdc++.h>
using namespace std;

double f(double t) {
    double f = t / (4 + t * t);
    return f;
}


int main() {
    double h = 1.0 / 8;
    double sum = 0;
    double t = 0;
    for (int i = 1; i <= 7; ++i) {
        t = i * h;
        printf("t = %lf, t + 1/2 = %lf\n", t, t + 0.5 * h );
        double temp = 2 * f(t) + 4 * f(t + 0.5 * h);
        sum += temp;
        cout << sum << endl;
    }
    sum += sum + 4 * f(h / 2);
    sum += sum + f(0) + f(1);
    sum = sum * h / 48;
    cout << sum << endl;
    cout << (0.5 * log(5.0 / 4)) << endl;
    return 0;
}
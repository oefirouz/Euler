#include <cstdio>
#include <cstdlib>
#include <iostream>


using namespace std;

int isPrime(int n) {
    if (n < 2) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    int i = 3;
    while (i*i <= n) {
        if (n % i == 0) return 0;
        i += 2;
    }
    return 1;
}

int main() {
    int length;
    int primeCount = 0;
    int corner = 1;
    for (length = 3; ; length += 2) {
        for (int i = 0; i < 4; i++) {
            corner += length - 1;
            if (isPrime(corner)) primeCount++;
        }
        if (primeCount / ((float) (1 + 4*((length) - 1)/2)) < .1) break;
    }

    printf("%d\n", length);
    return 0;
}
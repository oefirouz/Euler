#define N 30

#include <stdio.h>
#include <stdlib.h>

int main() {
    long long int n = 1 << N;
    long long int count = 0;
    long long int i;
    for (i = 1; i <= n; i++) {
        if ((i ^ (2*i) ^ (3*i)) == 0) {
            count += 1;
        }
    }
    printf("%lld\n", count);
    return 0;
}
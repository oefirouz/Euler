#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
#define N 100000000

int primes(char** isPrimePointer, int limit) {
    char* ptr;
    ptr = (char*) malloc(sizeof(char)*(limit+1));
    assert(ptr != NULL);
    int i, j;
    ptr[1] = 0;
    ptr[2] = 1;
    for (i = 3; i < limit; i += 2) {
        ptr[i] = 1;
        ptr[i+1] = 0;
    }
    if (limit % 2 == 1) ptr[limit] = 1;

    for (i = 3; i <= limit; i += 2) {
        if (i != 0) {
            for (j = i+i; j <= limit; j += i) {
                ptr[j] = 0;
            }
        }
    }
    int primeCount = 1;
    for (i = 3; i <= limit; i += 2) {
        if (ptr[i] == 1) primeCount++;
    }
    *isPrimePointer = ptr;
    return primeCount;
}

int main() {
    char* isPrime;
    int primeCount = primes(&isPrime, N+1);
    int i, j;
    double upperCheck;
    long long int sum = 1;
    for (i = 2; i <= N; i += 2) {
        if (isPrime[i+1]*isPrime[(i/2) + 2]) {
            upperCheck = sqrt(i);
            sum += i;
            for (j = 3; j <= upperCheck; j++) {
                if (i % j == 0) {
                    if (isPrime[(i/j) + j] == 0) {
                        sum -= i;
                        break;
                        break;
                    }
                }
            }
        }
    }
    printf("%lld\n", sum);
    return 0;
}

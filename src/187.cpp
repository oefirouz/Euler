#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cstdlib>
using namespace std;

#define UPPER 50000000

int isPrime[UPPER + 1];

void init_isPrime(int b) {
    int i,j;
    for(i = 4; i <= b; i += 2) isPrime[i] = 0;
    for(i = 3; i <= b; i += 2) isPrime[i] = 1;
    isPrime[2] = 1;
    for(i = 3; i*i < b; i += 2) {
        if (isPrime[i]) {
            for(j = i+i; j <= b; j += i) {
                isPrime[j] = 0; 
            }
        }
    }
}

int main() {
    int count;
    init_isPrime(UPPER);
    vector<int> primeList(0,0);
    for(int i = 2; i <= UPPER; i++) {
        if (isPrime[i] == 1) primeList.push_back(i);
    }

    for(vector<int>::iterator i = primeList.begin(); i != primeList.end(); i++) {
        for(vector<int>::iterator j = primeList.begin(); j <= i; j++) {
            if ((*i)*(*j) > 100000000) {
                break;
            } else if ((*i)*(*j) < 100000000) {
                count += 1;
            }
        }
    }
    printf("%d\n", count);
    return 0;
}
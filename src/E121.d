//

import std.stdio;

const int N = 15;

long factorial(int n) {
    long cum = 1;
    while (n > 1) {
        cum *= n--;
    }
    return cum;
}

long count(int cur, int req, int depth, int max) {
    if (cur == req) {
       long cum = 1;
        foreach (i; depth + 2 .. max + 2) {
            cum *= i;
        }
        return cum;
    } else if ((max-depth) < (req - cur)) {
        return 0;
    } else {
        return (count(cur + 1, req, depth + 1, max) + (depth+1)*count(cur, req, depth + 1, max));
    }
}

void main() {
    long outcomes = factorial(N+1);
    long wins = count(0,N/2 + 1,0,N);
    writeln(outcomes/wins);
}

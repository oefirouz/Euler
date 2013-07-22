import std.stdio, std.math;

const uint N = 1000000;

void main() {
    uint temp, M = 0, count = 0;
    while (M += 1) {
    	foreach (i; 1 .. M+1) {
    		foreach (j; i .. M+1) {
    			temp = (i+j)^^2 + M^^2;
    			if (temp == (cast (uint) sqrt(cast (float) temp))^^2) {
    				count += 1;
    			}
    		}
    	}
	    if (count > N) {
	   		writeln(M);
	   		break;
	   	}
    }
}
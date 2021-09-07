#include <math.h>
#include <time.h>
#include <windows.h>
#include <stdio.h>
__declspec(dllexport) float speedy_sqrt(float num, float speedFactor) {
        double n, n2, xF;
        if (num == 0) {
            return 0;
        }
        n = num/2;
        n2 = n + 1;
        while (fabs(n - n2) > speedFactor*n){
            xF = num/n;
            n2 = n;
            n = (n2 + xF) / 2;
        }
        return n;
}

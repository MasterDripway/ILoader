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
__declspec(dllexport) int * genArr() {
    static int array[1024];;
    for (int i=0; i < 1024; i++) {
        array[i] = i;
    }
    return array;

}
int main() {
    int arraysize = pow(10, 3);
    printf("full comp size: %d\n", arraysize);
    time_t t1, t2;
    int *array;
    double dt;
    time(&t1);
    /*
    for (int i=0; i <= arraysize; i++) {
        speedy_sqrt(i, 1);
    }*/
    array = genArr();
    time(&t2);
    dt = difftime(t1, t2);
    printf("Time: %.2fs\n", dt);
    printf("done.\n");
    for (int x = 0; x < 1024; x++) {
        printf("%d\n", array[x]);
    }
    Sleep(1000);
}
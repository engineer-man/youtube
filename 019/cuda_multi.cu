#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define BLOCKS 65535

__global__ void kernel(int *num1, int *num2, int *result) {
    result[blockIdx.x] = num1[blockIdx.x] + num2[blockIdx.x];
}

int main(void) {
    srand(time(NULL));
    int size = sizeof(int) * BLOCKS;

    // host copies
    int *num1, *num2, *result;

    // allocate space on host
    num1 = (int *) malloc(size);
    num2 = (int *) malloc(size);
    result = (int *) malloc(size);

    // device copies
    int *p_num1, *p_num2, *p_result;

    // allocate space on device
    cudaMalloc(&p_num1, size);
    cudaMalloc(&p_num2, size);
    cudaMalloc(&p_result, size);

    // pick numbers to add
    int i;
    for (i = 0; i < BLOCKS; ++i) {
        num1[i] = rand() % 100;
        num2[i] = rand() % 100;
    }

    // copy to device
    cudaMemcpy(p_num1, num1, size, cudaMemcpyHostToDevice);
    cudaMemcpy(p_num2, num2, size, cudaMemcpyHostToDevice);

    // start
    kernel<<<BLOCKS,1>>>(p_num1, p_num2, p_result);

    // copy from device
    cudaMemcpy(result, p_result, size, cudaMemcpyDeviceToHost);

    // print results
    for (i = 0; i < BLOCKS; ++i) {
        printf("%d\n", result[i]);
    }
}

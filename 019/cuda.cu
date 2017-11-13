#include <stdio.h>

__global__ void kernel(int *num1, int *num2, int *result) {
    *result = *num1 + *num2;
}

int main(void) {
    // host copies
    int num1, num2, result;

    // device copies
    int *p_num1, *p_num2, *p_result;

    // allocate space on device
    cudaMalloc(&p_num1, sizeof(int));
    cudaMalloc(&p_num2, sizeof(int));
    cudaMalloc(&p_result, sizeof(int));

    // pick numbers to add
    num1 = 4;
    num2 = 5;

    // copy to device
    cudaMemcpy(p_num1, &num1, sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(p_num2, &num2, sizeof(int), cudaMemcpyHostToDevice);

    // start
    kernel<<<1,1>>>(p_num1, p_num2, p_result);

    // copy from device
    cudaMemcpy(&result, p_result, sizeof(int), cudaMemcpyDeviceToHost);

    printf("%d\n", result);
}

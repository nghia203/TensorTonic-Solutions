#include <cuda_runtime.h>

__global__ void softmax_kernel(const float* input, float* output, int N) {
    // Write code here
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    extern __shared__ float shared_data[];

    if (blockIdx.x == 0 && threadIdx.x == 0) {
        // Find maximum value
        float max_val = input[0];
        for (int j = 1; j < N; ++j) {
            if (input[j] > max_val) max_val = input[j];
        }
        
        // Compute sum of exponentials
        float sum = 0.0f;
        for (int j = 0; j < N; ++j) {
            sum += expf(input[j] - max_val);
        }
        
        // Write out normalized probabilities
        for (int j = 0; j < N; ++j) {
            output[j] = expf(input[j] - max_val) / sum;
        }
    }
}

extern "C" void solve(const float* input, float* output, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    softmax_kernel<<<blocks, threads>>>(input, output, N);
    cudaDeviceSynchronize();
}
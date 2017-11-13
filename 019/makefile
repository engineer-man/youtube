all: clean
	gcc cpu_bench.c -o cpu_bench -lm -lpthread
	nvcc cuda.cu -o cuda
	nvcc cuda_multi.cu -o cuda_multi

clean:
	rm -f cpu_bench
	rm -f cuda
	rm -f cuda_multi

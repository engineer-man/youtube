#include <stdio.h>
#include <unistd.h>
#include <sys/time.h>
#include <math.h>
#include <pthread.h>
#include <stdlib.h>

void *calc(void *num) {
    long long c = (double)*((long long int *)num);

    for (; c > 0; --c) {
        double wat = sqrt(c);
    }
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("provide number to square\n");
        return 1;
    }

    struct timeval t1, t2;
    double elapsed;

    long long int num = atoll(argv[1]);
    int cpus = sysconf(_SC_NPROCESSORS_ONLN);
    long long int per_iteration = num / cpus;

    printf("processing %lld square roots using %d cpus at %lld per cpu\n", num, cpus, per_iteration);

    gettimeofday(&t1, NULL);

    pthread_t thread;

    pthread_t *threads = malloc(sizeof(pthread_t) * cpus);

    int i;

    for (i = 0; i < cpus; ++i) {
        threads[i] = thread;
    }

    for (i = 0; i < cpus; ++i) {
        pthread_create(&threads[i], NULL, calc, &per_iteration);
    }

    for (i = 0; i < cpus; ++i) {
        pthread_join(threads[i], NULL);
    }

    gettimeofday(&t2, NULL);

    elapsed = (t2.tv_sec - t1.tv_sec) * 1000.0;
    elapsed += (t2.tv_usec - t1.tv_usec) / 1000.0;

    printf("op took: %fms\n", elapsed);

    return 0;
}

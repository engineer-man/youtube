#include <pthread.h>
#include <math.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

void *do_some_sweet_work(void *arg) {
    for (int i = 0; i < 10000000000; ++i) {
        double res = sqrt(i);
    }
}

int main(void) {
    long num_procs = sysconf(_SC_NPROCESSORS_ONLN) - 1;
    int i = 0;

    pthread_t *thread_group = malloc(sizeof(pthread_t) * num_procs);

    for (i = 0; i < num_procs; ++i) {
        pthread_create(&thread_group[i], NULL, do_some_sweet_work, NULL);
    }

    for (i = 0; i < num_procs; ++i) {
        pthread_join(thread_group[i], NULL);
    }

    return 0;
}

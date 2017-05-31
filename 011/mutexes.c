#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define CALCULATIONS 100000000
#define BATCH_SIZE   100000
#define MAX_CORES    12

long long calculations_left = CALCULATIONS;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
int total_batches = 0;

void *process_batch(void *arg) {
    long long i, start_point;

    for (;;) {
        // acquire lock
        //pthread_mutex_lock(&mutex);

        // check if all calculations have been accomplished, and return if so
        if (calculations_left <= 0) {
            //pthread_mutex_unlock(&mutex);
            return NULL;
        }

        // retrieve a batch
        start_point = calculations_left - BATCH_SIZE;
        calculations_left -= BATCH_SIZE;
        ++total_batches;

        printf("processing %lld to %lld\n", start_point, start_point + BATCH_SIZE);

        // release lock
        //pthread_mutex_unlock(&mutex);

        // process batch
        for (i = start_point; i < start_point + BATCH_SIZE; ++i) {
            sqrt(i);
        }
    }
}

int main(void) {
    int i = 0;

    // create a thread group the size of MAX_CORES
    pthread_t *thread_group = malloc(sizeof(pthread_t) * MAX_CORES);

    // start all threads to begin work
    for (i = 0; i < MAX_CORES; ++i) {
        pthread_create(&thread_group[i], NULL, process_batch, NULL);
    }

    // wait for all threads to finish
    for (i = 0; i < MAX_CORES; ++i) {
        pthread_join(thread_group[i], NULL);
    }

    printf("total batches: %d\n", total_batches);

    return EXIT_SUCCESS;
}

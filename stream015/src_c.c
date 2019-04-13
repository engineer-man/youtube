#include <stdlib.h>
#include <stdio.h>

void main(int argc, char **argv) {
    int start_num = atoi(argv[1]);
    int count = atoi(argv[2]);

    int *list = malloc(0);
    int list_len = 0;

    int i = 0;

    for (; i < count; ++i) {
        ++list_len;

        list = realloc(list, list_len * sizeof(int));
        list[list_len - 1] = i * start_num;
    }

    i = 0;

    int sum = 0;
    int divisible = 0;

    for (; i < list_len; ++i) {
        sum += list[i];
        if (list[i] % 10 == 0) {
            ++divisible;
        }
    }

    free(list);

    printf("%d %d", sum, divisible);
}

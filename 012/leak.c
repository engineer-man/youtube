#include <stdlib.h>

void make_leak(void) {
    char *never_gonna_free_me = malloc(4 * sizeof(char));
    // upon return, there is no way to access or free never_gonna_free_me
}

void make_dangling_pointer(void) {
    char *gonna_dangle = malloc(4 * sizeof(char));
}

int main(void) {
    make_leak();

    char *gonna_dangle = malloc(4 * sizeof(char));
    free(gonna_dangle);
    // gonna_dangle is now a dangling pointer
}

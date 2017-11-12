#include <stdio.h>

#include "functions.h"

int main(void) {
    // use function
    printf("%d\n", add(2, 6));

    // use macro
    printf("%d\n", ADD(3, 7));

    // use typedef
    person engineer_man;
    engineer_man.age = 32;
    printf("engineer man's age is: %d\n", engineer_man.age);
}

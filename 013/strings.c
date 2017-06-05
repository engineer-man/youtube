#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    // single character, integer type
    char letter = 'A'; // 65

    // string literal, stored as read-only data
    char *name1 = "Engineer Man";

    // character array initialized from string literal, copied to and stored on the stack
    char name2[] = "Engineer Man";

    // exact same as above
    char name3[] = { 'E', 'n', 'g', 'i', 'n', 'e', 'e', 'r', ' ', 'M', 'a', 'n', '\0'};

    // pointer to char, holds up to 128 elements, stored on the stack
    char name4[128];

    // copy string literal into name4, 12 bytes + 1 for null terminator
    strcpy(name4, "Engineer Man");
    printf("%s\n", name4); // Engineer Man
    strlen(name4); // 12

    // access elements -- arr[index] => *(arr + index)
    name4[0]; // E
    *(name4 + 0); // E
    0[name4]; // E
    *(0 + name4); // E

    // modify element
    name4[8] = '-';
    *(name4 + 8) = '-';
    8[name4] = '-';
    *(8 + name4) = '-';

    name4; // Engineer-Man

    // change boundary of string
    name4[8] = '\0';
    printf("%s\n", name4); // Engineer
    strlen(name4); // 8

    return EXIT_SUCCESS;
}

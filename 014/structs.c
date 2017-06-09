#include <stdlib.h>
#include <string.h>

typedef struct {
    int age;
    char *name;
} person;

int main(void) {
    // declare a new struct
    person em;

    // set some data
    em.age = 32;
    em.name = malloc(6 * sizeof(char));
    strcpy(em.name, "Brian");

    // create a pointer to struct
    person *em_ptr = &em;

    // set some data, again
    (*em_ptr).age = 33;
    (*em_ptr).name = realloc((*em_ptr).name, 7 * sizeof(char));
    strcpy((*em_ptr).name, "Brian!");

    // set some data, again, but with better syntax
    em_ptr->age = 34;
    em_ptr->name = realloc(em_ptr->name, 8 * sizeof(char));
    strcpy(em_ptr->name, "Brian!!");
}

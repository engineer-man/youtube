#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    // strings
    char *name = malloc(sizeof(char) * 3); // [][][]
    strcpy(name, "em"); // [e][m][\0]
    printf("%s\n", name);
    free(name);

    int name_len = 3;
    char **names = malloc(sizeof(char *) * name_len);

    for (int i = 0; i < name_len; ++i) {
        names[i] = malloc(sizeof(char) * 16);
    }

    strcpy(names[0], "em");
    strcpy(names[1], "duck");
    strcpy(names[2], "pizza");

    printf("%s, %s, %s\n", names[0], names[1], names[2]);

    for (int i = 0; i < name_len; ++i) {
        if (strcmp(names[i], "duck") == 0) {
            strcat(names[i], " is not cool");
        } else {
            strcat(names[i], " is cool");
        }
    }

    names = realloc(names, sizeof(char *) * (name_len + 1));
    names[3] = malloc(sizeof(char) * 16);

    strcpy(names[3], "rh");

    printf("%s, %s, %s, %s\n", names[0], names[1], names[2], names[3]);

    for (int i = 0; i < name_len; ++i) {
        free(names[i]);
    }

    free(names);

    // comparison
    printf("%d\n", strcmp("aaaza", "aaagb"));

    // integers
    int num = 1;
    int *nums = malloc(sizeof(int) * 2);

    nums[0] = 0;
    nums[1] = 1;

    printf("%d, %d\n", nums[0], nums[1]);

    // structs
    struct person {
        char name[16];
        int age;
    };

    // on stack
    struct person em;
    strcpy(em.name, "em");
    em.age = 27;

    printf("%s is %d years old\n", em.name, em.age);

    // on heap
    struct person *doge = malloc(sizeof(struct person) * 1);
    strcpy(doge->name, "doge");
    doge->age = 29;

    printf("%s is %d years old\n", doge->name, doge->age);
}

#include <stdio.h>

int main(void) {
    int authorized = 0;
    char sys_pass[16] = "secret!";
    char usr_pass[16];

    printf("enter password: ");
    scanf("%s", usr_pass);

    printf("usr_pass: %s\n", usr_pass);
    printf("sys_pass: %s\n", sys_pass);
    printf("auth val: %d\n", authorized);
    printf("usr_pass   addr: %p\n", (void *)usr_pass);
    printf("sys_pass   addr: %p\n", (void *)sys_pass);
    printf("authorized addr: %p\n", (void *)&authorized);

    if (strcmp(sys_pass, usr_pass) == 0) {
        authorized = 1;
    }

    if (authorized) {
        printf("password is correct!\n");
    }
}

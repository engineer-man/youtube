#include <unistd.h>

int main(void) {
    write(4, "hello\n", 6);
}

#include <iostream>

extern "C" {
    void hello(void);
    int sum(int, int);
}

void hello(void) {
    std::cout << "hello from cpp\n";
}

int sum(int a, int b) {
    return a + b;
}

int main(void) {
    return 0;
}

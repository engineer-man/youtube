#import

int foo() {
    int a = 3
    int b = 2
    return c + d;
}

int main (int argc, const char * argv[]) {
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];

    result = foo();

    [pool drain];

    return 0;
}

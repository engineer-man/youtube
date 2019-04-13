#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char **argv) {
    int start_num = atoi(argv[1]);
    int count = atoi(argv[2]);

    int list_len = 0;
    vector<int> list(0); // please use a list in this case kids.

    int i = 0;

    for (; i < count; ++i) {
        ++list_len;

        list.resize(list_len);
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

    cout << sum << " " << divisible;

    return 0;
}

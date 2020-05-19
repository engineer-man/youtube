#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char **argv) {
    int start_num = atoi(argv[1]);
    int count = atoi(argv[2]);

    vector<int> list;

    for (int i = 0; i < count; ++i) {
        list.push_back(i * start_num);
    }

    int sum = 0;
    int divisible = 0;

    for (auto i: list) {
        sum += i;
        if (i % 10 == 0) {
            ++divisible;
        }
    }

    cout << sum << " " << divisible;

    return 0;
}

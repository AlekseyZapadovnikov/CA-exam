#include <algorithm>
#include <ctime>
#include <iostream>

/*
    Compile: 
        g++ -std=c++17 -o branch_prediction_unsorted branch_prediction.cpp
        g++ -std=c++17 -DSORT_DATA -o branch_prediction_sorted branch_prediction.cpp

    Run:
        ./branch_prediction_unsorted
        ./branch_prediction_sorted
*/

int main() {
    // Generate data
    const unsigned arraySize = 32768;
    int data[arraySize];

    for (unsigned c = 0; c < arraySize; ++c)
        data[c] = std::rand() % 256;

    // Sort data if macro SORT_DATA defined
    #ifdef SORT_DATA
        std::sort(data, data + arraySize);
    #endif

    // Test
    clock_t start = clock();
    long long sum = 0;
    for (unsigned i = 0; i < 100000; ++i) {
        for (unsigned c = 0; c < arraySize; ++c) {   // Primary loop.
            if (data[c] >= 128)
                sum += data[c];
        }
    }

    double elapsedTime = static_cast<double>(clock()-start) / CLOCKS_PER_SEC;

    std::cout << "Elapsed time: " << elapsedTime << std::endl;
    std::cout << "Sum: " << sum << std::endl;
}

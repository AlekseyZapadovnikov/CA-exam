#include <stdio.h>
#include <pthread.h>

int x, y, a, b;

void* thread1(void* unused) {
    x = 1;
    a = y;
    return NULL;
}

void* thread2(void* unused) {
    y = 1;
    b = x;
    return NULL;
}

int main() {
    int i = 0;
    while (1) {
        x = 0;
        y = 0;
        a = 0;
        b = 0;

        pthread_t tid1;
        pthread_attr_t attr1;

        pthread_t tid2;
        pthread_attr_t attr2;

        pthread_attr_init(&attr1);
        pthread_attr_init(&attr2);

        pthread_create(&tid1, &attr1, thread1, NULL);
        pthread_create(&tid2, &attr2, thread2, NULL);

        pthread_join(tid1, NULL);
        pthread_join(tid2, NULL);

        i++;
        if(a == 0 && b == 0) {
            break;
        }
    }

    printf("Iterations: %d\n", i);
    return 0;
}

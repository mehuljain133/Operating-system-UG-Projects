//  Write a program to calculate sum of n numbers using thread library

#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

#define MAX 1000
int arr[MAX];
int sum = 0;
int n;

// Mutex to avoid race conditions
pthread_mutex_t lock;

// Thread function to compute partial sum
void* sum_array(void* arg) {
    int start = ((int*)arg)[0];
    int end = ((int*)arg)[1];

    int local_sum = 0;
    for (int i = start; i < end; i++) {
        local_sum += arr[i];
    }

    pthread_mutex_lock(&lock);
    sum += local_sum;
    pthread_mutex_unlock(&lock);

    pthread_exit(0);
}

int main() {
    int num_threads;

    printf("Enter number of elements: ");
    scanf("%d", &n);
    if (n > MAX) {
        printf("Max limit is %d\n", MAX);
        return 1;
    }

    printf("Enter %d integers:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter number of threads: ");
    scanf("%d", &num_threads);

    pthread_t threads[num_threads];
    int range[num_threads][2];
    int chunk_size = n / num_threads;
    int remaining = n % num_threads;

    pthread_mutex_init(&lock, NULL);

    for (int i = 0; i < num_threads; i++) {
        range[i][0] = i * chunk_size;
        range[i][1] = (i == num_threads - 1) ? (i + 1) * chunk_size + remaining : (i + 1) * chunk_size;
        pthread_create(&threads[i], NULL, sum_array, (void*)range[i]);
    }

    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&lock);

    printf("Total sum = %d\n", sum);

    return 0;
}

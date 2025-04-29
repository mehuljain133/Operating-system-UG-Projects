// Write a program to implement SRJF scheduling algorithm.

#include <stdio.h>

int main() {
    int n, i, smallest, time = 0, count = 0;
    int at[10], bt[10], rt[10], finish[10], wt[10], tat[10];
    float avg_wt = 0, avg_tat = 0;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++) {
        printf("Enter arrival time and burst time for P[%d]: ", i+1);
        scanf("%d%d", &at[i], &bt[i]);
        rt[i] = bt[i]; // Initialize remaining time
    }

    printf("\nProcess\tTurnaround Time\tWaiting Time\n");

    while(count != n) {
        smallest = -1;
        int min_rt = 9999;

        for(i = 0; i < n; i++) {
            if(at[i] <= time && rt[i] > 0 && rt[i] < min_rt) {
                min_rt = rt[i];
                smallest = i;
            }
        }

        if(smallest == -1) {
            time++;
            continue;
        }

        rt[smallest]--;
        time++;

        if(rt[smallest] == 0) {
            count++;
            finish[smallest] = time;
            tat[smallest] = finish[smallest] - at[smallest];
            wt[smallest] = tat[smallest] - bt[smallest];
            avg_wt += wt[smallest];
            avg_tat += tat[smallest];
            printf("P[%d]\t%d\t\t%d\n", smallest+1, tat[smallest], wt[smallest]);
        }
    }

    printf("\nAverage Waiting Time = %.2f\n", avg_wt/n);
    printf("Average Turnaround Time = %.2f\n", avg_tat/n);

    return 0;
}

// Write a program to implement non-preemptive priority based scheduling algorithm

#include <stdio.h>

int main() {
    int n, i, j;
    int bt[20], p[20], wt[20], tat[20], pr[20];
    float avg_wt = 0, avg_tat = 0;

    printf("Enter the number of processes: ");
    scanf("%d", &n);

    printf("Enter burst time and priority for each process:\n");
    for(i = 0; i < n; i++) {
        printf("P[%d] Burst Time: ", i + 1);
        scanf("%d", &bt[i]);
        printf("P[%d] Priority (lower number = higher priority): ", i + 1);
        scanf("%d", &pr[i]);
        p[i] = i + 1; // Process ID
    }

    // Sort processes based on priority
    for(i = 0; i < n - 1; i++) {
        for(j = i + 1; j < n; j++) {
            if(pr[i] > pr[j]) {
                // Swap priority
                int temp = pr[i];
                pr[i] = pr[j];
                pr[j] = temp;

                // Swap burst time
                temp = bt[i];
                bt[i] = bt[j];
                bt[j] = temp;

                // Swap process ID
                temp = p[i];
                p[i] = p[j];
                p[j] = temp;
            }
        }
    }

    wt[0] = 0; // First process waiting time is 0

    for(i = 1; i < n; i++) {
        wt[i] = 0;
        for(j = 0; j < i; j++)
            wt[i] += bt[j];
    }

    for(i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
        avg_wt += wt[i];
        avg_tat += tat[i];
    }

    printf("\nProcess\tPriority\tBurst Time\tWaiting Time\tTurnaround Time\n");
    for(i = 0; i < n; i++) {
        printf("P[%d]\t%d\t\t%d\t\t%d\t\t%d\n", p[i], pr[i], bt[i], wt[i], tat[i]);
    }

    printf("\nAverage Waiting Time = %.2f", avg_wt / n);
    printf("\nAverage Turnaround Time = %.2f\n", avg_tat / n);

    return 0;
}

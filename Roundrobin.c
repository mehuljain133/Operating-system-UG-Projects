// Write a program to implement Round Robin scheduling algorithm

#include <stdio.h>

int main() {
    int i, j, n, time, remain, flag = 0, tq;
    int wt = 0, tat = 0;
    int at[10], bt[10], rt[10]; // at: Arrival Time, bt: Burst Time, rt: Remaining Time

    printf("Enter number of processes: ");
    scanf("%d", &n);
    remain = n;

    printf("Enter arrival time and burst time for each process:\n");
    for(i = 0; i < n; i++) {
        printf("P[%d] Arrival Time: ", i + 1);
        scanf("%d", &at[i]);
        printf("P[%d] Burst Time: ", i + 1);
        scanf("%d", &bt[i]);
        rt[i] = bt[i]; // Remaining time initially equals burst time
    }

    printf("Enter time quantum: ");
    scanf("%d", &tq);

    printf("\nProcess\tTurnaround Time\tWaiting Time\n");

    for(time = 0, i = 0; remain != 0; ) {
        if(rt[i] <= tq && rt[i] > 0) {
            time += rt[i];
            rt[i] = 0;
            flag = 1;
        } else if(rt[i] > 0) {
            rt[i] -= tq;
            time += tq;
        }

        if(rt[i] == 0 && flag == 1) {
            remain--;
            printf("P[%d]\t%d\t\t%d\n", i + 1, time - at[i], time - at[i] - bt[i]);
            wt += time - at[i] - bt[i];
            tat += time - at[i];
            flag = 0;
        }

        if(i == n - 1)
            i = 0;
        else if(at[i + 1] <= time)
            i++;
        else
            i = 0;
    }

    printf("\nAverage Waiting Time = %.2f\n", (float)wt / n);
    printf("Average Turnaround Time = %.2f\n", (float)tat / n);

    return 0;
}

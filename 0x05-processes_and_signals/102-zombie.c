#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>


/**
 * infinite_while - creates infinite loop
 * Return: 0 always
 */
int infinite_while(void) {
    while (1) {
        sleep(1);
    }
    return 0;
}


/**
 * main - creates zombie process
 * Return: 0 always
 */
int main(void) {
    pid_t pid;
    int i;

    for (i = 0; i < 5; i++) {
        pid = fork();

        if (pid < 0) {
            perror("fork error");
            exit(EXIT_FAILURE);
        } else if (pid == 0) {
            // Child process
            printf("Zombie process created, PID: %d\n", getpid());
            exit(EXIT_SUCCESS);
        }
    }

    infinite_while();

    return 0;
}


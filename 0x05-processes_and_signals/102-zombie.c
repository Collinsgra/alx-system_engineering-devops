#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an loop
 * Return: 0 always
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates processes
 * Return: 0 always
 */
int main(void)
{
	int i;
	pid_t zm_process;

	for (i = 0; i < 5; i++)
	{
		zm_process = fork();
		if (!zm_process)
			return (0);
		printf("Zombie process created, PID: %d\n", zm_process);
	}

	infinite_while();
	return (0);
}

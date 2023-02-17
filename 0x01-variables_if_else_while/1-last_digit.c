#include <stdlib.h>
#include <time.h>
#include <stdio.h>

/**
 * main - The last digit
 *
 * Return: 0
 */
int main(void)
{
	int n;

	srand(time(0));
	n = rand() - RAND_MAX / 2;
	x = n % 10;
	printf("Lat digit of %d is %d", n, x);
	if (x > 5)
	{
		printf(" and is greater then 5");
	}
	if (x == 0)
	{
		printf(" and is 0");
	}
	if (x < 6 && x != 0)
	{
		printf(" and is than 6 and not 0");
	}
	printf("\n");
	return (0);
}

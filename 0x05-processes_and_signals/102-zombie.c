#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while -  neverending sleep
 * Return: 0
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
 * main - function that creates 5 zombie processes
 * Return: allways 0
 */

int main(void)
{
	int i;
	pid_t id;

	i = 0;
	while (i < 5)
	{
		id = fork();
		if (!id)
			return (0);
		printf("Zombie process created, PID: %d\n", id);
		i++;
	}

	infinite_while();
	return (0);
}

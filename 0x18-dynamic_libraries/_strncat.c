#include "main.h"

int _strlen(char *s);

/**
 * _strncat - appends src to the dest string.
 * @dest: string result
 * @src: string to copy
 * @n: numbers of characteres to copy
 * Return: a pointer to the resultant string dest
 */

char *_strncat(char *dest, char *src, int n)
{
	int i, j = 0;

	for (i = _strlen(dest); j <= (n - 1) && src[j] != '\0'; i++)
	{
		dest[i] = src[j];
		j++;
	}
	dest[i] = '\0';
	return (dest);
}

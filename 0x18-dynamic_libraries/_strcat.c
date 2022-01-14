#include "main.h"

char *_strcat(char *dest, char *src)
{
	int i, j = 0;

	for (i = _strlen(dest); src[j] != '\0'; i++)
	{
		dest[i] = src[j];
		j++;
	}
	dest[i] = '\0';
	return (dest);
}
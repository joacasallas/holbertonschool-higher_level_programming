#include "main.h"

/**
 * _strpbrk - finds the 1st character in s that matches any character in accept
 * @s: pointer to string to be scanned
 * @accept: string containing the characters to match
 * Return: a pointer to the character in s1
 * that matches one of the characters in s2, else returns NULL
 */

char *_strpbrk(char *s, char *accept)
{
	int i, j;

	for (i = 0; s[i] != '\0'; i++)
	{
		for (j = 0; accept[j] != '\0'; j++)
		{
			if (s[i] == accept[j])
			{
				return (s + i);
			}
		}
	}
	return (0);
}
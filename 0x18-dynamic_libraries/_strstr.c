#include "main.h"

/**
 * _strstr -  finds the first occurrence of the substring needle
 * in the string haystack
 * @haystack: pointer to string to be scanned
 * @needle: pointer to substring to be searched
 * Return: pointer to the first occurrence in haystack
 * return a null pointer if the sequence is not present
 */

char *_strstr(char *haystack, char *needle)
{
	unsigned int i = 0, j = 0;

	while (haystack[i])
	{
		while (needle[j] && (haystack[i] == needle[0]))
		{
			if (haystack[i + j] == needle[j])
			{
				j++;
			}
			else
			{
				break;
			}
		}
		if (needle[j] != '\0')
		{
			i++;
			j = 0;
		}
		else
		{
			return  (haystack + i);
		}
	}
	return (0);
}
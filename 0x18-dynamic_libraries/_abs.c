#include "main.h"
#include <stdio.h>

/**
 * _abs - computes the absolute value of an integer.
 * @num: number
 * Return: absolut value
 */

int _abs(int num)
{
	if (num < 0)
	{
		num = num * -1;
	}
	return (num);
}
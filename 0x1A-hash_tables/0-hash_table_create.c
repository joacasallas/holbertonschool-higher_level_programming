#include "hash_tables.h"

/**
 * hash_table_create - function that creates a hash table.
 * @size: size of the array
 * Return: a pointer to the newly created hash table
 * otherwise return NULL
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *ht;

	ht = malloc(sizeof(hash_table_t) * size);
	if (ht == NULL)
	{
		free (ht);
		return (NULL);
	}
	if (size == 0)
	{
		free (ht);
		return (NULL);
	}
	else
	{
		return (ht);
	}
}

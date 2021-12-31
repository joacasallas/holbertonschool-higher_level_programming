#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list pointer
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *list_temp = list;

	while (list->next != NULL)
	{
		list = list->next;
		if (list->next == list_temp)
		{
			return (1);
		}
	}
	return (0);
}

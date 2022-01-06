#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = *head;

	if (new != NULL)
	{
		while (new->next != NULL)
		{
			new = new->next;
		}
		new->n = number;
	}
	return (*head);
}

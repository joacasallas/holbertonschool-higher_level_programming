#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: pointer to linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;

	if (temp != NULL)
	{
		while (temp->next != NULL)
		{
			temp = temp->next;
		}
	}
	if (temp->n == (*head)->n)
	{
		return (1);
	}
	return (0);
}

#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if linked list is palindrome
 * @head: is the first node of the linked list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *first = *head, *last = *head, *prev;
	int len = 1, i = 0;

	if (*head == NULL)
		return (1);
	while (last->next != NULL)
	{
		len++;
		last = last->next;
	}
	while (i < len)
	{
		if (first->n != last->n)
			return (0);
		if (first->next == last || first == last)
			break;
		first = first->next;
		prev = *head;
		while (prev->next != last)
			prev = prev->next;
		last = prev;
		i++;
	}
	return (1);
}

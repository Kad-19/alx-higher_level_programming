#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if there is a cycle in the list
 * @list: the pointer to the first node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr = list;
	listint_t *node;

	while (curr != NULL)
	{
		node = curr->next;
		if (node >= curr)
		{
			return (1);
		}
		curr = node;
	}
	return (0);
}

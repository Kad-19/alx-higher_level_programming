#include <stdio.h>
#include "lists.h"
/**
 * insert_nodeint_at_index - inserts a node at the specified index
 * @idx: location of the required node on the list
 * @head: the pointer to the first node
 * @n: the data of the new node to be inserted
 * Return: a pointer to the node inserted
 */
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	unsigned int nodenum = 0;
	listint_t *curr = *head;
	listint_t *new;
	listint_t *next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (idx == 0)
	{
		new->n = n;
		new->next = *head;
		*head = new;
		return (new);
	}
	while (curr != NULL)
	{
		if (idx == nodenum + 1)
			break;
		curr = curr->next;
		nodenum++;
	}
	next = curr->next;
	new->n = n;
	new->next = next;
	curr->next = new;

	return (new);
}

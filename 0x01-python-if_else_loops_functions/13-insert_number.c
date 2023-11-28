#include "lists.h"
/**
 * insert_node - inserts a node at the correct place in a sorted list
 * @head: the pointer to the first node
 * @number: the data of the new node to be inserted
 * Return: a pointer to the node inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *new;
	listint_t *temp = curr->next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (temp != NULL)
	{
		if (curr->n >= number || temp->n >= number)
		{
			if (curr == *head)
			{
				new->next = curr->next;
				*head = new;
				break;
			}
			else if (temp->n >= number)
			{
				new->next = temp;
				curr->next = new;
				break;
			}
		}
		temp = temp->next;
		curr = curr->next;
	}
	if (temp == NULL)
	{
		new->next = NULL;
		curr->next = new;
	}

	return (new);
}

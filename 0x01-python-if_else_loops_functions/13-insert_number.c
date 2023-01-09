#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: a pointer to a pointer to the head of the list
 * @number: the number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *curr;

	new = malloc(sizeof(*new));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	curr = *head;
	if (number < curr->n)
	{
		new->next = curr;
		*head = new;
		return (new);
	}

	while (curr->next != NULL && number > curr->next->n)
		curr = curr->next;
	new->next = curr->next;
	curr->next = new;

	return (new);
}

#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle
 * @list: pointer to beginning of node
 *
 * Return: 0 if cycle is not present, 1 if it is
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next; /* move one node at a time */
		fast = fast->next->next; /* move two nodes at a time */
		if (slow == fast) /* if cycle exists */
		{
			return (1);
		}
	}
	return (0);
}

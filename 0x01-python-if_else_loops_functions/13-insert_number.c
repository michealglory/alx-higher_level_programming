#include "lists.h"

/**
 * insert_node - Insert a node into a sorted singly-linked list
 *
 * @head: A pointer to a pointer to the head of the list
 * @number: The integer value to insert into the list
 *
 * Return: A pointer to the newly inserted node, or NULL on failure
 *
 * Description:
 * This function inserts a new node with the specified integer value 'number'
 * into a sorted singly-linked list while maintaining the list's ascending
 * order.
 * It takes a pointer to a pointer to the head of the list ('head') and the
 * value to insert ('number').
 *
 * Usage:
 * - To insert a new node into the list, call this function with a pointer to
 * the pointer to the head of the list and the integer value to insert.
 * - The function will dynamically allocate memory for the new node and set
 * its 'n' member to the specified 'number'.
 * - It then inserts the new node into the list at the appropriate position to
 *   maintain ascending order.
 *
 * Example:
 *   listint_t *head = NULL;
 *
 *   insert_node(&head, 42);
 *   insert_node(&head, 10);
 *   insert_node(&head, 30);
 *
 *   // The list now contains: 10 -> 30 -> 42
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;

	if (node == NULL || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}

	while (node && node->next && node->next->n < number)
	{
		node = node->next;
	}

	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}


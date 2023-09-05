#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - A singly-linked list structure for integers
 *
 * @n: The integer data stored in the node
 * @next: A pointer to the next node in the list
 *
 * Description:
 * This structure represents a node in a singly-linked list that holds integer
 * values. It consists of an integer field 'n' to store the data and a pointer
 * 'next' that points to the next node in the list.
 *
 * Usage:
 * - To create new node, allocate memory for 'listint_t' & set 'n' and 'next'
 *   accordingly.
 * - To traverse list, start at the head node & follow the 'next' pointers
 *   until 'next' is NULL.
 * - To access the integer value in a node, use the 'n' member.
 *
 * Example:
 *   listint_t *head = NULL;
 *   listint_t *new_node = malloc(sizeof(listint_t));
 *
 *   if (new_node == NULL)
 *   {
 *       perror("Unable to allocate memory for new node");
 *       exit(EXIT_FAILURE);
 *   }
 *
 *   new_node->n = 42;
 *   new_node->next = NULL;
 *
 *   head = new_node; // The new node is now the head of the list
 */
typedef struct listint_s
{
	int n;                /* The integer data stored in the node */
	struct listint_s *next; /* A pointer to the next node in the list */
} listint_t;


size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

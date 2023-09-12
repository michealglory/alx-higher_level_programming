#include "lists.h"

/**
 * reverse_listint - Reverses a singly linked list in-place.
 *
 * This function takes a pointer to the head of a singly linked list
 * and reverses the order of its nodes in place. It uses three pointers
 * (prev, current, and next) to reverse the list while preserving the
 * connections between nodes.
 *
 * @head: A pointer to a pointer to the head of the linked list.
 *        Upon completion, this pointer will be updated to point to
 *        the new head of the reversed list.
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * This function takes a pointer to the head of a singly linked list and
 * determines whether the linked list is a palindrome. It uses a slow and
 * fast pointer technique to find the middle of the list and reverse the
 * second half. Then, it compares the reversed second half with the first
 * half to check for palindromic properties.
 *
 * @head: A pointer to a pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast = *head, *temp = *head, *middle = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			middle = slow_ptr->next;
			break;
		}
		if (!fast->next)
		{
			middle = slow_ptr->next->next;
			break;
		}
		slow_ptr = slow_ptr->next;
	}

	reverse_listint(&middle);

	while (middle && temp)
	{
		if (temp->n == middle->n)
		{
			middle = middle->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!middle)
		return (1);

	return (0);
}

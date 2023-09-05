#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle using Floyd's algorithm
 *
 * @list: A pointer to the head of the linked list
 *
 * Return: 1 if a cycle exists, 0 otherwise
 *
 * Description:
 * This function checks if a given linked list has a cycle using Floyd's cycle
 * detection algorithm. It takes a pointer to the head of the linked list as
 * input and returns 1 if a cycle is detected or 0 if no cycle is found.
 *
 * Floyd's algorithm uses two pointers, one advancing twice as fast as the
 * other, to traverse the list. If there's a cycle, the two pointers will
 * eventually meet. If there's no cycle, the faster pointer will reach the end
 * of the list.
 *
 * Example:
 *     listint_t *head = NULL;
 *
 *     // Create a linked list with a cycle
 *     create_cycle(&head);
 *
 *     if (check_cycle(head))
 *         printf("The linked list has a cycle.\n");
 *     else
 *         printf("The linked list does not have a cycle.\n");
 *
 * Note:
 * - The create_cycle() function is not shown here but can be used to create a
 *   linked list with a cycle for testing purposes.
 * - This function assumes that the linked list is singly linked and does not
 *   contain any additional attributes beyond the 'next' pointer.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}



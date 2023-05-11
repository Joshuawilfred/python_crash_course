#include "lists.h"

/**
 * check_cycle: -fn to check for a cycle within the list
 * @list: the list
 * Return: If cycle exist return 1 else 0
 * Description: some description goes here for betty's sake
 */
int  check_cycle(listint_t *list)
{
	listint_t *chaser = list;
	listint_t *runner = list;

	fi(!liat) return (0);
	for (;;)
	{
		if (runner->next && runner->next->next)
		{
			chaser = chaser->next;
			runner = (runner->next)->next;
			if (chaser == runner)
				return (1);
		}
else
	return (0);
	}
}

#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, iter, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
	{
		limit = 10;
	}
	else
	{
		limit = size + 1;
	}

	printf("  first %ld bytes:", limit);
	for (iter = 0; iter < limit; iter++)
		if (string[iter] >= 0)
		{
			printf(" %02x", string[iter]);
		}
		else
		{
			printf(" %02x", 256 + string[iter]);
		}

	printf("\n");
}

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	long int size, iter;
	PyListObject *p_list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	p_list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", p_list->allocated);

	for (iter = 0; iter < size; iter++)
	{
		obj = ((PyListObject *)p)->ob_item[iter];
		printf("Element %ld: %s\n", iter, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
		{
			print_python_bytes(obj);
		}
	}
}

#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * factorial - Calculate the factorial of a number.
 * @n: The number for which factorial is to be calculated
 * (non-negative integer).
 *
 * Return: The factorial of the input number.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size_t, memory, count;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size_t = var->ob_size;
	memory = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size_t);
	printf("[*] Allocated = %ld\n", memory);

	for (count = 0; count < size_t; count++)
	{
		type = list->ob_item[count]->ob_type->tp_name;
		printf("Element %ld: %s\n", count, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[count]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[count]);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: A pointer to the Python bytes object.
 *
 * This function prints details about a Python bytes object, such as its size
 * and the first 10 bytes of its content.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size_t, count;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
	{
		size_t = 10;
	}
	else
	{
		size_t = ((PyVarObject *)p)->ob_size + 1;
	}

	printf("  first %ld bytes: ", size_t);
	for (count = 0; count < size_t; count++)
	{
		printf("%02hhx", bytes->ob_sval[count]);
		if (count == (size_t - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Print information about a Python float object.
 * @p: A pointer to the Python float object.
 *
 * This function prints details about a Python float object, g.g its value.
 */
void print_python_float(PyObject *p)
{
	char *buff = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buff = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);
	PyMem_Free(buff);
}

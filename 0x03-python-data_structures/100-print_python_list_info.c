#include <object.h>
#include <listobject.h>
#include <Python.h>

/**
 * print_python_list_info - function that prints some basic
 * info about Python lists
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
	int elem;

	print("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	print("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elem = 0; elem <Py_SIZE(p); elem++)
		print("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);
}

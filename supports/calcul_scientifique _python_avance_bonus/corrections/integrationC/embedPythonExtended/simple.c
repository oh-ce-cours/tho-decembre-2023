#include <Python.h>
static int numargs = 0;

/* Return the number of arguments of the application command line */
static PyObject *
emb_numargs(PyObject *self, PyObject *args)
{
	puts("in emb_numargs \n");
	if (!PyArg_ParseTuple(args, ":numargs"))
		return NULL;
	return PyLong_FromLong(numargs);
}

static PyMethodDef EmbMethods[] = {
	{"numargs", emb_numargs, METH_VARARGS,
	 "Return the number of arguments received by the process."},
	{NULL, NULL, 0, NULL}};

static PyModuleDef EmbModule = {
	PyModuleDef_HEAD_INIT, "emb", NULL, -1, EmbMethods,
	NULL, NULL, NULL, NULL};

static PyObject *
PyInit_emb(void)
{
	puts("in PyInit \n");
	return PyModule_Create(&EmbModule);
}

int main(int argc, char *argv[])
{
	const char *python_file = "test_emb.py";
	wchar_t *program = Py_DecodeLocale(argv[0], NULL);
	if (program == NULL)
	{
		fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
		exit(1);
	}
	Py_SetProgramName(program); /* optional but recommended */

	numargs = argc;
	PyImport_AppendInittab("emb", &PyInit_emb);
	Py_Initialize();
	PyRun_SimpleString("import sys, os; sys.path.append(os.getcwd())");

	//Run a simple file
	if (1)
	{
		FILE *PScriptFile = fopen(python_file, "r");
		if (PScriptFile)
		{
			puts("Python file found!!\n");
			int a = PyRun_SimpleFile(PScriptFile, python_file);
			printf("run it as %d\n", a);
			fclose(PScriptFile);
		}
		else
		{
			puts("Python file not found !!\n");
		}
		return Py_FinalizeEx();
	}
	else
	{
		PyRun_SimpleString("import emb as em\n"
						   "print(f'{em.numargs()}')\n");
		if (Py_FinalizeEx() < 0)
		{
			exit(120);
		}
		PyMem_RawFree(program);
	}
}
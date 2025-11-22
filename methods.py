import io
import contextlib

def get_function(input):
    f = io.StringIO()
    namespace = {}
    with contextlib.redirect_stdout(f):
                exec(input, namespace)  # define functions, variables, etc.
    result = None

    # Find all functions in the namespace
    functions = [obj for obj in namespace.values() if callable(obj)]

    if functions:
        # Call the last function defined
        result = functions[-1]()
    return result

def execute_function(code):
    f = io.StringIO()
    output = f.getvalue().strip()
    return output

def test_case(code, expected):
    expected = str(expected)
    return execute_function(code) == expected
import io
import contextlib

def execute_code(code):
    """
    Execute Python code and capture both printed output and return values.
    Returns a tuple of (result, output_string)
    """
    f = io.StringIO()
    namespace = {}
    result = None
    
    # Capture stdout while executing the code
    with contextlib.redirect_stdout(f):
        exec(code, namespace)
    
    # Get captured output
    output = f.getvalue()
    
    # Find and call the last function defined
    functions = [obj for obj in namespace.values() if callable(obj)]
    if functions:
        # Call the last function and capture its return value
        f2 = io.StringIO()
        with contextlib.redirect_stdout(f2):
            result = functions[-1]()
        output += f2.getvalue()
    
    return result, output

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
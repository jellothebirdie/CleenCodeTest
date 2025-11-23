import io
import contextlib
from problems import problems

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

def test_case(code, expected):
    return str(execute_code(code)[0]) == str(expected)

def load_user_function(code):
    namespace = {}
    exec(code, namespace)
    functions = [obj for obj in namespace.values() if callable(obj)]
    return functions[-1] if functions else None

def run_test(func, test):
    # Extract args from JSON into function call
    inputs = test["input"]

    # If input is a dict, pass via **kwargs
    result = func(**inputs)
    
    return result == test["output"], result

def get_problem(problem_name):
    try:
        return problems[problem_name]
    except:
        print("Problem not found")
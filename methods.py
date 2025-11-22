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

problems = {
            "Two Sum": {"problem_name":"Two Sum", 
                        "function_header": """def TwoSum(List[int], target: int) -> List[int]:""", 
                        "incorrect_code":"""def (nums: List[int], target: int) -> List[int]:
                                                    for i in range(len(nums)):
                                                        for j in range(len(nums)):
                                                            if nums[i] + nums[j] == target:
                                                                return [i, j]"""},
            "Palindrome": {"problem_name": "Palindrome", 
                           "function_header": """def isPalindrome(s: str) -> bool""", \
                            "incorrect_code":"""def isPalindrome(s: str) -> bool:
                                                        s = s.lower()
                                                        filtered = ''.join(c for c in s if c.isalpha())
                                                        return filtered == filtered[::-1]"""},
            "Remove Node": {"problem_name":"Remove Node",
                            "function_header": """def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:""", 
                            "incorrect_code":"""def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
                                                        length = 0
                                                        current = head
                                                        while current:
                                                            length += 1
                                                            current = current.next
                                                        current = head
                                                        for _ in range(length - n - 1):
                                                            current = current.next
                                                        current.next = current.next.next
                                                        return head"""}
            }

def get_problem(problem_name):
    try:
        return problems[problem_name]
    except:
        print("Problem not found")
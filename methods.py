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


def test_case(code, expected):
    return str(execute_code(code)[0]) == str(expected)

problems = {
            "Two Sum": {"level":1,
                        "problem_name":"Two Sum", 
                        "function_header": """def TwoSum(List[int], target: int) -> List[int]:""", 
                        "incorrect_code":
"""
def (nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]""",
                        "description":   
"""
Given an array of integers nums and an integer target, return the 
indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices 
i and j that satisfy the condition.

Return the answer with the smaller index first.
""",
            "examples":
"""
Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
""",
"tests": """
[
    {
      "input": {
        "nums": [2, 7, 11, 15],
        "target": 9
      },
      "output": [0, 1]
    },
    {
      "input": {
        "nums": [3, 2, 4],
        "target": 6
      },
      "output": [1, 2]
    }
]
"""},


            "Palindrome": {"problem_name": "Palindrome", 
                           "function_header": "def isPalindrome(s: str) -> bool", \
                           "incorrect_code": 
"""
def isPalindrome(s: str) -> bool:
    s = s.lower()
    filtered = ''.join(c for c in s if c.isalpha())
    return filtered == filtered[::-1]""",
                           "description":
"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
""",
            "examples":
"""
Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.
""",
"tests":
[
    {
      "input": { "s": "A man, a plan, a canal: Panama" },
      "output": True,
    },
    {
      "input": { "s": "race a car" },
      "output": False,
    },
    {
      "input": { "s": "" },
      "output": True,
    },
    {
      "input": { "s": " " },
      "output": True,
    },
    {
      "input": { "s": "0P" },
      "output": False,
    },
    {
      "input": { "s": "abba" },
      "output": True,
    },
    {
      "input": { "s": "abcba" },
      "output": True,
    },
    {
      "input": { "s": "No 'x' in Nixon" },
      "output": True,
    },
    {
      "input": { "s": ".,," },
      "output": True,
    },
    {
      "input": { "s": "a." },
      "output": True,
    },
    {
      "input": { "s": "Àbbà" },
      "output": False,
    },
    {
      "input": { "s": "åböbå" },
      "output": True,
    },
    {
      "input": { "s": "123321" },
      "output": True,
    },
    {
      "input": { "s": "123421" },
      "output": False,
    },
    {
      "input": { "s": "Able was I ere I saw Elba" },
      "output": True,
    }
  ]
},


            "Remove Node": {"problem_name":"Remove Node",
                            "function_header": "def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:", 
                            "incorrect_code":             
"""
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    current = head
    for _ in range(length - n - 1):
        current = current.next
    current.next = current.next.next
    return head""",
                            "description":
"""
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.
""",
            "examples":
            """
Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []
Example 3:

Input: head = [1,2], n = 2

Output: [2]
"""}
}

def get_problem(problem_name):
    try:
        return problems[problem_name]
    except:
        print("Problem not found")
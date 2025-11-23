problems = {
            "Two Sum": {"level":1,
                        "problem_name":"Two Sum", 
                        "function_header": """def TwoSum(List[int], target: int) -> List[int]:""", 
                        "incorrect_code":
"""
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
""",
                        "description":   
"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

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
"tests":
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
},


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


            "Rain Water": {"problem_name":"Rain Water",
                           "function_header": "def trap(self, height: List[int]) -> int:", 
                           "incorrect_code":             
"""
def trap(height):
    water = 0
    max_left = 0
    for i in range(len(height)):
        if height[i] > max_left:
            max_left = height[i]
        water += max_left - height[i]  # ignores right boundary
    return water""",
                            "description":
"""
You are given an array of non-negative integers height which represent an elevation map. 
Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
""",
            "examples":
            """
Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
""",
            "tests":
[
    {
      "input": { "height": [0,1,0,2,1,0,1,3,2,1,2,1] },
      "output": 6,
      "description": "classic example with multiple pits"
    },
    {
      "input": { "height": [] },
      "output": 0,
      "description": "empty array, no water trapped"
    },
    {
      "input": { "height": [0,0,0,0] },
      "output": 0,
      "description": "all zeros, no water trapped"
    },
    {
      "input": { "height": [1,2,3,4,5] },
      "output": 0,
      "description": "strictly increasing heights"
    },
    {
      "input": { "height": [5,4,3,2,1] },
      "output": 0,
      "description": "strictly decreasing heights"
    },
    {
      "input": { "height": [2,0,2] },
      "output": 2,
      "description": "single pit"
    },
    {
      "input": { "height": [3,0,1,3,0,5] },
      "output": 8,
      "description": "multiple pits of different heights"
    },
    {
      "input": { "height": [4,2,0,3,2,5] },
      "output": 9,
      "description": "complex pit arrangement"
    },
    {
      "input": { "height": [1,0,2,1,0,1,3] },
      "output": 5,
      "description": "nested pits"
    },
    {
      "input": { "height": [1] },
      "output": 0,
      "description": "single bar, no water trapped"
    },
    {
      "input": { "height": [1,2] },
      "output": 0,
      "description": "two bars, no water trapped"
    },
    {
      "input": { "height": [2,1,2] },
      "output": 1,
      "description": "small pit between two higher bars"
    }
  ]}
}
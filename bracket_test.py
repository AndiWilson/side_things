import unittest

def check_brackets(string):
    stack = []
    bracket_map = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in bracket_map.keys():
            stack.append(char)
        elif char in bracket_map.values():
            if not stack or bracket_map[stack.pop()] != char:
                return False
    
    return len(stack) == 0

class TestBracketMatching(unittest.TestCase):
    
    def test_correct_matching(self):
        self.assertTrue(check_brackets("()"))
        self.assertTrue(check_brackets("[()]{}"))
        self.assertTrue(check_brackets("({[]})"))
        self.assertTrue(check_brackets(""))

def test_incorrect_matching(self):
        self.assertFalse(check_brackets("))"))
        self.assertFalse(check_brackets(")"))
        self.assertFalse(check_brackets("()}"))
        self.assertFalse(check_brackets("["))
        self.assertFalse(check_brackets("[]]"))
        self.assertFalse(check_brackets("{[}]"))

if __name__ == '__main__':
    unittest.main()
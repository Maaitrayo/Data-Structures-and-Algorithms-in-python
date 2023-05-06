from collections import deque
stack = deque()

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

    # problem statement 1
    def reverse_string(self, str_val):
        for val in str_val:
            self.push(val)
        
        rev_str = ''
        for i in range(self.size()):
            char = self.pop()
            rev_str += char
        return rev_str

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(statement):
    stack = Stack()
    for char in statement:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        
        if char == ')' or char == '}' or char == ']':
            if stack.size() == 0:
                return False
            if not is_match(char, stack.pop()):
                return False

def test_case_2():
    s = Stack()
    print(s.is_balanced("({a+b})"))     
    print(s.is_balanced("))((a+b}{"))   
    print(s.is_balanced("((a+b))"))     
    print(s.is_balanced("))"))          
    print(s.is_balanced("[a+b]*(x+2y)*{gg+kk}")) 

if __name__ == '__main__':
    s = Stack()
    _input = "We will conquere COVID-19"
    reversed_String = s.reverse_string(_input)
    # print(reversed_String)
    test_case_2()
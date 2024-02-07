#create a class for stack
class Stack:
    def __init__(self, size):
        #properties of stack
        self.size = size
        self.stack = [None] * size
        self.top = 0

    #checking whether stack is empty
    def is_empty(self):
        if self.top == 0:
            return True
        else:
            return False

    #pushing elements to stack
    #in stack last come first out rule is used
    def push(self, x):
        if self.top == self.size:
            raise OverflowError("Stack overflow")
        else:
            self.top += 1
            self.stack[self.top] = x

    #pop operation, removing last or the top element from stack
    def pop(self):
        if self.is_empty():
            raise OverflowError("Stack underflow")
        else:
            self.top -= 1
            return self.stack[self.top + 1]

#sample operation of every operation of functions
stack_size = 5
my_stack = Stack(stack_size)

print("Is the stack empty before pushing elements?", my_stack.is_empty())  # this should be True

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(50)

print("Is the stack empty after pushing elements?", my_stack.is_empty())  # this should be False

print("Popped element:", my_stack.pop())  #  print 30
print("Popped element:", my_stack.pop())  #  print 20
print("Popped element:", my_stack.pop())  #  print 10

print("Is the stack empty after poping elements?", my_stack.is_empty())  # this should be True

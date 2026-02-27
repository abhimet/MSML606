import csv
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HomeWork2:

    # Problem 1: Construct an expression tree (Binary Tree) from a postfix expression
    # input -> list of strings (e.g., [3,4,+,2,*])
    # this is parsed from p1_construct_tree.csv (check it out for clarification)

    # there are no duplicate numeric values in the input
    # support basic operators: +, -, *, /

    # output -> the root node of the expression tree. Here: [*,+,2,3,4,None,None]
    # Tree Node with * as root node, the tree should be as follows
    #         *
    #        / \
    #       +   2
    #      / \
    #     3   4

    def constructBinaryTree(self, input) -> TreeNode:
        node_list = [] #making a list to store all the nodes from input
        for element in input: # iterating through my input 
            if element not in ['+', '-', '*', '/']:
                node_list.append(TreeNode(element))
            else:
                right_child = node_list.pop() #popping last node in list to be right child 
                left_child = node_list.pop() #popping the one before that last one to be left child
                
                #need to make a node in the tree for the actual operator
                operator_node = TreeNode(element)
                #make left child this operator's left child
                operator_node.left = left_child
                #make right child this operator's right child
                operator_node.right = right_child
                
                node_list.append(operator_node) #push to list
        #get root of the tree
        return node_list[0]
        
      
                
    # Problem 2.1: Use pre-order traversal (root, left, right) to generate prefix notation
    # return an array of elements of a prefix expression
    # expected output for the tree from problem 1 is [*,+,3,4,2]
    # you can see the examples in p2_traversals.csv

    def prefixNotationPrint(self, head: TreeNode) -> list:
        #checking if no node, then giving out nothing
        if head is None:
            return []
        final_result = [head.val] #setting up the list with value at root
        left = self.prefixNotationPrint(head.left)#going from root to left child immediately
        for vals in left:
            final_result.append(vals) #adding left side to list
        right = self.prefixNotationPrint(head.right)
        for vals in right:
            final_result.append(vals) #adding right 
        return final_result #returning list w all combined
    # Problem 2.2: Use in-order traversal (left, root, right) for infix notation with appropriate parentheses.
    # return an array of elements of an infix expression
    # expected output for the tree from problem 1 is [(,(,3,+,4,),*,2,)]
    # you can see the examples in p2_traversals.csv

    # don't forget to add parentheses to maintain correct sequence
    # even the outermost expression should be wrapped
    # treat parentheses as individual elements in the returned list (see output)

    def infixNotationPrint(self, head: TreeNode) -> list:
        #no node, giving out nothing, empty list
        if head is None:
            return [] 
  
        #checking if number at given node
        if head.left is None and head.right is None:
            return [head.val] #give number directly
        final_result = ['('] #starting with parentheses if child exists
        #getting all left vals
        left = self.infixNotationPrint(head.left)
        for vals in left:
            final_result.append(vals) 
        #going root next since in order
        final_result.append(head.val)
        
        #getting right values
        right = self.infixNotationPrint(head.right)
        for vals in right:
            final_result.append(vals)
        final_result.append(')') #adding closed parentheses
        return final_result #combined with everything 
    

    # Problem 2.3: Use post-order traversal (left, right, root) to generate postfix notation.
    # return an array of elements of a postfix expression
    # expected output for the tree from problem 1 is [3,4,+,2,*]
    # you can see the examples in p2_traversals.csv

    def postfixNotationPrint(self, head: TreeNode) -> list:
        if head is None: #checking if no node again, then return empty list
            return []
        final_result =[]
        #going left first for post order
        left = self.postfixNotationPrint(head.left)
        for vals in left:
            final_result.append(vals)
        #going right next
        right = self.postfixNotationPrint(head.right)
        for vals in right:
            final_result.append(vals)
        final_result.append(head.val) #getting to root last since post order
        return final_result #return combined
hw2 = HomeWork2()
empty_tree =None
case_1 = hw2.constructBinaryTree(["3", "4", "+", "2", "*"]) 
case_2 = hw2.constructBinaryTree(["5"])  

#testing prefix 
print(hw2.prefixNotationPrint(empty_tree))
print(hw2.prefixNotationPrint(case_1))
print(hw2.prefixNotationPrint(case_2))

#testing postfix
print(hw2.postfixNotationPrint(empty_tree))
print(hw2.postfixNotationPrint(case_1))

#testing infix
print(hw2.infixNotationPrint(empty_tree))
print(hw2.infixNotationPrint(case_1))
print(hw2.infixNotationPrint(case_2))

#all are working



class Stack:
    # Implement your stack using either an array or a list
    # (i.e., implement the functions based on the Stack ADT we covered in class)
    # You may use Python's list structure as the underlying storage.
    # While you can use .append() to add elements, please ensure the implementation strictly follows the logic we discussed in class
    # (e.g., manually managing the "top" of the stack
    
    # Use your own stack implementation to solve problem 3

    def __init__(self):
        # TODO: initialize the stack
        self.elements = []
        self.top = -1 #accessing top index of my stack
    
    def push(self, value): #pushing each element into my stack
        self.elements.append(value) #appending to stack
        self.top +=1 #move index to right so i can always get the last added value
    
    def pop(self):
        if self.top == -1:
            return None #there is nothing in the stack to even pop
        value = self.elements[self.top] #accessing top value currently
        self.elements.pop() #popping that top value
        self.top -= 1  #change top to index on left
        return value #return value  
    
    # Problem 3: Write code to evaluate a postfix expression using stack and return the integer value
    # Use stack which you implemented above for this problem

    # input -> a postfix expression string. E.g.: "5 1 2 + 4 * + 3 -"
    # see the examples of test entries in p3_eval_postfix.csv
    # output -> integer value after evaluating the string. Here: 14

    # integers are positive and negative
    # support basic operators: +, -, *, /
    # handle division by zero appropriately

    # DO NOT USE EVAL function for evaluating the expression

    def evaluatePostfix(s, exp: str) -> int: 
        # TODO: implement this using your Stack class
        sep_exp = exp.split() #splitting the expresison so each value has its own string
        stack = Stack() 
        for element in sep_exp: 
            if element not in ['+', '-', '*', '/']: #checking if any element is a number
                stack.push(int(element))
            else:
                last_no = stack.pop() #last #, on right
                second_last_no = stack.pop() #second to last #, on left
                if last_no is None or second_last_no is None:
                    raise ValueError("malformed") #malformed edge case
                if element == '+':
                    calculation = second_last_no + last_no #addition
                    stack.push(calculation)
                elif element == '-':
                    calculation = second_last_no - last_no #subtraction
                    stack.push(calculation)
                elif element == '*':
                    calculation = second_last_no * last_no #multiplication
                    stack.push(calculation)
                elif element == "/":
                    if last_no == 0:
                        raise ZeroDivisionError("error cant divide by zero") #zerodivisionerror
                    calculation = int((second_last_no)/(last_no)) #division
                    stack.push(calculation)
        return stack.pop() #returning whatever is left after all calculations
s = Stack()
print(s.evaluatePostfix("5 1 2 + 4 * + 3 -"))
#edge cases


# Main Function. Do not edit the code below
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)

        assert output == postfix, f"P1 Test {i} failed: tree structure incorrect"
        print(f"P1 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    with open('p2_traversals.csv', 'r') as f:
        testcases = list(csv.reader(f))

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)

        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"

        print(f"P2 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 3")
    testcases = []
    try:
        with open('p3_eval_postfix.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                testcases.append(row)
    except FileNotFoundError:
        print("p3_eval_postfix.csv not found")

    for idx, row in enumerate(testcases, start=1):
        expr, expected = row

        try:
            s = Stack()
            result = s.evaluatePostfix(expr)
            if expected == "DIVZERO":
                print(f"Test {idx} failed (expected division by zero)")
            else:
                expected = int(expected)
                assert result == expected, f"Test {idx} failed: {result} != {expected}"
                print(f"Test case {idx} passed")

        except ZeroDivisionError:
            assert expected == "DIVZERO", f"Test {idx} unexpected division by zero"
            print(f"Test case {idx} passed (division by zero handled)")
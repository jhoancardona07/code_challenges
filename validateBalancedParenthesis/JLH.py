class Solution:
  def isValid(self, string):
    stack=[]
    for character in string:
        if(character == "(" or character=="[" or character=="{"):
            stack.append(character)
        if(character == ")"):
            if(not(stack.pop()=="(")):
                stack.append("(")
        if(character == "]"):
            if(not(stack.pop()=="[")):
                stack.append("[")
        if(character == "}"):
            if(not(stack.pop()=="{")):
                stack.append("{")    
    if(len(stack)==0):
        return True
    else:
        return False

#TEST ZONE
s="((()))"
print(s, Solution().isValid(s))
s="[()]{}"
print(s, Solution().isValid(s))
s="({[)]"
print(s, Solution().isValid(s))
s=""
print(s, Solution().isValid(s))
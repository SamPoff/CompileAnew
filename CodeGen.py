'''
Created on Oct 12, 2018

@author: Harrison Fitch
@author: Samuel Poff
'''

"""
Code generator for Tramelblaze assembly. Utilizes nodes within the AST.
"""
import re

class CodeGen:
    
    def __init__(self):
        self.phrase = []
        self.variables = []
        self.mem_loc = 0
    def check_repeat(self, tok):
        # check to see if a variable is already used
        
        for item in self.variables:
            if(item[0] == tok.val):
                # Variable has already been mapped to memory location
                return item[1]
        
        # Add to the variable list, return the new location
        self.mem_loc = self.mem_loc + 1
        self.variables.append((tok.val,self.mem_loc))
        return self.mem_loc 
     
    def int_declare(self):
        mem = self.check_repeat(self.phrase[1])
        print(mem)
        print('LOAD\tR1, ',end='')
        if(len(self.phrase) > 3):
            if(self.phrase[3].val == ';'):
                print("R4");
            else:          
                print(hex(int(self.phrase[3].val))[2:].rjust(4, '0'));
        else:
            print('0000')
        print('STORE\tR1, ',hex(int(mem))[2:].rjust(4, '0'))
            
    def translate(self, rule, phrase):
        self.phrase = phrase
        print(len(self.phrase))
        assemble = {
            'INT_DECLARE': self.int_declare()
        }
        # Get the function from switcher dictionary
        func = assemble.get(rule, "Nothing")
        # Execute the function
        return func
   
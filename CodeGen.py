'''
Created on Oct 12, 2018

@author: Harrison Fitch
@author: Samuel Poff
'''

"""
Code generator for Tramelblaze assembly. Utilizes nodes within the AST.
"""
import re
import textwrap



class CodeGen:
    
    def __init__(self):
        self.phrase = []
        self.variables = []
        self.mem_loc = 0
        self.assembly = ""
        self.header = ""
        file = open("assembly.tba","w")
        file.write("")
        file.close()
        
    def file_output(self):
        # write to assembly file
        file = open("assembly.tba","a")
        file.write(self.assembly)
        file.close()
        self.assembly = ""
    def write_header(self):
        # write to assembly file
        print(self.header)
        with open("assembly.tba", 'r+') as file:
            content = file.read()
            file.seek(0, 0)
            file.write(self.header + content)
            file.close()
        self.header = ""
        
    def check_repeat(self, tok):
        # check to see if a variable is already used
        
        for item in self.variables:
            if(item[0] == tok.val):
                # Variable has already been mapped to memory location
                if(tok.val.isupper()):
                    temp_equ = tok.val
                else:
                    temp_equ = tok.val.upper()+'_'
                return temp_equ
        
        # Add to the variable list, return the new location
        self.mem_loc = self.mem_loc + 1
        if(tok.val.isupper()):
            temp_equ = tok.val
        else:
            temp_equ = tok.val.upper()+'_'
        self.header = self.header + temp_equ + '\tEQU ' + hex(int(self.mem_loc))[2:].rjust(4, '0') + '\n'
        self.variables.append((tok.val,self.mem_loc))
        
        return temp_equ
    
    def e_add(self):
        temp = 0
        mem1 = '0'
        mem2 = '0'
        if(self.phrase[0].type == 'IDENTIFIER'):
            print('HERE')
            mem1 = self.check_repeat(self.phrase[0])
        elif(self.phrase[0].type == 'NUMBER'):
            temp = temp + int(self.phrase[0].val)
        if(self.phrase[2].type == 'IDENTIFIER'):
            mem2 = self.check_repeat(self.phrase[2])
        elif(self.phrase[2].type == 'NUMBER'):
            temp = temp + int(self.phrase[2].val)
        
        try:
            first = int(self.phrase[0].val)
        except ValueError:
            first = 0
        try:
            second = int(self.phrase[2].val)
        except ValueError:
            second = 0
        
        temp = first + second
        
        if(temp == 0):
            asm = '\tFETCH\tR4, ' + mem1 + '\n'
            asm = '\tFETCH\tR5, ' + mem2 + '\n'
            asm = asm + '\tADD \tR4, R5\n'
        elif(temp == first):
            asm = '\tFETCH\tR4, ' + mem2 + '\n'
            asm = asm + '\tADD \tR4 ' + hex(temp)[2:].rjust(4, '0') + '\n'
        elif(temp == second):
            asm = '\tFETCH\tR4, ' + mem1 + '\n'
            asm = asm + '\tADD \tR4 ' + hex(temp)[2:].rjust(4, '0') + '\n'
        else:
            asm = '\tLOAD\tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        self.assembly = self.assembly + asm
        
            
    def int_declare(self):
        mem = self.check_repeat(self.phrase[1])
        print(mem)
        asm = '\tLOAD\tR1, '
        if(len(self.phrase) > 3):
            if(self.phrase[3].val == ';'):
                asm = asm + "R4\n"
            else:          
                asm = asm + hex(int(self.phrase[3].val))[2:].rjust(4, '0') + '\n'
        else:
            asm = asm + '0000\n'
        asm = asm + '\tSTORE\tR1, ' + mem + '\n'
        self.assembly = self.assembly + asm
        
    def main_start(self):
        # push main on label on top of main function
        asm = "MAIN\n"
        self.assembly = asm + self.assembly
        print(self.assembly)
        self.file_output()

    def translate(self, rule, phrase):
        self.phrase = phrase
        print(len(self.phrase))
        print(self.phrase)
        #print(rule)
        
        assemble = {
            'MAIN'          : self.main_start,
            'INT_DECLARE'   : self.int_declare,
            'E_ADD_RULE'    : self.e_add,
        }
        #assemble[rule]
        
        # Get the function from switcher dictionary
        
        func = assemble[rule]
        # Execute the function
        func()
   
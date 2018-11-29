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
import sys


class CodeGen:
    
    def __init__(self):
        self.phrase = []
        self.variables = []
        self.mem_loc = 0
        self.assembly = ""
        self.rel = ""
        self.header = ""
        self.footer = ""
        self.label = 0
        self.repeat = 0
        self.else_flag = 0
        self.cond_point = 0
        self.conditionals = ['JUMP','JUMPC','JUMPNC','JUMPZ','JUMPNZ']
        file = open("assembly.tba","w")
        file.write("")
        self.file_pos = file.tell()
        file.close()
        
    def file_output(self):
        # write to assembly file
        file = open("assembly.tba","a")
        file.write(self.assembly)
        file.close()
        self.assembly = ""
        
    def write_header(self):
        # write header to assembly file
        print(self.header)
        # prepend to start of file
        with open("assembly.tba", 'r+') as file:
            content = file.read()
            file.seek(0, 0)
            file.write(self.header + content)
            file.close()
        self.header = ""
    
    def write_footer(self):
        # write header to assembly file
        print(self.footer)
        file = open("assembly.tba","a")
        file.write(self.footer)
        file.close()
        self.footer = ""
    
    def rel_switch(self):
        # reverses the logic for relational statments, e.g. JMPNZ to JMPZ
        pointer = self.cond_point
        if(pointer == 1):
            pointer = 2
        elif(pointer == 2):
            pointer = 1
        elif(pointer == 3):
            pointer = 4
        elif(pointer == 4):
            pointer = 3
        return pointer
    
    def check_repeat(self, tok):
        # check to see if a variable is already used
        for item in self.variables:
            if(item[0] == tok.val):
                # Variable has already been mapped to memory location
                if(tok.val.isupper()):
                    temp_equ = tok.val
                else:
                    temp_equ = tok.val.upper()+'_'
                self.repeat = 1
                return temp_equ
        
        # \t\tADD to the variable list, return the new location
        self.mem_loc = self.mem_loc + 1
        if(tok.val.isupper()):
            temp_equ = tok.val
        else:
            temp_equ = tok.val.upper()+'_'
        self.header = self.header + temp_equ + '\tEQU ' + hex(int(self.mem_loc))[2:].rjust(4, '0') + '\n'
        self.variables.append((tok.val,self.mem_loc))
        self.repeat = 0
        
        return temp_equ
    
    def conditional_generic(self):
        mem1 = '0'
        mem2 = '0'
        if(self.phrase[0].type == 'IDENTIFIER'):
            mem1 = self.check_repeat(self.phrase[0])
        if(self.phrase[2].type == 'IDENTIFIER'):
            mem2 = self.check_repeat(self.phrase[2])
        try:
            first = int(self.phrase[0].val, 0)
        except ValueError:
            first = 0
        try:
            second = int(self.phrase[2].val, 0)
        except ValueError:
            second = 0
        
        temp = first + second
        # both
        if(temp == 0):
            asm = '\t\t\tFETCH\tR6, ' + mem1 + '\n'
            asm = asm + '\t\t\tFETCH\tR5, ' + mem2 + '\n'
            asm = asm + '\t\t\tCOMP \tR6, R5\n'
        elif(temp == first):
            asm = '\t\t\tFETCH\tR6, ' + mem2 + '\n'
            asm = asm + '\t\t\tCOMP \tR6, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        elif(temp == second):
            asm = '\t\t\tFETCH\tR6, ' + mem1 + '\n'
            asm = asm + '\t\t\tCOMP \tR6, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        else:
            asm = '\t\t\tLOAD\tR6, ' + hex(first)[2:].rjust(4, '0') + '\n'
            asm = '\t\t\tCOMP \tR6, ' + hex(second)[2:].rjust(4, '0') + '\n'
        return asm
    
    def port_declare(self):
        for item in self.variables:
            if(item[0] == self.phrase[1]):
                # Variable has already been mapped to memory location
                print("ERROR: " + item[0] + "Variable already declared.")
                sys.exit(1)
        temp_equ = ''
        if(self.phrase[1].val.isupper()):
            temp_equ = self.phrase[1].val
        else:
            temp_equ = self.phrase[1].val.upper()+'_'
        self.header = self.header + temp_equ + '\tEQU ' + hex(int(self.phrase[3].val, 0))[2:].rjust(4, '0') + '\n'
            
    def port_output(self):
        # check if outputing to variable or number
        try:
            temp = int(self.phrase[4].val, 0)
            if(temp > 15):
                print("ERROR: " + str(temp) + "port out of range.")
                sys.exit(1)        
        except ValueError:
            if(self.phrase[5].val.isupper()):
                temp = self.phrase[4].val
            else:
                temp = self.phrase[4].val.upper()+'_'
        # check if mem location is lowercase or uppercase
        if(self.phrase[2].val.isupper()):
            var = self.phrase[2].val
        else:
            var = self.phrase[2].val.upper()+'_'
        asm = '\t\t\tFETCH\tR7, ' + var + '\n'
        asm = asm + '\t\t\tOUTPUT\tR7, '+ str(temp) +'\n'            
        self.assembly = self.assembly + asm
    
    def port_input(self):
        # check if outputing to variable or number
        try:
            temp = int(self.phrase[4].val, 0)
            if(temp > 15):
                print("ERROR: " + str(temp) + "port out of range.")
                sys.exit(1)        
        except ValueError:
            if(self.phrase[5].val.isupper()):
                temp = self.phrase[4].val
            else:
                temp = self.phrase[4].val.upper()+'_'
        # check if mem location is lowercase or uppercase
        if(self.phrase[2].val.isupper()):
            var = self.phrase[2].val
        else:
            var = self.phrase[2].val.upper()+'_'
        asm = '\t\t\tINPUT\tR7, '+ str(temp) +'\n'            
        asm = asm + '\t\t\tSTORE\tR7, ' + var + '\n'        
        self.assembly = self.assembly + asm
        
    def if_statement(self):
        pointer = self.rel_switch()
        asm1 = 'LABEL' + str(self.label) + '\n'
        asm2 = self.rel + '\t\t\t' + str(self.conditionals[pointer]) + '\tLABEL' + str(self.label) + '\t;if statement\n'
        self.label = self.label + 1
        if(self.else_flag == 1):
            asm3 = '\t\t\tJUMP\tLABEL'+ str(self.label) + '\n'
            self.assembly = asm2 + self.assembly + asm3 + asm1
        else:
            self.assembly = asm2 + self.assembly + asm1
    
    def else_statement(self):
        asm1 = 'LABEL' + str(self.label) + '\n'
        self.assembly = self.assembly + asm1
        self.label = self.label + 1
    
    def if_else(self):
        self.file_output()
    
    def while_loop(self):
        label1 = self.label
        self.label = self.label + 1
        label2 = self.label
        asm1 = '\t\t\tJUMP\tLABEL' + str(label2) + '\t;while loop check condition\n' + 'LABEL' + str(label1) + '\n'
        asm2 = 'LABEL' + str(label2) + '\n' + self.rel + '\t\t\t' + str(self.conditionals[self.cond_point]) + '\tLABEL' + str(label1) +'\t;while loop\n' 
        self.label = self.label + 1
        self.assembly = asm1 + self.assembly + asm2
    
    def for_loop(self):
        asm1 = 'LABEL' + str(self.label) + '\n'
        asm2 = self.rel + '\t\t\t' + str(self.conditionals[self.cond_point]) + '\tLABEL' + str(self.label) +'\t;for loop\n' 
        self.label = self.label + 1
        self.assembly = asm1 + self.assembly + asm2
    
        
    
    def conditional_less_than(self):
        self.rel = self.conditional_generic()
        self.cond_point = 1
    
    def conditional_greater_than(self):
        self.rel = self.conditional_generic()
        self.cond_point = 2
    
    def conditional_equal(self):
        self.rel = self.conditional_generic()
        self.cond_point = 3   
    
    def conditional_not_equal(self):
        self.rel = self.conditional_generic()
        self.cond_point = 4
      
    def post_inc(self):
        mem = self.check_repeat(self.phrase[0])
        if(self.repeat == 1):
            asm = '\t\t\tFETCH\tR2, ' + mem + '\n\t\t\tADD \tR2, 0001\n'
            self.assembly = self.assembly + asm 
        else:
            print("ERROR: " + mem + "Variable not declared.")
            sys.exit(1)
            
    def e_add(self):
        temp = 0
        mem1 = '0'
        mem2 = '0'
        if(self.phrase[0].type == 'IDENTIFIER'):
            mem1 = self.check_repeat(self.phrase[0])
        if(self.phrase[2].type == 'IDENTIFIER'):
            mem2 = self.check_repeat(self.phrase[2])
        # check which is a number
        try:
            first = int(self.phrase[0].val, 0)
        except ValueError:
            first = 0
        try:
            second = int(self.phrase[2].val, 0)
        except ValueError:
            second = 0
        
        temp = first + second
        # if both are  
        if(temp == 0):
            asm = '\t\t\tFETCH\tR4, ' + mem1 + '\n'
            asm = asm + '\t\t\tFETCH\tR5, ' + mem2 + '\n'
            asm = asm + '\t\t\tADD \tR4, R5\n'
        # if first element is a number and third is a variable
        elif(temp == first):
            asm = '\t\t\tFETCH\tR4, ' + mem2 + '\n'
            asm = asm + '\t\t\tADD \tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        # if third element is a number and first is a variable
        elif(temp == second):
            asm = '\t\t\tFETCH\tR4, ' + mem1 + '\n'
            asm = asm + '\t\t\tADD \tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        # if there is no variable, pre-process
        else:
            asm = '\t\t\tLOAD\tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        self.assembly = self.assembly + asm
     
    def e_and(self):
        temp = 0
        mem1 = '0'
        mem2 = '0'
        if(self.phrase[0].type == 'IDENTIFIER'):
            print('HERE\n\n')
            mem1 = self.check_repeat(self.phrase[0])
        if(self.phrase[2].type == 'IDENTIFIER'):
            print('HERE\n\n')
            mem2 = self.check_repeat(self.phrase[2])
        # check which is a number
        try:
            first = int(self.phrase[0].val, 0)
        except ValueError:
            first = 0
        try:
            second = int(self.phrase[2].val, 0)
        except ValueError:
            second = 0
        
        temp = first & second
        # if both are  
        if(first == 0 and second == 0):
            asm = '\t\t\tFETCH\tR4, ' + mem1 + '\n'
            asm = asm + '\t\t\tFETCH\tR5, ' + mem2 + '\n'
            asm = asm + '\t\t\tAND \tR4, R5\n'
        # if first element is a number and third is a variable
        elif(temp != first):
            asm = '\t\t\tFETCH\tR4, ' + mem2 + '\n'
            asm = asm + '\t\t\tAND \tR4, ' + hex(first)[2:].rjust(4, '0') + '\n'
        # if third element is a number and first is a variable
        elif(temp != second):
            asm = '\t\t\tFETCH\tR4, ' + mem1 + '\n'
            asm = asm + '\t\t\tAND \tR4, ' + hex(second)[2:].rjust(4, '0') + '\n'
        # if there is no variable, pre-process
        else:
            asm = '\t\t\tLOAD\tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        self.assembly = self.assembly + asm
    
    def e_or(self):
        temp = 0
        mem1 = '0'
        mem2 = '0'
        if(self.phrase[0].type == 'IDENTIFIER'):
            mem1 = self.check_repeat(self.phrase[0])
        if(self.phrase[2].type == 'IDENTIFIER'):
            mem2 = self.check_repeat(self.phrase[2])
        # check which is a number
        try:
            first = int(self.phrase[0].val, 0)
        except ValueError:
            first = 0
        try:
            second = int(self.phrase[2].val, 0)
        except ValueError:
            second = 0
        
        temp = first | second
        # if both are  
        if(first == 0 and second == 0):
            asm = '\t\t\tFETCH\tR4, ' + mem1 + '\n'
            asm = asm + '\t\t\tFETCH\tR5, ' + mem2 + '\n'
            asm = asm + '\t\t\tOR  \tR4, R5\n'
        # if first element is a number and third is a variable
        elif(temp == first):
            asm = '\t\t\tFETCH\tR4, ' + mem2 + '\n'
            asm = asm + '\t\t\tOR  \tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        # if third element is a number and first is a variable
        elif(temp == second):
            asm = '\t\t\tFETCH\tR4, ' + mem1 + '\n'
            asm = asm + '\t\t\tOR  \tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        # if there is no variable, pre-process
        else:
            asm = '\t\t\tLOAD\tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        self.assembly = self.assembly + asm
    
    def e_xor(self):
        temp = 0
        mem1 = '0'
        mem2 = '0'
        if(self.phrase[0].type == 'IDENTIFIER'):
            mem1 = self.check_repeat(self.phrase[0])
        if(self.phrase[2].type == 'IDENTIFIER'):
            mem2 = self.check_repeat(self.phrase[2])
        # check which is a number
        try:
            first = int(self.phrase[0].val, 0)
        except ValueError:
            first = 0
        try:
            second = int(self.phrase[2].val, 0)
        except ValueError:
            second = 0
        
        temp = first ^ second
        # if both are  
        if(first == 0 and second == 0):
            asm = '\t\t\tFETCH\tR4, ' + mem1 + '\n'
            asm = asm + '\t\t\tFETCH\tR5, ' + mem2 + '\n'
            asm = asm + '\t\t\tXOR \tR4, R5\n'
        # if first element is a number and third is a variable
        elif(temp == first):
            asm = '\t\t\tFETCH\tR4, ' + mem2 + '\n'
            asm = asm + '\t\t\tXOR \tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        # if third element is a number and first is a variable
        elif(temp == second):
            asm = '\t\t\tFETCH\tR4, ' + mem1 + '\n'
            asm = asm + '\t\t\tXOR \tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        # if there is no variable, pre-process
        else:
            asm = '\t\t\tLOAD\tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
        self.assembly = self.assembly + asm
        
    def assign_statement(self):
        mem = self.check_repeat(self.phrase[0])
        asm = ""
        if(self.repeat == 1):
            if(self.phrase[2].type == 'NUMBER'):
                temp = int(self.phrase[2].val, 0)
                asm = '\t\t\tLOAD\tR4, ' + hex(temp)[2:].rjust(4, '0') + '\n'
            asm = asm + '\t\t\tSTORE\tR4, ' + mem
            
            self.assembly = self.assembly + asm + '\n'
        else:
            print("ERROR: " + mem + "Variable not declared.")
            sys.exit(1)
        
    def int_declare(self):
        mem = self.check_repeat(self.phrase[1])
        print(mem)
        asm = '\t\t\tLOAD\tR1, '
        if(len(self.phrase) > 3):
            if(self.phrase[3].val == ';'):
                asm = asm + "R4\n"
            else:          
                asm = asm + hex(int(self.phrase[3].val, 0))[2:].rjust(4, '0') + '\n'
        else:
            asm = asm + '0000\n'
        asm = asm + '\t\t\tSTORE\tR1, ' + mem + '\n'
        self.assembly = self.assembly + asm
        
    def main_start(self):
        # push main on label on top of main function
        asm = "\nMAIN\n"
        print(self.assembly)
        with open("assembly.tba", 'r+') as file:
            file.seek(self.file_pos)
            content = file.read()
            file.seek(self.file_pos)
            file.write(asm + content + self.assembly + '\n\n')
            self.file_pos = file.tell()
            file.close()
        self.assembly = ""
        #self.file_output()
    
    def isr_start(self):
        asm1 = '\t\t\tADDRESS\t0300\n' + '\nISR\n'
        asm2 = '\t\t\tRETEN'
        self.assembly = self.assembly + asm2
        self.footer = self.footer + "\t\t\tADDRESS\t0FFE\n\n"+"\t\t\tJUMP\tISR"+"\n\n\t\t\tEND"
        with open("assembly.tba", 'r+') as file:
            file.seek(self.file_pos)
            content = file.read()
            file.seek(self.file_pos)
            file.write(asm1 + content + self.assembly + '\n\n')
            self.file_pos = file.tell()
            file.close()
        self.assembly = ""
        
    def enable_interrupt(self):
        asm = '\t\t\tENINT\n'
        self.assembly = self.assembly + asm
        
    def disable_interrupt(self):
        asm = '\t\t\tDISINT\n'
        self.assembly = self.assembly + asm

    def translate(self, rule, phrase):
        self.phrase = phrase
        print(len(self.phrase))
        print(self.phrase)
        #print(rule)
        
        assemble = {
            'MAIN'              : self.main_start,
            'ISR'               : self.isr_start,
            'INT_DECLARE'       : self.int_declare,
            'ENABLE_INTERRUPT'  : self.enable_interrupt,
            'DISABLE_INTERRUPT' : self.disable_interrupt,
            'E_ADD_RULE'        : self.e_add,
            'E_XOR_RULE'        : self.e_xor,
            'E_OR_RULE'         : self.e_or,
            'E_AND_RULE'        : self.e_and,
            'E_EQUALS_RULE'     : self.conditional_equal,
            'E_LESS_THAN'       : self.conditional_less_than,
            'E_GREATER_THAN'    : self.conditional_greater_than,
            'PORT_DECLARE'      : self.port_declare,
            'PORT_OUTPUT'       : self.port_output,
            'PORT_INPUT'        : self.port_input,
            'ASSIGN'            : self.assign_statement,
            'IF_STATEMENT'      : self.if_statement,
            'ELSE_STATEMENT'    : self.else_statement,
            'IF_ELSE_STATEMENT' : self.if_else,
            'WHILE_LOOP'        : self.while_loop,
            'FOR_LOOP'          : self.for_loop,
            'POST_INC_RULE'     : self.post_inc,
            
        }
        #assemble[rule]
        
        # Get the function from switcher dictionary
        
        func = assemble[rule]
        # Execute the function
        func()
   
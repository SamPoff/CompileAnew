'''
Created on Oct 12, 2018

@author: Harrison Fitch
@author: Samuel Poff
'''

"""
Traverses the Abstract Syntax Tree created by the parser.
"""
import re
from ParseNode import ParseNode
from CodeGen import CodeGen

class TreeClimber:
    
    def __init__(self, position):
        self.position = position
        self.CodeGen = CodeGen()
        
    def climb(self, tree):
        if(tree.children):
            print(tree.rule)
        if(tree.rule.new == 'IF_ELSE_STATEMENT'):
            self.CodeGen.else_flag = 1
        if(tree.rule.new == 'FOR_LOOP' or tree.rule.new == 'IF_STATEMENT'or tree.rule.new == 'ELSE_STATEMENT' or tree.rule.new == 'WHILE_LOOP'):
            self.CodeGen.file_output()
        if(tree.rule.orig == 'FUNCT_DECLARE'):
            self.CodeGen.header_flag = False
        
        
        if(tree.rule.new == 'IF_STATEMENT' or tree.rule.new == 'PRIME_STATEMENT' or tree.rule.new == 'STATEMENT' ):
            self.CodeGen.express_index = 0
            self.CodeGen.express_list = []
        # Order of operations
        if(tree.rule.orig == 'E'):
            self.CodeGen.express_list.append((tree.rule.priority,self.CodeGen.express_index))
            self.CodeGen.express_index = self.CodeGen.express_index + 1
            self.CodeGen.express_list = sorted(self.CodeGen.express_list,key=lambda x:(x[0],-x[1]))
            self.CodeGen.temp_assembly = ["" for x in range(len(self.CodeGen.express_list))]            
            #print(self.CodeGen.express_list)
            #print(self.CodeGen.temp_assembly)
    
    
        for child in tree.children:
            if(type(child) == ParseNode):
                # go to the deepest node
                self.climb(child)
        toks = []
        for child in tree.children:
            if(type(child) != ParseNode):
                print("")
                toks.append(child)
                print(child.val, end = '')
        print('\n')
        
        # Comment out next line to test the traveler only 
        self.CodeGen.translate(tree.rule.new,toks)
        # order of operations
        if(tree.rule.orig == 'E'):
            self.CodeGen.express_index = self.CodeGen.express_index -1
        
        """
        for child in tree.children:
            if(type(child) != ParseNode):
                print(child.val, end = '')    
        print('\n')
        """
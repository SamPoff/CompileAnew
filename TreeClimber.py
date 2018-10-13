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
        self.CodeGen.translate(tree.rule,toks)
        """
        for child in tree.children:
            if(type(child) != ParseNode):
                print(child.val, end = '')    
        print('\n')
        """
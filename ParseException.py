'''
Created on Oct 5, 2018

@author: Harrison Fitch
@author: Samuel Poff
'''

import ParseNode 
# from ParseNode import ParseNode

class ParseException(Exception):
    """An exception raised if the parsing goes badly"""

    def __init__(self, stack):
        self.stack = stack

    def __str__(self):
        print("Error parsing input.\nEnd tree: ",end='')
        for item in self.stack :
            if(type(item) != ParseNode.ParseNode):
                try:
                    print(item.val)
                except TypeError:
                    print()
        return " " 



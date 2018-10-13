'''
Created on Oct 12, 2018

@author: Harrison Fitch
@author: Samuel Poff
'''

import re
# from ParseNode import ParseNode

class CodeGenException(Exception):
    """An exception raised if the parsing goes badly"""

    def __init__(self, stack):
        self.stack = stack

    def __str__(self):
        return "Error parsing input.\nEnd tree: " + str(self.stack)



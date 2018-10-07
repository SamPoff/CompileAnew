'''
Created on Oct 5, 2018

@author: Fitch
@author: Sam
'''

import re
# from ParseNode import ParseNode

class ParseException(Exception):
    """An exception raised if the parsing goes badly"""

    def __init__(self, stack):
        self.stack = stack

    def __str__(self):
        return "Error parsing input.\nEnd tree: " + str(self.stack)



'''
Created on Oct 5, 2018

@author: Harrison Fitch
@author: Samuel Poff
'''

class Token(object):

    # A simple Token structure.
    # Contains the token type, value and position.
    def __init__(self, type, val, priority, pos): 
        self.type = type
        self.val = val
        self.priority = priority
        self.pos = pos
  
    # Defines the return value when a token is printed. 
    def __str__(self):
        return 'Lexeme Type: %s, Value: %s, At: %s, Priority: %s' % (self.type, self.val, self.pos, self.priority)


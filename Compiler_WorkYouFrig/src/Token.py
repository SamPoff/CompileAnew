'''
Created on Oct 5, 2018

@author: Fitch
@author: Sam
'''

class Token(object):

    # A simple Token structure.
    # Contains the token type, value and position.
    def __init__(self, type, val, priority, pos):  # @ReservedAssignment
        self.type = type
        self.val = val
        self.pos = pos
        self.priority = priority
  
    # Defines the return value when a token is printed. 
    def __str__(self):
        return 'Lexeme Type: %s, Value: %s, At: %s' % (self.type, self.val, self.pos)

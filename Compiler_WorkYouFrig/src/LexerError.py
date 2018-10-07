'''
Created on Oct 5, 2018

@author: Fitch
@author: Sam
'''


class LexerError(Exception):

    # Returns position where a lexing error has occured. 
    def __init__(self, pos):
        self.pos = pos

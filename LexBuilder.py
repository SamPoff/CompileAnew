'''
Created on Oct 5, 2018

@author: Harrison Fitch
@author: Samuel Poff
'''

import re
from Token import Token
import LexerError

class LexBuilder(object):
    """ A simple regex-based lexer/tokenizer.
        See below for an example of usage.
    """

    def __init__( self, rules, filename , skip_whitespace=False ):
        # All the regexes are concatenated into a single one
        # with named groups. Since the group names must be valid
        # Python identifiers, but the token types used by the
        # user are arbitrary strings, we auto-generate the group
        # names and map them to token types.
        index = 1
        regex_parts = []
        self.group_type = {}
        self.prio = {}

        for regex, type, priority in rules:  # @ReservedAssignment
            groupname = 'GROUP%s' % index
            regex_parts.append('(?P<%s>%s)' % (groupname, regex))
            self.group_type[groupname] = type
            self.prio[groupname] = priority
            index += 1

        self.regex = re.compile('|'.join(regex_parts))
        self.skip_whitespace = skip_whitespace
        self.re_ws_skip = re.compile('\S')
        self.data = self.inputLexData( filename )
#         print(self.data)
        self.input( self.data )

    def inputLexData( self, filename ):
        with open(filename, 'r') as myfile:
            data = myfile.read()
            #data = re.sub(re.compile("(\/\*[\w\'\s\r\n\*]*\*\/)|(\/\/[\w\s\']*)|(\<![\-\-\s\w\>\/]*\>)"),"",data)
            data = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,data) # remove all occurance streamed comments (/*COMMENT */) from string
            data = re.sub(re.compile("//.*?\n" ) ,"" ,data) # remove all occurance singleline comments (//COMMENT\n ) from string
            data = data.replace('\n', '')
            return data
        

    def input(self, buf):
        # Initialize the lexer with a buffer as input.
        self.buf = buf
        self.pos = 0

    def token(self):
        """ Return the next token (a Token object) found in the
            input buffer. None is returned if the end of the
            buffer was reached.
            In case of a lexing error (the current chunk of the
            buffer matches no rule), a LexerError is raised with
            the position of the error.
        """
        if self.pos >= len(self.buf):
            return None
        else:
            if self.skip_whitespace:
                m = self.re_ws_skip.search(self.buf, self.pos)

                if m:
                    self.pos = m.start()
                else:
                    return None
                
            m = self.regex.match(self.buf, self.pos)
            if m:
                groupname = m.lastgroup
                tok_type = self.group_type[groupname]
                tok_prio = self.prio[groupname]
                tok = Token(tok_type, m.group(groupname), tok_prio, self.pos)
                self.pos = m.end()
                return tok

            # if we're here, no rule matched
            error = LexerError(self.pos)
            raise error

    def tokens(self):
        """ Returns an iterator to the tokens found in the buffer.
        """
        while 1:
            LexBuilder.tok = self.token()
            if LexBuilder.tok is None: break
            yield LexBuilder.tok
           
    @staticmethod 
    def genTokenList( lexObj ):
        try:
            token_list = []
            for index, tok in enumerate(lexObj.tokens()):
                    token_list.append(tok)
                    """
                    Prints tokens when found.
                    """
#                     print('Token found at index: ', index, tok.val, ' Token priority: ', tok.priority)
            print('\n')
            return token_list
        except LexerError as err:
            print('LexerError at position %s' % err.pos)
    
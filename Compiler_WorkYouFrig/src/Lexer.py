'''
Created on Oct 5, 2018

@author: Fitch
@author: Sam
'''

import re
from Token import Token
import LexerError
import Rules
import Parse

#test
class Lexer(object):
    """ A simple regex-based lexer/tokenizer.
        See below for an example of usage.
    """

    def __init__(self, rules, skip_whitespace=False):
        """ Create a lexer.
            rules:
                A list of rules. Each rule is a `regex, type`
                pair, where `regex` is the regular expression used
                to recognize the token and `type` is the type
                of the token to return when it's recognized.
            skip_whitespace:
                If True, whitespace (\s+) will be skipped and not
                reported by the lexer. Otherwise, you have to
                specify your rules for whitespace, or it will be
                flagged as an error.
        """
        # All the regexes are concatenated into a single one
        # with named groups. Since the group names must be valid
        # Python identifiers, but the token types used by the
        # user are arbitrary strings, we auto-generate the group
        # names and map them to token types.
        idx = 1
        regex_parts = []
        self.group_type = {}
        self.prio = {}

        for regex, type, priority in rules:  # @ReservedAssignment
            groupname = 'GROUP%s' % idx
            regex_parts.append('(?P<%s>%s)' % (groupname, regex))
            self.group_type[groupname] = type
            self.prio[groupname] = priority
            idx += 1

        self.regex = re.compile('|'.join(regex_parts))
        self.skip_whitespace = skip_whitespace
        self.re_ws_skip = re.compile('\S')

    def input(self, buf):
        """ Initialize the lexer with a buffer as input.
        """
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
            Lexer.tok = self.token()
            if Lexer.tok is None: break
            yield Lexer.tok
            
    def start(self, filename, rules): 
            with open(filename, 'r') as myfile:
                data = myfile.read().replace('\n', '')
        #         print( data )
         
            lx = Lexer(rules, skip_whitespace=True)
            lx.input(data)
         
            try:
                token_list = []
                for index, tok in enumerate(lx.tokens()):
                    if(tok.type == 'COMMENT'):
                        tok = None
                    else:
                        token_list.append(tok)
                        print(index, tok.val, tok.priority)
            except LexerError as err:
                print('LexerError at position %s' % err.pos)
             
            # start symbol used in parser
            start_symbol = Token("START", "START", None, None)
             
            tree = Parse.generate_tree(token_list, Rules.rules, start_symbol)
            print(tree)
            print("\n\n\n\n")
            print(tree.bracket_repr())
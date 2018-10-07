'''
Created on Oct 5, 2018

@author: Fitch
@author: Sam
'''

from LexBuilder import LexBuilder
from NewCompile import NewCompile
from Token import Token
from ParseException import ParseException
from ParseException import generate_tree
from Rule import Rule
from LexerError import LexerError


# Change this path to source '.c' file.
path = 'C:\\Users\\Sam\\My Documents\\LiClipse Workspace\\Compiler\\src\\test.c'


def inputLexData( filename ):
        with open(filename, 'r') as myfile:
            data = myfile.read().replace('\n', '')
            return data
        
def genTokenList( lexObj ):
    try:
        token_list = []
        for index, tok in enumerate(lexObj.tokens()):
            if(tok.type == 'COMMENT'):
                tok = None
            else:
                token_list.append(tok)
                print('Token found at index: ', index, tok.val, ' Token priority: ', tok.priority)
    except LexerError as err:
        print('LexerError at position %s' % err.pos)

# Generates an object containing the lexing rules and path
# to the '.c' file.
compileObj = NewCompile( path )

# Generates a lexer object with the rules specified
# in compObj.
lexObj = LexBuilder( compileObj.rules, skip_whitespace=True )

# Get text data from file you want to lex, then input data
# into lexer object.
data = lexObj.inputLexData( path )
lexObj.input( data )
genTokenList( lexObj )

# try:
#     token_list = []
#     for index, tok in enumerate(lexObj.tokens()):
#         if(tok.type == 'COMMENT'):
#             tok = None
#         else:
#             token_list.append(tok)
#             print('Token found at index: ', index, tok.val, ' Token priority: ', tok.priority)
# except LexerError as err:
#     print('LexerError at position %s' % err.pos)
#   
# # start symbol used in parser
# start_symbol = Token("START", "START", None, None)
#   
# tree = ParseException.generate_tree(token_list, Rule.rules, start_symbol)
# print(tree)
# print("\n\n\n\n")
# print(tree.bracket_repr())



# def start(self, filename, rules): 
#         with open(filename, 'r') as myfile:
#             data = myfile.read().replace('\n', '')
# #             print( data )
#      
#         lx = LexBuilder(rules, skip_whitespace=True)
#         lx.input(data)
#      
#         try:
#             token_list = []
#             for index, tok in enumerate(lx.tokens()):
#                 if(tok.type == 'COMMENT'):
#                     tok = None
#                 else:
#                     token_list.append(tok)
#                     print(index, tok.val, tok.priority)
#         except LexerError as err:
#             print('LexerError at position %s' % err.pos)
#           
#         # start symbol used in parser
#         start_symbol = Token("START", "START", None, None)
#           
#         tree = ParseNode.generate_tree(token_list, Rule.rules, start_symbol)
#         print(tree)
#         print("\n\n\n\n")
#         print(tree.bracket_repr())



# Starts the actural lexing process, results in a 
# lex_obj.start( path, compile_obj.rules )
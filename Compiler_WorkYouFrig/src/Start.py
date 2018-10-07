'''
Created on Oct 5, 2018

@author: Fitch
@author: Sam
'''

from LexBuilder import LexBuilder
from NewCompile import NewCompile
from Token import Token
from ParseNode import ParseNode

# from LexBuilder import genTokenList
# Change this path to source '.c' file.
path = 'C:\\Users\\Sam\\My Documents\\LiClipse Workspace\\Compiler\\src\\test.c'

# Generates an object containing the lexing rules and path
# to the '.c' file.
compileObj = NewCompile( path )

# Generates a lexer object with the rules specified
# in compObj. Also adds in all the data from the input file.
lexObj = LexBuilder( compileObj.rules, compileObj.filename, skip_whitespace=True )
print( 'Data in Lexer Object: ', lexObj.data, '\n' )

# Generate a list of tokens from lex object.
tokenList = lexObj.genTokenList( lexObj )

# start symbol used in parser
start_symbol = Token( "START", "START", None, None )
# print(start_symbol)
  
tree = ParseNode.generate_tree( tokenList, compileObj.rules, start_symbol )
#             print(tree)
#             print("\n\n\n\n")
#             print(tree.bracket_repr())
   




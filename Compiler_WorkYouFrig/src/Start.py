'''
Created on Oct 5, 2018

@author: Fitch
@author: Sam
'''

from NewCompile import NewCompile
from LexBuilder import LexBuilder
from ParseNode import ParseNode
from Token import Token
import Rule

"""
# Change this path to source file.
"""
path = 'C:\\Users\\Sam\\My Documents\\LiClipse Workspace\\Compiler\\src\\test.c'

# Generates an object containing the lexing rules and path
# to the '.c' file.
compileObj = NewCompile( path )

# Generates a lex object with the rules specified
# in the compObj. Also adds in all the data from the input file
# to the lex object automatically.
lexObj = LexBuilder( compileObj.rules, compileObj.filename, skip_whitespace=True )
# print( 'Data in Lexer Object: ', lexObj.data, '\n' )

# Generate a list of tokens from lex object.
tokenList = lexObj.genTokenList( lexObj )
print('Start token list')
for tok in tokenList:
    print(tok.val)
    
# start symbol used in parser
start_symbol = Token( "START", "START", None, None )
# print(start_symbol)
  
tree = ParseNode.generate_tree( tokenList, Rule.rules, start_symbol )
#             print(tree)
#             print("\n\n\n\n")
#             print(tree.bracket_repr())
   

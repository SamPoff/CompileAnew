'''
Created on Oct 5, 2018

@author: Fitch
@author: Sam
'''

import sys
from antlr4 import *
from NewCompile import NewCompile
from LexBuilder import LexBuilder
from ParseNode import ParseNode
from Token import Token
import Rule
from CLexer import CLexer
from io import *

"""
# Change this path to source file.
"""
# path = 'C:\\Users\\Sam\\My Documents\\LiClipse Workspace\\Compiler\\src\\test.c'
# path = '/Users/sp31485/git/CompileAnew/Compiler_WorkYouFrig/src/test.c'
path = '/home/sam/git/CompileAnew/Compiler_WorkYouFrig/src/test.c'
file = open( path, "r", encoding="utf-8" )
print( file.line_buffering )
input = FileStream( path )
lexer = CLexer( input )


# # Generates an object containing the lexing rules and path
# # to the '.c' file.
# compileObj = NewCompile( path )
# 
# # Generates a lex object with the rules specified
# # in the compObj. Also adds in all the data from the input file
# # to the lex object automatically.
# lexObj = LexBuilder( compileObj.rules, compileObj.filename, skip_whitespace=True )
# 
# # Generate a list of tokens from lex object.
# tokenList = lexObj.genTokenList( lexObj )
# for tok in tokenList:
#     print(tok)
# 
# # Start symbol used in parser.
# start_symbol = Token( "START", "START", None, None )
# 
# # Generate abstract syntax tree.
# tree = ParseNode.generate_tree( tokenList, Rule.rules, start_symbol )
# # print(tree)
# # print("\n\n\n\n")
# # print(tree.bracket_repr())
   

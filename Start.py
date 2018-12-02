'''
Created on Oct 5, 2018

@author: Harrison Fitch
@author: Samuel Poff
'''

from NewCompile import NewCompile
from LexBuilder import LexBuilder
from ParseNode import ParseNode
from Token import Token
from TreeClimber import TreeClimber
import Rule

"""
# Change this path to source file.
"""
path = 'test2.c'
# path = '/Users/sp31485/git/CompileAnew/Compiler_WorkYouFrig/src/test.c'

# Generates an object containing the lexing rules and path
# to the '.c' file.
compileObj = NewCompile( path )

# Generates a lex object with the rules specified
# in the compObj. Also adds in all the data from the input file
# to the lex object automatically.
lexObj = LexBuilder( compileObj.rules, compileObj.filename, skip_whitespace=True )

# Generate a list of tokens from lex object.
tokenList = lexObj.genTokenList( lexObj )
for tok in tokenList:
    print(tok)

# Start symbol used in parser.
start_symbol = Token( "START", "START", None, None )

# Generate abstract syntax tree.
tree = ParseNode.generate_tree( tokenList, Rule.rules, start_symbol )
print('\n\n\n')

print(tree)
print("\n\n\n\n")
for node in tree:
    if(type(node) == ParseNode):
        print(node.bracket_repr())

#declkare iterator and code generator 
traveler = TreeClimber(0)

'''
Refer to TreeClimber class. The tree is broken into functions,
tree climber can break down each singular function to code generate. This 
process is done by iterating through the tree list, which is a list of 
functions that make up the program.
'''

for node in tree:
    if(type(node) == ParseNode):
        traveler.climb(node)
traveler.CodeGen.write_header()
traveler.CodeGen.write_footer()

import trambler4
trambler4

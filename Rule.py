'''
Created on Oct 5, 2018

@author: Harrison Fitch
@author: Samuel Poff
'''

"""
Rule class to represent grammar rules for parser.
"""

class Rule:
    """A rule in the CFG for C"""

    def __init__(self, value, orig, new, priority = None):
        # orig - stores the symbol the rules replaces
        # new - stores the symbol(s) the rules replaces `orig` with
        # priority - priority of the rule relative to priority of nex
        self.orig = orig
        self.value = value
        self.new = new
        self.priority = priority

    def __repr__(self):
        return str(self.orig) + " -> " + str(self.new)

    
########################################################################
# Below is a list of grammar rules applicable to the py.py file.
# These rules are used to represent the Context Free Grammar of C.
# Regex is utilizes these rules for the parse, and each rule must
# adhere to Regex's grammar.
########################################################################

# int main() {}
main_funct = Rule('(TYPE_INT)(MAIN)(LP)(RP)(LB)(STATEMENT|IF_STATEMENT|PRIME_STATEMENT)*?(RB)', 'FUNCT_DECLARE', 'MAIN', None)

########################################################################
# Integer declares and port declares are prime statements.
# This means they can be used outside of a function.
# Purposes include global variables and ports used in the ISR.
########################################################################
# int id;;
int_declare = Rule('((TYPE_INT)(IDENTIFIER)(EQUALSIGN)(E|UE|NUMBER|HEX|IDENTIFIER|PARA)(SEMICOLON)|'
                       '(TYPE_INT)(IDENTIFIER)(SEMICOLON))', 'PRIME_STATEMENT', 'INT_DECLARE', None)

int_array_declare = Rule('((TYPE_INT)(IDENTIFIER)(LK)(NUMBER|IDENTIFIER)(RK)(EQUALSIGN)(LB)((((NUMBER|HEX|IDENTIFIER)(COMMA))*?)(E|UE|NUMBER|HEX|IDENTIFIER|PARA))(RB)(SEMICOLON)|'
                       '(TYPE_INT)(IDENTIFIER)(LK)(NUMBER|IDENTIFER)(RK)(SEMICOLON)|'
                       '(TYPE_INT)(IDENTIFIER)(LK)(RK)(EQUALSIGN)(LB)((((NUMBER|HEX|IDENTIFIER)(COMMA))*?)(E|UE|NUMBER|HEX|IDENTIFIER|PARA))(RB)(SEMICOLON))', 'PRIME_STATEMENT', 'INT_ARRAY_DECLARE', None)

port_declare = Rule('(TYPE_PORT)(IDENTIFIER)(EQUALSIGN)(NUMBER|HEX)(SEMICOLON)', 'PRIME_STATEMENT', 'PORT_DECLARE', None)

# if( some t/f expression ) {}
if_statement = Rule('((IF)(PARA)(LB)(STATEMENT|IF_STATEMENT)*?(RB)|'
                         '(IF)(PARA)(STATEMENT|IF_STATEMENT))', 'IF_STATEMENT', 'IF_STATEMENT', None)
if_else = Rule('((IF_STATEMENT)(ELSE_STATEMENT)|'
                         '(IF_STATEMENT)(ELSE_STATEMENT))', 'STATEMENT', 'IF_ELSE_STATEMENT', None)
else_statement = Rule('((ELSE)(LB)(STATEMENT|IF_STATEMENT)*?(RB)|'
                         '(ELSE)(STATEMENT|IF_STATEMENT))', 'ELSE_STATEMENT', 'ELSE_STATEMENT', None)

# for( statement; expression; statement ) {} or for( statement; expression; statement ) statement; 
for_loop = Rule('((FOR)(LP)(PRIME_STATEMENT|STATEMENT)(E)(SEMICOLON)(((IDENTIFIER)(EQUALSIGN)(E))|(UE))(RP)(LB)(STATEMENT|IF_STATEMENT)*?(RB)|'
                 '(FOR)(LP)(PRIME_STATEMENT|STATEMENT)(E)(SEMICOLON)(((IDENTIFIER)(EQUALSIGN)(E))|(UE))(RP)(STATEMENT|IF_STATEMENT|SEMICOLON))', 'STATEMENT', 'FOR_LOOP', None)

# while( expression ){}
while_loop = Rule('((WHILE)(PARA)(LB)(STATEMENT|IF_STATEMENT)*?(RB)|'
                         '(WHILE)(PARA)(STATEMENT|IF_STATEMENT|SEMICOLON))', 'STATEMENT', 'WHILE_LOOP', None)

# id = something;
assign_rule = Rule('(IDENTIFIER)(EQUALSIGN)(E|UE|NUMBER|HEX|IDENTIFIER|PARA)(SEMICOLON)', 'STATEMENT', 'ASSIGN', None)

# id >> 1
shift_right = Rule('(NUMBER|HEX|IDENTIFIER|E|PARA)(RIGHTSHIFT)(NUMBER|HEX)', 'E', 'E_SHIFT_RIGHT', 5)

# id << 1 
shift_left = Rule('(NUMBER|HEX|IDENTIFIER|E|PARA)(LEFTSHIFT)(NUMBER|HEX)', 'E', 'E_SHIFT_LEFT', 5)

# num/id + num/id
add_rule = Rule('(NUMBER|HEX|IDENTIFIER|E|PARA)(PLUS)(NUMBER|HEX|IDENTIFIER|E|PARA)', 'E', 'E_ADD_RULE', 4)

# num/id & num/id
and_rule = Rule('(NUMBER|HEX|IDENTIFIER|E|PARA)(BIT_AND)(NUMBER|HEX|IDENTIFIER|E|PARA)', 'E', 'E_AND_RULE', 8)

# num/id | num/id
or_rule = Rule('(NUMBER|HEX|IDENTIFIER|E|PARA)(BIT_OR)(NUMBER|HEX|IDENTIFIER|E|PARA)', 'E', 'E_OR_RULE', 9)

# num/id ^ num/id
xor_rule = Rule('(NUMBER|HEX|IDENTIFIER|E|PARA)(BIT_XOR)(NUMBER|HEX|IDENTIFIER|E|PARA)', 'E', 'E_XOR_RULE', 10)

# id ++
post_inc_rule = Rule('(IDENTIFIER)(DOUBLE_PLUS)', 'UE', 'POST_INC_RULE', 1)

# ++ id
pre_inc_rule = Rule('(DOUBLE_PLUS)(IDENTIFIER)', 'UE', 'PRE_INC_RULE', 1)

# id --
post_dec_rule = Rule('(IDENTIFIER)(DOUBLE_MINUS)', 'UE', 'POST_DEC_RULE', 1)

# -- id
pre_dec_rule = Rule('(DOUBLE_MINUS)(IDENTIFIER)', 'UE', 'PRE_DEC_RULE', 1)

# unary operation ;
unary_rule = Rule('(UE)(SEMICOLON)', 'STATEMENT', 'UNARY_RULE', None)

# something == something
rel_equal = Rule('(E|UE|NUMBER|HEX|IDENTIFIER)(EQUALVALUE)(E|UE|NUMBER|HEX|IDENTIFIER)', 'E', 'E_EQUALS_RULE', 7)

# something != something
rel_not_equal = Rule('(E|UE|NUMBER|HEX|IDENTIFIER)(NOTEQUAL)(E|UE|NUMBER|HEX|IDENTIFIER)', 'E', 'E_EQUALS_RULE', 7)

# something < something
rel_less_than = Rule('(E|UE|NUMBER|HEX|IDENTIFIER)(LESSTHAN)(E|UE|NUMBER|HEX|IDENTIFIER)', 'E', 'E_LESS_THAN', 6)

# something > something
rel_greater_than = Rule('(E|UE|NUMBER|HEX|IDENTIFIER)(GREATERTHAN)(E|UE|NUMBER|HEX|IDENTIFIER)', 'E', 'E_GREATER_THAN', 6)

# enable interrupt;
enable_interrupt = Rule('(ENABLE)(INTERRUPT)(SEMICOLON)', 'STATEMENT', 'ENABLE_INTERRUPT', None)

# disable interrupt;
disable_interrupt = Rule('(DISABLE)(INTERRUPT)(SEMICOLON)', 'STATEMENT', 'DISABLE_INTERRUPT', None)

# int main() {}
isr_funct = Rule('(ISR_HANDLER)(LP)(RP)(LB)(STATEMENT|IF_STATEMENT|PRIME_STATEMENT)*?(RB)', 'FUNCT_DECLARE', 'ISR', None)

# output(something, somewhere);
port_output = Rule('(OUTPUT)(LP)(IDENTIFIER)(COMMA)(IDENTIFIER)(RP)(SEMICOLON)', 'STATEMENT', 'PORT_OUTPUT', None)
# input(somewhere, something);
port_input = Rule('(INPUT)(LP)(IDENTIFIER)(COMMA)(IDENTIFIER)(RP)(SEMICOLON)', 'STATEMENT', 'PORT_INPUT', None)
# # i = k + l;

# all_ids = Rule('(IDENTIFIER)(EQUALSIGN)(IDENTIFIER)(PLUS)(IDENTIFIER)', 'E', 'E_ALL_IDENTIFIERS', None)

# #define identifier value
define = Rule('(DEFINE)(IDENTIFIER)(NUMBER|HEX)', 'PRIME_STATEMENT', 'DEFINE', None)

parantheses = Rule('(LP)(E|UE|NUMBER|HEX|IDENTIFIER)(RP)', 'PARA', 'PARANTHESES', None)
# The List of rules used for the parse
rules = [
    define,
    parantheses,
    main_funct,
    isr_funct,
    enable_interrupt,
    disable_interrupt,
    int_declare,
    int_array_declare,
    port_declare,
    assign_rule,
    else_statement,
    if_else,
    if_statement,
    for_loop,
    while_loop,
    shift_left,
    shift_right,
    add_rule,
    or_rule,
    and_rule,
    xor_rule,
    post_inc_rule,
    post_dec_rule,
    pre_inc_rule,
    pre_dec_rule,
    unary_rule,
    rel_less_than,
    rel_greater_than,
    rel_equal,
    port_output,
    port_input,

    ]

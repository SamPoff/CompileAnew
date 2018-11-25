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

    def __init__(self, value, orig, new, rules, priority=None):
        # orig - stores the symbol the rules replaces
        # new - stores the symbol(s) the rules replaces `orig` with
        # priority - priority of the rule relative to priority of nex
        self.orig = orig
        self.value = value
        self.new = new
        self.rules = rules
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
main_funct = Rule('(TYPE_INT)(MAIN)(LP)(RP)(LB)(STATEMENT|IF_STATEMENT)*?(RB)', 'FUNCT_DECLARE', 'MAIN', None)

# int id;;
int_declare = Rule('((TYPE_INT)(IDENTIFIER)(EQUALSIGN)(E|UE|NUMBER|HEX|IDENTIFIER)(SEMICOLON)|'
                       '(TYPE_INT)(IDENTIFIER)(SEMICOLON))', 'STATEMENT', 'INT_DECLARE', None)

port_declare = Rule('(TYPE_PORT)(IDENTIFIER)(EQUALSIGN)(NUMBER|HEX)(SEMICOLON)', 'STATEMENT', 'PORT_DECLARE', None)

# if( some t/f expression ) {}
if_statement = Rule('((IF)(LP)(E|UE|NUMBER|HEX|IDENTIFIER)(RP)(LB)(STATEMENT|IF_STATEMENT)*?(RB)|'
                         '(IF)(LP)(E|UE|NUMBER|HEX|IDENTIFIER)(RP)(STATEMENT|IF_STATEMENT))', 'IF_STATEMENT', 'IF_STATEMENT', None)
if_else = Rule('((IF_STATEMENT)(ELSE_STATEMENT)|'
                         '(IF_STATEMENT)(ELSE_STATEMENT))', 'STATEMENT', 'IF_ELSE_STATEMENT', None)
else_statement = Rule('((ELSE)(LB)(STATEMENT|IF_STATEMENT)*?(RB)|'
                         '(ELSE)(STATEMENT|IF_STATEMENT))', 'ELSE_STATEMENT', 'ELSE_STATEMENT', None)

# for( statement; expression; statement ) {} or for( statement; expression; statement ) statement; 
for_loop = Rule('((FOR)(LP)(STATEMENT)(E)(SEMICOLON)(((IDENTIFIER)(EQUALSIGN)(E))|(UE))(RP)(LB)(STATEMENT|IF_STATEMENT)*?(RB)|'
                 '(FOR)(LP)(STATEMENT)(E)(SEMICOLON)(((IDENTIFIER)(EQUALSIGN)(E))|(UE))(RP)(STATEMENT|IF_STATEMENT|SEMICOLON))', 'STATEMENT', 'FOR_LOOP', None)

# while( expression ){}
while_loop = Rule('((WHILE)(LP)(E|UE|NUMBER|HEX|IDENTIFIER)(RP)(LB)(STATEMENT|IF_STATEMENT)*?(RB)|'
                         '(WHILE)(LP)(E|UE|NUMBER|HEX|IDENTIFIER)(RP)(STATEMENT|IF_STATEMENT|SEMICOLON))', 'STATEMENT', 'WHILE_LOOP', None)

# id = something;
assign_rule = Rule('(IDENTIFIER)(EQUALSIGN)(E|UE|NUMBER|HEX|IDENTIFIER)(SEMICOLON)', 'STATEMENT', 'ASSIGN', None)

# num/id + num/id
add_rule = Rule('(NUMBER|HEX|IDENTIFIER|E)(PLUS)(NUMBER|HEX|IDENTIFIER|E)', 'E', 'E_ADD_RULE', 5)

# num/id & num/id
and_rule = Rule('(NUMBER|HEX|IDENTIFIER|E)(BIT_AND)(NUMBER|HEX|IDENTIFIER|E)', 'E', 'E_AND_RULE', 5)

# num/id | num/id
or_rule = Rule('(NUMBER|HEX|IDENTIFIER|E)(BIT_OR)(NUMBER|HEX|IDENTIFIER|E)', 'E', 'E_OR_RULE', 5)

# num/id ^ num/id
xor_rule = Rule('(NUMBER|HEX|IDENTIFIER|E)(BIT_XOR)(NUMBER|HEX|IDENTIFIER|E)', 'E', 'E_XOR_RULE', 5)

# id ++
post_inc_rule = Rule('(IDENTIFIER)(DOUBLE_PLUS)', 'UE', 'POST_INC_RULE', 20)

# ++ id
pre_inc_rule = Rule('(DOUBLE_PLUS)(IDENTIFIER)', 'UE', 'PRE_INC_RULE', 20)

# id --
post_dec_rule = Rule('(IDENTIFIER)(DOUBLE_MINUS)', 'UE', 'POST_DEC_RULE', 20)

# -- id
pre_dec_rule = Rule('(DOUBLE_MINUS)(IDENTIFIER)', 'UE', 'PRE_DEC_RULE', 20)

# unary operation ;
unary_rule = Rule('(UE)(SEMICOLON)', 'STATEMENT', 'UNARY_RULE', None)

# something == something
rel_equal = Rule('(E|UE|NUMBER|HEX|IDENTIFIER)(EQUALVALUE)(E|UE|NUMBER|HEX|IDENTIFIER)', 'E', 'E_EQUALS_RULE', None)

# something < something
rel_less_than = Rule('(E|UE|NUMBER|HEX|IDENTIFIER)(LESSTHAN)(E|UE|NUMBER|HEX|IDENTIFIER)', 'E', 'E_LESS_THAN', None)

# something > something
rel_greater_than = Rule('(E|UE|NUMBER|HEX|IDENTIFIER)(GREATERTHAN)(E|UE|NUMBER|HEX|IDENTIFIER)', 'E', 'E_GREATER_THAN', None)

# enable interrupt;
enable_interrupt = Rule('(ENABLE)(INTERRUPT)(SEMICOLON)', 'STATEMENT', 'ENABLE_INTERRUPT', None)

# disable interrupt;
disable_interrupt = Rule('(DISABLE)(INTERRUPT)(SEMICOLON)', 'STATEMENT', 'DISABLE_INTERRUPT', None)

# int main() {}
isr_funct = Rule('(ISR_HANDLER)(LP)(RP)(LB)(STATEMENT|IF_STATEMENT)*?(RB)', 'FUNCT_DECLARE', 'ISR', None)

# output(something, somewhere);
port_output = Rule('(OUTPUT)(LP)(IDENTIFIER)(COMMA)(IDENTIFIER)(RP)(SEMICOLON)', 'STATEMENT', 'PORT_OUTPUT', None)
# input(somewhere, something);
port_input = Rule('(INPUT)(LP)(IDENTIFIER)(COMMA)(IDENTIFIER)(RP)(SEMICOLON)', 'STATEMENT', 'PORT_INPUT', None)
# # i = k + l;
# all_ids = Rule('(IDENTIFIER)(EQUALSIGN)(IDENTIFIER)(PLUS)(IDENTIFIER)', 'E', 'E_ALL_IDENTIFIERS', None)

"""
'LESSTHAN', 20),
        ('\<=',                         'LESSTHANEQUAL', 20),
        ('\>',                          'GREATERTHAN', 20),
        ('\<=',                         'GREATERTHANEQUAL', 20),
"""
# Rule('/(TYPE_INT)/'                                       ,'STATEMENT'  ,'MAIN'       , None),

rules = [
    main_funct,
    isr_funct,
    enable_interrupt,
    disable_interrupt,
    int_declare,
    port_declare,
    assign_rule,
    else_statement,
    if_else,
    if_statement,
    for_loop,
    while_loop,
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

'''
Created on Oct 5, 2018

@author: Harrison Fitch
@author: Samuel Poff
'''

class NewCompile(object):
    
        def __init__(self, filename):  
            self.filename = filename
            self.rules = rules = [
    ('\#define',                    'DEFINE', 60),
    ('0[xX][0-9a-fA-F]+',           'HEX', 60),
    ('\d+',                         'NUMBER', 60),
    ('Interrupt_Handler',           'ISR_HANDLER', 60),
    ('interrupt',                   'INTERRUPT', 60),
    ('int',                         'TYPE_INT', 60),
    ('char',                        'TYPE_CHAR', 60),
    ('port',                        'TYPE_PORT', 60),
    ('enable',                      'ENABLE', 60),
    ('disable',                     'DISABLE', 60),
    ('input',                       'INPUT', 60),
    ('output',                      'OUTPUT', 60),
    ('main',                        'MAIN', None),
    ('return',                      'RETURN', 5),
    ('else',                        'ELSE', 10),
    ('if',                          'IF', 10),
    ('for',                         'FOR', 10),
    ('while',                       'WHILE', 10),
    ('define',                      'DEFINE', 60),
    ('[_a-zA-Z][_a-zA-Z0-9]{0,31}', 'IDENTIFIER', 60),
    ('\(',                          'LP', 40),
    ('\)',                          'RP', 40),
    ('\[',                          'LK', 40),
    ('\]',                          'RK', 40),
    ('\{',                          'LB', 60),
    ('\}',                          'RB', 60),
    ('(\-)(\-)',                    'DOUBLE_MINUS', 60),
    ('(\+)(\+)',                    'DOUBLE_PLUS', 60),
    ('\;',                          'SEMICOLON', 70),
    ('\>>',                         'RIGHTSHIFT', 10),
    ('\<<',                         'LEFTSHIFT', 10),
    ('\<=',                         'LESSTHANEQUAL', 20),
    ('\<',                          'LESSTHAN', 20),
    ('\>=',                         'GREATERTHANEQUAL', 20),
    ('\>',                          'GREATERTHAN', 20),
    ('\+',                          'PLUS', 10),
    ('\-',                          'MINUS', 10),
    ('\|',                          'BIT_OR', 10),
    ('\&',                          'BIT_AND', 10),
    ('\^',                          'BIT_XOR', 10),
    ('==',                          'EQUALVALUE', 20),
    ('!=',                          'NOTEQUAL', 20),
    ('=',                           'EQUALSIGN', 30),
    (',',                           'COMMA', 30),
    ]

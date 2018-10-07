    
    
    
def start(self, filename, rules): 
        with open(filename, 'r') as myfile:
            data = myfile.read().replace('\n', '')
#             print( data )
     
        lx = LexBuilder(rules, skip_whitespace=True)
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
#         print(tree)
#         print("\n\n\n\n")
#         print(tree.bracket_repr())
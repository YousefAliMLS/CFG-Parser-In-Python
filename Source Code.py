import collections

class def_init__:
    def __init__(self, grammar_text):
        self.rules = None
        self.start_symbol = None
        self.terminals = None
    def parse(self, text):
        raise NotImplementedError

    def print_info(self):
        raise NotImplementedError

#MEMBER 1: Grammar Structure & Input.
#Aim: Reading the rules, storing them, and identifying terminals.
class Grammar:
 def __init__(self, grammar_text):
        self.rules = collections.defaultdict(list)  
        self.start_symbol = None
        self.terminals = set()
        
if grammar_text:
     self.parse(grammar_text)

def parse(self, text):
        lines = text.strip().split('\n')
        
for line in lines:
     line = line.strip()
     if not line: continue
     if "->" not in line: continue
lhs, rhs = line.split("->")
lhs = lhs.strip()
rhs = rhs.strip()
if self.start_symbol is None:
     self.start_symbol = lhs
     options = rhs.split('|')
for option in options:
     symbols = option.strip().split()
self.rules[lhs].append(symbols)
for s in symbols:
    if not s.isupper():
         self.terminals.add(s)

def print_info(self):
        print(f"The Grammar Start Symbol: {self.start_symbol}")
        print("The Rules:")
for lhs, paths in self.rules.items():
            for path in paths:
                print(f"  {lhs} -> {path}")
print(f"Terminals found: {list(self.terminals)}")




#MEMBER 2: Normalizer (CNF Helper)
#Aim: CYK requires rules to be in specific forms. This part handles.
#helper logic to verify or manage rule formats (Binary or Terminal).

class GrammarNormalizer:




#MEMBER 3: The CYK Algorithm (The Engine).
#Aim: Implementing the dynamic programming table filling logic.

class CYKParser:




#MEMBER 4: Tree visualization and output.
#Aim: Reconstructing the parse tree from the table and printing it.

class TreePrinter:



#if __name__ == "__main__":
    #MEMBER 1 AREA: Define the Grammar ---
    #Beware: For CYK to work easily, use Chomsky Normal Form (A -> BC or A -> a)
    grammar_text = """
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> the | a
    N -> dog | cat
    V -> chased | saw
    """
    
    # Create the Grammar object
    g = Grammar(grammar_text)
    
    # Print the results to verify it works
    g.print_info()

    
   

    #MEMBER 2 AREA: Normalize or check 
    

    #MEMBER 3 AREA: Run parser
   test_string = "the dog chased a cat"
    

    #MEMBER 4 AREA: Output
    

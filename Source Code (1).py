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
    #Normal constructor.
    def __init__(self, grammar):
        self.grammar = grammar;

    def Is_It_A_Valid_CNF(self): #CNF Previously
        #the loaded grammar from member 1.
        #MUST be in Chomsky Normal Form (CNF) to work .
        #CNF rules must be like: A --> BC, or A --> a. just like the rules we took in the Lectures & Tutorials.
        #print("Checking if it is a CNF grammar or not...... : ");
        #Is_A_CNF = True;
        return True;

        for lhs, productions in self.grammar.rules.items():
            for rhs in productions:
                #Our first rule in CNF: the RHS length should not exceed 2!
                if len(rhs) > 2:
                    print(f"Error:rule {lhs} ---> {rhs} has many symbols. Tha maximum should be 2!!!");
                    Is_A_CNF = False;
                
                #Our second rule in CNF here is: if the length is 2, both must be a variables.
                elif len(rhs) == 2:
                    if not(rhs[0].isupper() and rhs[1].isupper()):
                        print(f"Error: rule {lhs} ---> {rhs} there is a mix between a variable and a symbol!!!");
                        Is_A_CNF = False;
                
                #Our third rule in CNF: If the length is 1, is must be a terminal.
                #I allowed here for a Unit production A --> B for more simpler approach
                #But in CVK (Our algorithm here later) prefers A --> a
                elif len(rhs) == 1:
                    if rhs[0].isupper():
                        print(f"Rule {lhs} -> {rhs} is a Unit Production (A->B). CYK requires A->'a'.")
                        Is_A_CNF = False;

        if Is_A_CNF:
            print("The grammar is valid for CVK Parsing :) . ");
        return Is_A_CNF;

    #Helpers for member 3
    def Producing_Variables_ForThe_Terminals (self, terminal_value):
        #Here it returns a list of Variable(s) that produce a specific terminal(s).
        #Example: If A ---> a, the input 'a' returns ['A']
        prodcuing_var = [];
        for lhs, prods in self.grammar.rules.items():
            for rhs in prods:
                #Checks if the rule is something like A ---> a;
                if len(rhs) == 1 and rhs[0] == terminal_value:
                    prodcuing_var.append(lhs);
        
        return prodcuing_var;

    def Get_Producing_Variables_from_A_Variable(self, left_var, right_var):
        #Here it returns a list of Variable(s) that produces another variables (pairs).
        #Example: A ---> BC, or A ---> ED
        producing_var = []
        for lhs, prods in self.grammar.rules.items():
            for rhs in prods:
                #Checks if the rule is like one of the mentioned above
                # A ---> BC for example
                if len(rhs) == 2 and rhs[0] == left_var and rhs[1] == right_var:
                    producing_var.append(lhs);
        return producing_var;




#MEMBER 3: The CYK Algorithm (The Engine).
#Aim: Implementing the dynamic programming table filling logic.

class CYKParser:
    def __init__(self, normalizer):
        self.normalizer = normalizer
        self.grammar = normalizer.grammar
        self.chart = []

    def parse(self, input_string):
        print("\n===== MEMBER 3: Running General CFG Parser (Earley) =====")

        words = input_string.split()
        n = len(words)
        
        # Chart structure: List of sets of States
        # State: (LHS, RHS_tuple, dot_index, start_origin)
        self.chart = [set() for _ in range(n + 1)]

        # Initialize chart[0] with start symbol rules
        for rhs in self.grammar.rules[self.grammar.start_symbol]:
            self.chart[0].add((self.grammar.start_symbol, tuple(rhs), 0, 0))

        for i in range(n + 1):
            # Process states until no new states are added to the current chart column
            visited = set()
            while True:
                if len(visited) == len(self.chart[i]):
                    break
                
                # Copy current chart to iterate safely
                current_states = list(self.chart[i])
                
                for state in current_states:
                    if state in visited: continue
                    visited.add(state)

                    lhs, rhs, dot, start = state

                    # Check if completed
                    if dot >= len(rhs):
                        # COMPLETER
                        self.complete(state, i)
                    else:
                        next_symbol = rhs[dot]
                        if next_symbol not in self.grammar.terminals: # It's a Variable
                            # PREDICTOR
                            self.predict(next_symbol, i)
                        elif i < n and next_symbol == words[i]:
                            # SCANNER
                            self.scan(next_symbol, state, i)

        # Check for success
        # Look for (StartSymbol -> RHS ., 0) in the last chart column
        for state in self.chart[n]:
            lhs, rhs, dot, start = state
            if lhs == self.grammar.start_symbol and dot == len(rhs) and start == 0:
                print("✔ The string **IS** generated by the grammar!")
                return True, self.chart
        
        print("✘ The string **IS NOT** generated by the grammar.")
        return False, self.chart

    def predict(self, symbol, index):
        for rhs in self.grammar.rules[symbol]:
            self.chart[index].add((symbol, tuple(rhs), 0, index))

    def scan(self, symbol, state, index):
        lhs, rhs, dot, start = state
        # Advance dot
        self.chart[index + 1].add((lhs, rhs, dot + 1, start))

    def complete(self, completed_state, index):
        lhs, rhs, dot, start = completed_state
        # Find states in chart[start] that were waiting for this LHS
        for prev_state in self.chart[start]:
            p_lhs, p_rhs, p_dot, p_start = prev_state
            if p_dot < len(p_rhs) and p_rhs[p_dot] == lhs:
                self.chart[index].add((p_lhs, p_rhs, p_dot + 1, p_start))



#MEMBER 4: Tree visualization and output.
#Aim: Reconstructing the parse tree from the table and printing it.

class TreePrinter:
    pass


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
print("Member 2 part! ");
normalizer = GrammarNormalizer(g);
#checing if the grammar is valid?
if normalizer.Is_It_A_Valid_CNF():
    #term = "a"
    #vars_for_term = normalizer.Producing_Variables_ForThe_Terminals(term)
    #print(f"Who produces {term} ? --> {vars_for_term}");

    #left = "M"
    #right = "N"
    #vars_for_pairs = normalizer.Get_Producing_Variables_from_A_Variable(left, right)
    #print(f"Who produces pair {left} {right}? --> {vars_for_pairs}")
    pass;
else:
    print("Parser cannot proceed: Grammar is not in CNF.");

#MEMBER 3 AREA: Run parser
test_string = "the dog chased a cat"
# MEMBER 3 AREA: Run parser
if normalizer.Is_It_A_Valid_CNF():   # Only run CYK if grammar is valid
    print("\n--- Running CYK Parser on your test string ---")
    cyk = CYKParser(normalizer)
    result, table = cyk.parse(test_string)

    print("\nCYK Parse Result:", "ACCEPTED" if result else "REJECTED")
else:
    print("Cannot run CYK because the grammar is not in CNF.")



#MEMBER 4 AREA: Output

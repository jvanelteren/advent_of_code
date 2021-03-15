#%%
def test(s,seq):
    if s == '' or seq == []:
        return s == '' and seq == [] # if both are empty, True. If only one, False.
    
    r = rules[seq[0]]
    if '"' in r:
        if s[0] in r:
            return test(s[1:], seq[1:]) # strip first character
        else:
            return False # wrong first character
    else:
        return any(test(s, t + seq[1:]) for t in r) # expand first term

def parse_rule(s):
    n,e = s.split(": ")
    if '"' not in e:
        e = [[int(r) for r in t.split()] for t in e.split("|")]
    return (int(n),e)

rule_text, messages = [x.splitlines() for x in open("test.txt").read().split("\n\n")]
rules = dict(parse_rule(s) for s in rule_text)            
print("Part 1:", sum(test(m,[0]) for m in messages))       

rule_text += ["8: 42 | 42 8","11: 42 31 | 42 11 31"]
rules = dict(parse_rule(s) for s in rule_text)
print("Part 2:", sum(test(m,[0]) for m in messages)) 
print(rules)
# %%

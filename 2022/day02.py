f = open('day2-input.txt').read()

def p1():
    a = 0
    m = f.strip().split('\n')
    tp = {'X': 1, 'Y': 2, 'Z': 3}
    mp = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
            ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
            ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}
    for e in m:
        opp,you = e.split()
        a += tp[you]
        a += mp[opp,you]
    
    return a

def p2():
    a = 0
    m = f.strip().split('\n')
    mp = {('A', 'X'): (0+3), ('A', 'Y'): (3+1), ('A', 'Z'): (6+2),
         ('B', 'X'): (0+1), ('B', 'Y'): (3+2), ('B', 'Z'): (6+3),
         ('C', 'X'): (0+2), ('C', 'Y'): (3+3), ('C', 'Z'): (6+1)}
    
    for e in m:
        opp,you = e.split()     
        a += mp[opp,you]

    return a

print(p1())
print(p2())

f = open('day1-input.txt').read()

def p1():
    return max(sum(int(c) for c in l.split()) for l in f.split('\n\n'))

def p2():
    a = sorted([sum(int(c) for c in l.split()) for l in f.split('\n\n')], reverse=True)
    return sum(int(c) for c in a[0:3]) 
    
print(p1())
print(p2())

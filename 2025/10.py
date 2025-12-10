from z3 import *




userins = []
while True:
    try:
        s = input()
    except EOFError:
        break 
    
    parts = s.split()
    userins.append(parts)

def to_grid(x,n):
    ans = ''
    for i in range(n):
        if (x>>i)&1:
            ans+='#'
        else:
            ans+='.'
    return ans
def to_move(x):
    ans = []
    for i in range(30):
        if (x>>i)&1:
            ans.append(i)
    return ans
'''
for i in range(len(userins)):
    strgrid = userins[i][0]
    print(f'ith user in is {userins[i]} strgrid is {strgrid}')
    targetstate = 0
    for i1 in range(1,len(strgrid)-1):
        if strgrid[i1]=='#':
            targetstate|=(1<<(i1-1))
    targets.append(targetstate)
    print(f'target is {targetstate} togrid is {to_grid(targetstate,len(strgrid)-2)}')
    
    curmoves = []
    
    for j in range(1,len(userins[i])-1):
        curmove = 0
        clean_tuple = tuple(map(int,userins[i][j].strip("()").split(',')))
        #print(f'cleantuple is {clean_tuple} string version is {userins[i][j]}')
        for x in clean_tuple:
            #print(f'x is {x}')
            curmove|=(1<<x)
        curmoves.append(curmove)
        #print(f'move is {curmove} to tuple is {to_move(curmove)}')
    moves.append(curmoves)
'''


def solve(moves,target):
    initial_state = 0
    visited = set([0])
    q = [[0,0]]
    while q:
        curstate,curdist = q.pop(0)
        if curstate==target:
            return curdist
        for move in moves:
            newstate = curstate^move 
            if newstate not in visited:
                visited.add(newstate)
                q.append((newstate,curdist+1))
    return -1
ans = 0
'''
for i in range(len(userins)):
    print(f'ith target is {targets[i]} ith moves are {moves}')
    curadd=solve(moves[i],targets[i])
    ans+=curadd 
print(ans)
'''

from z3 import *


def solve1(moves,target):
    coeffs = []
    # let n be number of moves, m = len of target
    # then we want 
    n = len(moves)
    m = len(target)

    print(f'moves are {moves} target is {target}')

    print(f'there are {n} moves and target length is {m}')

    coeffs = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        print(f'{i}th move is {moves[i]} type is {type(moves[i])}')
        #curmove = list(map(int,moves[i].strip("()").split(",")))
        for j in moves[i]:
            coeffs[j][i]=1
    
    # now the variables we need to solve for are x_0 ... x_(n-1)
    x = [Int(f'x_{i}') for i in range(n)]

    

    # we also need to minimize the sum of variables 

    # an additional constraint is that each variable must be positive

    opt = Optimize()
    for i in range(n):
        opt.add(x[i] >= 0)      # or > 0 if strict positivity required
    for i in range(m):
        expr = Sum([coeffs[i][j]*x[j] for j in range(n)])
        opt.add(expr == target[i])
    h = opt.minimize(Sum(x))
    # if there is a solution we get the sum of the coefficients
    if opt.check() == sat:
        model = opt.model()
        # lets print out the coefficients for debug purposes
        print('Solution found:')
        for i in range(n):
            print(f'x_{i} = {model.evaluate(x[i])}')
        return model.evaluate(Sum(x)).as_long()
    else:
        return -1
ans = 0
for i in range(len(userins)):
    target_ans = list(map(int,userins[i][-1].strip("{}").split(',')))
    moves = []
    for j in range(1,len(userins[i])-1):
        moves.append(tuple(map(int,userins[i][j].strip("()").split(","))))
    curadd = solve1(moves,target_ans)
    ans+=curadd 
print(ans)


    

'''
from z3 import *

# Variables
x, y, z = Ints('x y z')

# Use Optimize instead of Solver
opt = Optimize()

# Constraints (example)
opt.add(2*x + 3*y == 7)
opt.add(x - z >= 4)
opt.add(x >= 0, y >= 0, z >= 0)

# Add minimization goal
h = opt.minimize(x + y + z)

# Solve
if opt.check() == sat:
    print("Optimal model:", opt.model())
    print("Minimum value:", opt.model().eval(x + y + z))

'''


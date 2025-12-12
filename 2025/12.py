

import sys 
sys.setrecursionlimit(1000000)

grids = []
dims = []
checks = []
idx = -1
while True:
    try:
        s = input()
    except EOFError:
        break 
    if len(s)==0:
        continue
    # find if : is in the string
    if s[-1]==':':
        idx = int(s[:-1])
        grids.append([])
    elif s[0].isdigit():
        dim, nums = s.split(':')
        n,m = map(int,dim.split('x'))
        curcheck = list(map(int,nums.strip().split()))
        checks.append(curcheck)
        dims.append((n,m))
    else:
        grids[idx].append([x for x in s])

def place(grid, piece, x, y):
    n = len(piece)
    m = len(piece[0])
    for i in range(n):
        for j in range(m):
            if piece[i][j] == '#':
                if x+i>=len(grid) or y+j>=len(grid[0]) or grid[x + i][y + j] == '#':
                    return False
    for i in range(n):
        for j in range(m):
            if piece[i][j] == '#':
                grid[x + i][y + j] = '#'
    return True
def unplace(grid, piece, x, y):
    n = len(piece)
    m = len(piece[0])
    for i in range(n):
        for j in range(m):
            if piece[i][j]=='#':
                grid[x+i][y+j]='.'
def backtrack(grid,curcheck,grids,yes):
    if yes[0]:
        return
    zeroflag = True
    for ind in range(len(curcheck)):
        if curcheck[ind]>0:
            zeroflag = False
            # try to place it in the grid 
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    n = len(grids[ind])
                    m = len(grids[ind][0])
                    if place(grid,grids[ind],x,y):
                        curcheck[ind]-=1
                        backtrack(grid,curcheck,grids,yes)
                        curcheck[ind]+=1
                        unplace(grid,grids[ind],x,y)
    if zeroflag:
        yes[0]=True 
        return 

ans = 0
print(f'dims are {dims} checks are {checks}')
print(f'grids are:')
for grid in grids:
    for row in grid:
        print(''.join(row))
    print()
for i in range(len(dims)):
    n,m = dims[i]
    curcheck = checks[i]
    a = 0
    for i1 in range(len(curcheck)):
        cura = sum(sum(1 if x=='#' else 0 for x in row) for row in grids[i1])
        a+=cura*curcheck[i1]
    print(f'for {n} {m} curcheck as {curcheck} a is {a} n*m is {n*m}')
    if n*m>=a:
        ans+=1
print(ans)
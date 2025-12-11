
edges = {}
redges = {}
nodes = set()
# let's really assume this is a dag, and we want to calculate how many paths there are from
# you to out

while True:
    try:
        s = input()
    except EOFError:
        break 

    source, targets = s.split(':')
    nodes.add(source)
    if source not in edges:
        edges[source]=[]
    for t in targets.strip().split():
        nodes.add(t)
        if t not in redges:
            redges[t]=[]
        redges[t].append(source)
        edges[source].append(t)

# the start is you, which is not necessarily degree 0
start = 'you'
end = 'out'

dp = {}
def solve(i,edges,redges,dp,source = None):
    if i in dp:
        return dp[i]
    # otherwise dp[i] = sum of all dp of its children
    if source is not None and i==source:
        dp[i]=1 
        return 1
    elif i not in redges:
        dp[i]=0
        return 0
    ans = 0

    for j in redges[i]:
        addj = solve(j,edges,redges,dp)
        #print(f'there are {addj} ways to get to {j} and they can go to {i}')
        ans+=addj
    #print(f'final count is {ans} for {i}')
    dp[i]=ans 
    return dp[i]

def dfs(i,visited):
    visited.add(i)
    if i not in edges:
        return 
    for j in edges[i]:
        if j not in visited:
            dfs(j,visited)
def dfs1(i,visited,edges,redges,dp):
    visited.add(i)
    dp[i] = solve(i,edges,redges,dp,source = start)
    
    if i not in edges:
        return 
    for j in edges[i]:
        if j not in visited:
            dfs1(j,visited,edges,redges,dp)




'''
part1
visited = set()
dfs(start,visited)

newedges = {}
newredges = {}
for node in visited:
    if node in edges:
        newedges[node] = [x for x in edges[node]]
    if node in redges:
        newredges[node] = [x for x in redges[node]]


dfs1(start,set(),newedges,newredges,dp)
dfs1(start,set(),newedges,newredges,dp)
print(f'final dp is {dp}')
print(f'{dp[end]}')
'''

'''
part2 
now you can go from 
sver -> dac -> fft -> out
sver -> fft -> dac -> out

these are possible combos:
sver -> dac dp1
sver -> fft dp2
dac -> fft dp3
fft -> dac dp4
dac -> out dp4
fft -> out dp6

therefore ans = dp1[dac]*dp3[fft]*dp6[out] + dp2[fft]*dp4[dac]*dp5[out]
'''

ans_vars = [-1 for _ in range(6)]
starts = ['svr','svr','dac','fft','dac','fft']
ends = ['dac','fft','fft','dac','out','out']

for i in range(6):
    
    start = starts[i]
    end = ends[i]
    #print(f'on {start} -> {end}')
    visited = set()
    dfs(start,visited)

    newedges = {}
    newredges = {}
    for node in visited:
        if node in edges:
            newedges[node] = [x for x in edges[node]]
        if node in redges:
            newredges[node] = [x for x in redges[node]]
    

    dp = {}
    dfs1(start,set(),newedges,newredges,dp)
    ans_vars[i]=dp[end] if end in dp else 0
    #print(f'dp is {dp}\n\n\n')
print(ans_vars[0]*ans_vars[2]*ans_vars[5] + ans_vars[1]*ans_vars[3]*ans_vars[4])


        
        

    
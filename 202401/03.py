p,q,r,m = [int(x) for x in input().split()]
n = p+q+r
data = [0]+[int(x) for x in input().split()]+[0]*(q+r)
gate = [0]*(p+1)+[int(x) for x in input().split()]+[0]*r
depth = [0]*(n+1)
pred = [[] for i in range(n+1)]
succ = [[] for i in range(n+1)]
for i in range(m):
    u,v = [int(x) for x in input().split()]
    succ[u].append(v)
    pred[v].append(u)
# find topological sort
indeg = [len(pred[v]) for v in range(n+1)]
seq = list(range(1,p+1))
head = 0
while head < len(seq):
    v = seq[head]; 
    head += 1
    for u in succ[v]:
        what = indeg[u]
        indeg[u] -= 1
        if indeg[u] == 0:
            seq.append(u)
# find max depth
for v in seq[p:]: # ignore input nodes
    depth[v] = max(depth[c] for c in pred[v])+1
print(max(depth[p+q+1:])-1) # -1 for output gate
# find data
for v in seq[p:]: # ignore input nodes
    if gate[v] == 1:
        fitst_part = data[pred[v][0]]
        second_part = data[pred[v][1]]
        data[v] = data[pred[v][0]] & data[pred[v][1]]
    elif gate[v] == 2: 
        fitst_part = data[pred[v][0]]
        second_part = data[pred[v][1]]
        data[v] = data[pred[v][0]] | data[pred[v][1]]
    elif gate[v] == 3:
        fitst_part = data[pred[v][0]]
        second_part = data[pred[v][1]]
        data[v] = data[pred[v][0]] ^ data[pred[v][1]]
    elif gate[v] == 4:
        fitst_part = data[pred[v][0]]
        data[v] = 1-data[pred[v][0]]
    else: # output
        fitst_part = data[pred[v][0]]
        data[v] = data[pred[v][0]] 
#
print(*data[p+q+1:])
# Not my code
# testing https://codeforces.com/contest/580/submission/55056991 code
# with my bootstraped recursion
 
# My magical way of doing recursion in python. This
# isn't the fastest, but at least it works.

#for each function call
#for each return statement yield should used
from types import GeneratorType
def bootstrap(func, stack=[]):
    def wrapped_function(*args, **kwargs):
        if stack:
            return func(*args, **kwargs)
        else:
            call = func(*args, **kwargs)
            while True:
                if type(call) is GeneratorType:
                    stack.append(call)
                    call = next(call)
                else:
                    stack.pop()
                    if not stack:
                        break
                    call = stack[-1].send(call)
            return call
 
    return wrapped_function
 
@bootstrap
def go_child(node, path_cat, parent):
    # check if too more cat
    m_cat = 0
    if cat[node] == 0:
        m_cat = 0
    else:
        m_cat = path_cat + cat[node]
    # too many cats
    if m_cat > m:
        yield 0
    isLeaf = True
    sums = 0
    # traverse edges belongs to node
    for j in e[node]:
        # ignore parent edge
        if j == parent:
            continue
        # node has child
        isLeaf = False
        # dfs from child of node
        sums += yield go_child(j, m_cat, node)
    # achievable leaf
    if isLeaf:
        yield 1
    # return achievable leaves count
    yield sums
 
 
n, m = map(int, input().split())
cat = list(map(int, input().split()))
e = [[] for i in range(n)]
 
for i in range(n - 1):
    v1, v2 = map(int, input().split())
    # store undirected edge
    e[v1 - 1].append(v2 - 1)
    e[v2 - 1].append(v1 - 1)
# dfs from root
print(go_child(0, 0, -1))
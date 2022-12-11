def dfs(vec, vis, node, compSize):
    vis[node] = True
    compSize[0] += 1
    for x in vec[node]:
        if not vis[x]:
            dfs(vec, vis, x, compSize)


def minimumSwaps(a, n):
    aux = [*enumerate(a)]
    aux.sort(key=lambda it: it[1])
    vis = [False] * (n + 1)
    vec = [[] for i in range(n + 1)]
    for i in range(n):
        vec[aux[i][0] + 1].append(i + 1)
    ans = 0
    for i in range(1, n + 1):
        compSize = [0]
        if not vis[i]:
            dfs(vec, vis, i, compSize)
            ans += compSize[0] - 1
    return ans

list =[1,4,3,2,5,8,9,6]
print(minimumSwaps(list,8))
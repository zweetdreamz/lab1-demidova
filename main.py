n = 7
ar = [[0] * n for i in range(n)]
arr = list(map(float, input().split(" ")))

for i in range(n):
    ar[i][0] = arr[i]
    for j in range(n):
        if i == j:
            ar[i][j] = 1
    ar[0][i] = 1 / ar[i][0]

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == j:
            continue
        else:
            ar[i][j] = ar[0][j]/ar[0][i]

[[print("%.2f" % (ar[i][j]), end=' ') if j != n-1 else print("%.2f" % (ar[i][j])) for j in range(n)] for i in range(n)]
print("-"*40)
[print("%.2f" % i, end=' ') for i in [1/sum([ar[i][j] for i in range(n)]) for j in range(n)]]
print("\nПроверка степеней принадлежности(сумма)", sum([1/sum([ar[i][j] for i in range(n)]) for j in range(n)]))

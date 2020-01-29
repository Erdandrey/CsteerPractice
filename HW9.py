problem6 = sum([x for x in range(1, 101)])*sum([x for x in range(1, 101)]) - sum([x*x for x in range(1, 101)])
problem9 = [a*b*c for a in range(1, 500) for b in range(a, 500) for c in range(1, 500)
            if (a+b+c == 1000) and (a*a + b*b == c*c)]
problem48 = sum(a**a for a in range(1, 1000)) % 10000000000
s = ''.join([str(x) for x in range(1, 100000)])
t = 1
problem40 = 1
for x in range(0, len(s)):
    if x == t-1:
        problem40 = problem40*int(s[x])
        t = t*10
print(problem6)
print(problem9[0])
print(problem48)
print(problem40)

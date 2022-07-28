n = input()
m = int(input())
x = n[len(n)-m:]
fib_series = [int(dig) for dig in x]
while (fib_series[-1])<int(x):
    term = sum(fib_series[len(fib_series)-m:])
    fib_series.append(term)
if fib_series[-1]==int(x):
    print("Generated")
else:
    print("Cannot be generated")

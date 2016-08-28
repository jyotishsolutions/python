def fib(n):
	a=1
	b=1
        result = []
	while b < n:
                result.append(b)
		a=b
		b=a+b
        return result

fib_result=fib(100)
print fib_result

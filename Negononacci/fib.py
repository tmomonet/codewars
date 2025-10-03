def fib(n: int) -> int:
    def fib_pair(k):
        # Returns (F(k), F(k+1))
        if k == 0:
            return (0, 1)
        a, b = fib_pair(k // 2)
        c = a * ((b << 1) - a)       # F(2k)
        d = a * a + b * b            # F(2k+1)
        return (c, d) if k % 2 == 0 else (d, c + d)

    if n >= 0:
        return fib_pair(n)[0]
    else:
        f = fib_pair(-n)[0]
        return -f if n % 2 == 0 else f

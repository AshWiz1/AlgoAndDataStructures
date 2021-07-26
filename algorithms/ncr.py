def ncr(n, r):
    # initialize numerator
    # and denominator
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % MOD
        den = (den * (i + 1)) % MOD
    return (num * pow(den,
                      MOD - 2, MOD)) % MOD


def invfact(num):
    return pow(num, MOD-2, MOD)

fact = [0]*(n+1)
fact[0] = 1
for i in range(1, n+1):
    fact[i] = (fact[i-1]*i)%MOD
    inv[i] = invfact(fact[i])

def ncr(n, r):
    return ( ( ( (fact[n] * inv[n-r]) % MOD ) * inv[r] ) %MOD )



def sign(u, k):
    u_int = int(u, 2)
    k_int = int(k, 2)
    s_u = sum_digits(u_int)
    s_k = sum_digits(k_int)
    s = s_u * s_k
    t = str(bin(s))[2:]
    return u, t

def sum_digits(n):
    n = str(n)
    s_n = 0
    for i in n:
        s_n += int(i)
    return s_n    

def verify(x, k, t):
    _, t_prime = sign(x, k)
    return t == t_prime

def task_1(u, k):
    x, t = sign(u, k)
    print(verify(x, k, t))

def task_2(u, k):
    u, t = sign(u, k)
    u_int = str(int(u, 2))
    u_fake = int(u_int[::-1])
    u_fake_bin = str(bin(u_fake))[2:]
    print(f"Il messaggio è {u_fake_bin}|{t}")
    print(f"Il messaggio è accettato? {verify(u_fake_bin, k, t)}") 

def task_3(l):
    freq = {}
    for i in range(2**l):
        s = sum_digits(i)
        if s in freq:
            freq[s] += 1
        else:
            freq[s] = 1
        

def main():
    task_1('100011', '1001110')
    task_2('100011', '1001110')

if __name__ == "__main__":
    main()
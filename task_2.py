def substitution_attack(u):
    u_fake_int = str(int(u,2)*10)
    u_fake_bin = str(bin(int(u_fake_int)))[2:]
    return u_fake_bin

def task_2(u, k):    
    u, t = sign(u, k)
    
    #attack ---
    
    u_fake_bin = substitution_attack(u)
    #end of attack ---
    print(f"Il messaggio è {u_fake_bin}|{t}")
    print(f"Il messaggio è accettato? {verify(u_fake_bin, k, t)}") 

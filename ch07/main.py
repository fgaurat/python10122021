def main():
    a = 2
    b = 3
    c = a/b

    r = f"résultat de {a} / {b} =  {c:.2%}"
    print(r)
    
    r = "résultat de {0:-3}/{1:-3} = {2:.2%}".format(a,b,c)
    print(r)
    s = """
    toto
    titi
    """
    print(repr(s))
    print(50*'-')
    l = ["valeur 1","valeur 2","valeur 3"]

    r= f"values  v1 = {l[0]}, v2 = {l[1]}, v3 = {l[2]}"
    r = "values  v1 = {}, v2 = {}, v3 = {}".format(*l)
    print(r)
    print(50*'-')
    l = {"key1":"valeur 1","key2":"valeur 2","key3":"valeur 3"}
    r= f"values v1 = {l['key1']}, v2 = {l['key2']}, v3 = {l['key3']}"
    print(r)
    r = "values v1 = {k1}, v2 = {k2}, v3 = {k3}".format(k1=l['key1'],k2=l['key2'],k3=l['key3'])
    print(r)
    r = "values v1 = {key1}, v2 = {key2}, v3 = {key3}".format(**l)
    print(r)

    r = f"valeur : {l['key1']:>19} la suite"
    print(r)




if __name__ == '__main__':
    main()
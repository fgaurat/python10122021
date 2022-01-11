


l = ["valeur 1","valeur 2","valeur 3","valeur 2","valeur 1"]
s = {"valeur 1","valeur 2","valeur 3","valeur 2","valeur 1"}
t = "valeur 1","valeur 2","valeur 3","valeur 2","valeur 1"


if "valeur 2" in l and "valeur 3" in l:
    print("ok list")

if "valeur 2" in s:
    print("ok set")

if "valeur 2" in t:
    print("ok tuple")
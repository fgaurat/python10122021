import traceback

from DivBy12Error import DivBy12Error




def division(a, b):
    
    if b == 12:
        # raise ArithmeticError('Division par 12 !')
        err = DivBy12Error()
        raise err
    c = a/b
    
    return c

def call_division(a, b):
    c = None
    try:
        c = division(a, b)
    # except:
    #     print("Erreur dans call_division !")
    #     raise    
    finally:
        print("finally fin call_division")
    
    return c


def main():
    try:
        a = 2
        b = 12

        # b = int(input("valeur de b:"))
        # c = a/b
        # c=division(a,b)

        c = call_division(a, b)

        print("c",c)

    except ZeroDivisionError as e:
        print("ZeroDivisionError!")
        print(type(e))
        print(e)
        print(50*'-')
        traceback.print_exc()
        print(50*'-')
    except ValueError as e:
        print("ValueError!")
        print(type(e))
        print(e)
        print(50*'-')
        traceback.print_exc()
        print(50*'-')
    except Exception as e:
        print("Exception!")
        print(type(e))
        print(e)
        print(50*'-')
        traceback.print_exc()
        print(50*'-')
    else:
        print("else")
    finally:
        print("finally")
    print("fin")


if __name__ == '__main__':
    main()

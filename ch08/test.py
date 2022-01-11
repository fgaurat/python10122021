import traceback

# ordre : main appelle --> call_division qui appelle --> division --> retourne à call_division --> retroune à main
def division(a, b):
    c = a/b

    return c


def call_division(a, b):
    c = None
    try:
        c = division(a, b)
    # except:
    #     print(f"Erreur call_division !!!")
    #     print(f"fin call_division")
    #     # 0 division error = raise
    #     raise
    
    #finally = exécuter du code, qu’il y ait erreur ou pas
    finally:
        print(f"finally fin call_division !!")

    return c


def main():
    # code susceptible de générer une erreur => l’essayer :
    # (logique = faire un gros block try, +sieurs blocks except pr chaque erreur)
    try:
        a = 2

        # b = 0
        # si on tape b = 0, on provoquera l’erreur
        # pb : si je saisis une lettre, j’aurai une autre erreur => je dosi la gérer aussi
        b = int(input("Saisir la valeur de b :"))

        c = call_division(a, b)
        # le print n’est pas exécuté après l’erreur => le code s’interromp
        print(f"c : {c}")

    # Note : les blocks except = exécutés dans l’ordre => je vais du plus précis au + global
    except ZeroDivisionError as e:
        print("Erreur de division par zéro !!! :")
        print(type(e))
        print(e)
        print(50*'-')
        # (optionnel : traceback = afficher l’exception sur l’erreur en cours => donner + d’info que l’erreur par défaut)
        traceback.print_exc()
    # si je tape une lettre :
    except ValueError as e:
        print("Erreur de value !!! :")
        print(type(e))
        print(e)
        print(50*'-')
        # (optionnel : traceback = afficher l’exception sur l’erreur en cours => donner + d’info que l’erreur par défaut)
        traceback.print_exc()
    except Exception as e:
        print("Erreur générique !!! :")
        print(type(e))
        print(e)
        print(50*'-')
        # (optionnel : traceback = afficher l’exception sur l’erreur en cours => donner + d’info que l’erreur par défaut)
        traceback.print_exc()
    else:
        print("else !!!")
    finally:
        print("finally !!!")

    # à partir du moment où je gère une erreur dans un block except, le code continue à être exécuté => "fin" s’affiche
    print("fin")


if __name__ == '__main__':
    main()
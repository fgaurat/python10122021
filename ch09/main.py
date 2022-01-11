

from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from ch09.ICalcGeo import ICalcGeo


def show_surface(o:ICalcGeo):
    print(o)
    print(o.surface)

def main():
    r = Rectangle(2,6)
    c = Carre(2)
    ce = Cercle(2)

    print(ce)
    print(ce.surface)
    print("cote",c.cote)
    print("surface",c.surface)
    c.cote= 12
    print("surface",c.surface)
    print("cote",c.cote)

    s = str(c)
    print(s)

    show_surface(r)
    show_surface(c)
    show_surface(ce)


def main_rectangle():

    r= Rectangle(1,2)
    print(Rectangle.get_cpt())
    r1= Rectangle(1,2)
    print(Rectangle.get_cpt())
    
    # if r.__eq__(r1):
    if r == r1:
        print("ok")
    else:
        print("ko")

    print(r.longueur)
    
    r.longueur = 12
    print(r.longueur)

    surface = r.surface
    print(surface) # 24

    print(r)
    print(r1)

    l = [r,r1]
    for obj in l:
        print(obj)

    print("fin")

if __name__ == '__main__':
    main()
import math

def Menu ():
        print("Wpisz 1 aby obliczyć pole kwadratu")
        print("Wpisz 2 aby obliczyć pole prostokątu")
        print("Wpisz 3 aby obliczyć pole trójkąta")
        print("Wpisz 4 aby obliczyć pole trapezu")
        print("Wpisz 5 aby obliczyć pole koła")
        print("Wpisz 6 aby zakończyć")

def powrót ():
    Menu()
    print()
    wart()

def kwadrat (a):
    return a * a

def prostokąt (a, b):
    return a * b

def trójkąt (a, h):
    return (a * h) / 2

def trapez (a, b, h):
    return ((a+b) * h) / 2

def koło(r):
    return math.pi * r**2

def wart ():
    c = input("Wybierz opcję: ")
    if (c == '1'):
        a = input("Wpisz długosc boku: ")
        a = int(a)
        wynik = kwadrat(a)
        print(wynik)
        print()
        w = input("Wpisz 1 aby wrócić do menu ")
        if (w == '1'):
            print()
            return powrót()
        else:
            quit()
            
    elif (c == '2'):
        a = input("Wpisz długosc 1 boku: ")
        a = int(a)
        b = input("Wpisz długosc 2 boku: ")
        b = int(b)
        wynikP = prostokąt(a, b)
        print(wynikP)
        print()
        w = input("Wpisz 1 aby wrócić do menu ")
        if (w == '1'):
            print()
            return powrót()
        else:
            quit()
        
    elif(c == '3'):
        a = input("Wpisz długosc boku: ")
        a = int(a)
        h = input("Wpisz długosc wysokosci: ")
        h = int(h)
        wynikT = trójkąt(a, h)
        print(wynikT)
        print()
        w = input("Wpisz 1 aby wrócić do menu ")
        if (w == '1'):
            print()
            return powrót()
        else:
            quit()
    
    elif(c == '4'):
        a = input("Wpisz długosc 1 podstawy: ")
        a = int(a)
        b = input("Wpisz długosc 2 podstawy: ")
        b = int(b)
        h = input("Wpisz długosc wysokosci: ")
        h = int(h)
        wynikTr = trapez(a, b, h)
        print(wynikTr)
        print()
        w = input("Wpisz 1 aby wrócić do menu ")
        if (w == '1'):
            print()
            return powrót()
        else:
            quit()
        
    elif(c == '5'):
        r = input("Wpisz długosc promienia ")
        r = int(r)
        wynikK = koło(r)
        print(wynikK)
        print()
        w = input("Wpisz 1 aby wrócić do menu ")
        if (w == '1'):
            print()
            return powrót()
        else:
            quit()
    
    elif(c =='6'):
        quit()

    else:
        quit()

print(powrót())

















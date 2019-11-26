# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computer_v1.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmartins <mmartins@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/31 17:04:09 by mmartins          #+#    #+#              #
#    Updated: 2019/02/01 17:10:35 by mmartins         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys


def solve_degres_1(b, c):
    #x1 = c / b
    x1 = float(c) / float(b)
    # print("\033[32m[================= SOLUTION =================]\033[37m")
    # print("La solution à l'équation est : {}.".format(round(x1, 2)))
    result = "[================= SOLUTION =================]\n\nLa solution à l'équation est : {}.".format(round(x1, 2))
    return result
        
def solve_null(a, b, delta):
    #x1 = -b / 2*a
    x1 = (-float(b)) / (2 * float(a))
    # print("\033[32m[================= SOLUTION =================]\033[37m")
    # print("La solution à l'équation est : {}.".format(round(x1, 2)))
    result = "[================= SOLUTION =================]\n\nLa solution à l'équation est : {}.".format(round(x1, 2))
    return result


def solve_positiv(a, b, delta):
    #x1 = -b - racine_carre(delta) / 2 * a
    #x2 = -b + racine_carre(delta) / 2 * a
    x1 =  (-float(b) - rsquare(delta)) / (2 * float(a))
    x2 =  (-float(b) + rsquare(delta)) / (2 * float(a))
    # print("\033[32m[================= SOLUTION =================]\033[37m")
    # print("Les solution à l'équation sont : {} et {}".format(round(x1, 2), round(x2, 2)))
    result = "[================= SOLUTION =================]\n\nLes solution à l'équation sont : {} et {}".format(round(x1, 2), round(x2, 2))
    return result


def rsquare(nb):
    nb = nb**0.5
    return nb


def square(nb):
    nb = nb * nb
    return nb

def delta(a, b, c):
    # discriminant = delta = b^2 - 4 ac
    b = square(float(b))
    delta = b - 4 * float(a) * float(c)
    return delta


def first_part(equation_0):
    # ax2 + bx + c
    # a*x^2 + b*x^1 + c*x^0
    equation_0 = equation_0.split(' ')
    a = '0'
    b = '0'
    c = '0'
    d = '0'
    degres = 0
    x = ['X^0', 'X^1', 'X^2', '-', '+', '*', '/']
    for i in range(0, len(equation_0)):
        print(equation_0[i])
        if equation_0[i] == '-':
            equation_0[i+1] = '-'+equation_0[i+1]
        if equation_0[i] == 'X^0':
            if c != '':
                c = str(float(c) + float(equation_0[i -2]))
            else:
                c = equation_0[i - 2]
        if equation_0[i] == 'X^1':
            if b != '':
                b = str(float(b) + float(equation_0[i -2]))
            else:
                b = equation_0[i - 2]
        if equation_0[i] == 'X^2':
            if a != '':
                a = str(float(a) + float(equation_0[i -2]))
            else:
                a = equation_0[i - 2]
        if len(equation_0[i]) >= 3 and equation_0[i].lstrip('-').replace(".", "", 1).isdigit() == False and equation_0[i] not in x:
            if equation_0[i] == 'X^3':
                if d != '':
                    d = str(float(d) + float(equation_0[i -2]))
                else:
                    d = equation_0[i - 2]
                degres = 3
                return a, b, c, degres, d
    if a == '0':
        degres = 1
    else:
        degres = 2
    return a, b, c, degres, d


def seconde_part(equation_0, equation_1):
    second = equation_1.strip().split(' ')
    second[0] =  -1 * int(second[0])
    equation_0 += ' + '+ str(second[0])
    for i in range(1, len(second)):
        equation_0 += ' '+str(second[i])
    return equation_0


def equal_solution():
    # print("\033[32m[================= FORME RÉDUITE =================]\033[37m \n0 = 0")
    # print("Le discriminant est 0.")
    # print("\033[32m[================= SOLUTION =================]\033[37m")
    # print("Tous les nombres réels")
    result = "[================= FORME RÉDUITE =================]\n\n0 = 0\nLe discriminant est 0.\n[================= SOLUTION =================]\nTous les nombres réels"
    return result


def compute(equation):
    # equation = input("Entrez votre équation :")
    try:
        equation = equation.split("=", 1)
        if equation[0].strip() == '0':
            equation[0] = equation[1].strip()
            equation[1] = '0'
        if equation[0].strip() == equation[1].strip():
            result = equal_solution()
            return result
        if equation[1].strip() != '0':
            equation[0] = seconde_part(equation[0], equation[1])
            equation[1] = ' 0'
    except:
        # print("\033[91mPolynôme Error: Le format de votre polynôme n'est pas correct.\033[0m")
        result = "Polynôme Error: Le format de votre polynôme n'est pas correct."
        return result

    a, b, c, degres, d = first_part(equation[0])
    result = ""
    print("degres = ",degres)
    if degres > 2:
        result += "Ce polynôme est d'un degrés supérieur à 2. Je ne peux pas le résoudre, désolé.\n"
        return result
    elif degres == 2:
        # print("\033[32m[================= FORME RÉDUITE =================]\033[37m\n{}x^2 + {}x^1 + {} ={}".format(a, b, c, equation[1]))
        result += "[================= FORME RÉDUITE =================]\n\n{}x^2 + {}x^1 + {} ={}\n".format(a, b, c, equation[1])
    elif degres == 1:
        # print("\033[32m[================= FORME RÉDUITE =================]\033[37m\n{}x^1 + {} ={}".format(b, c, equation[1]))
        result += "[================= FORME RÉDUITE =================]\n\n{}x^1 + {} ={}\n".format(b, c, equation[1])

    # print("L'équation est de degrés {}.".format(degres))
    result += "\nL'équation est de degrés {}.\n".format(degres)
    
    discriminant = delta(a, b, c)
    if discriminant < 0 and degres == 2:
        # print("\033[91mLe discriminant est strictement négatif. Il n'y a donc pas de solution pour cette équation.\033[0m")
        result += "Le discriminant est strictement négatif. Il n'y a donc pas de solution pour cette équation.\n"
        return result
    elif discriminant == 0 and degres == 2:
        result += solve_null(a, b, discriminant)
        return result
    elif discriminant > 0 and degres == 2:
        result += solve_positiv(a, b, discriminant)
        return result
    elif degres == 1:
        result += solve_degres_1(b, c)
        return result
    else:
        # print("\033[91mCe polynôme est d'un degrés supérieur à 2. Je ne peux pas le résoudre, désolé.\033[0m")
        result += "Ce polynôme est d'un degrés supérieur à 2. Je ne peux pas le résoudre, désolé.\n"
        return result


# if __name__ == "__main__":
#     # pygame.init()
#     # fenetre = pygame.display.set_mode((640,480), RESIZABLE)
#     # fond = pygame.image.load("background.jpeg").convert()
#     # fenetre.blit(fond, (0,0))
#     # pygame.display.flip()
#     # continuer = 1
#     # while continuer:
#     #     continuer = int(input())
#     main()




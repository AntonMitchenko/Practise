import exp_root.exponentiation
import exp_root.root
import factorial.factorial
import logarithm.logarithm
print('You use a not very reliable but very funny calculator '
      'from Anton to calculate the factorial, 2nd and 3rd roots and different'
      ' logarithms (ordinary natural ones and with a base of 10)')
main_menu_print = """
To perform the desired action, write the number under which your function is located:

* factorial - 1
* square root - 2
* root of the third degree - 3
* square number - 4
* third degree - 5
* logarithm base 10 - 6
* natural logarithm - 7
* logarithm - 8

Please, choose ur option:
"""


def checker(a):
    n = input('Write ur number (int format) \n')
    try:
        n = int(n)
    except:
        print('The value you entered is incorrect')
        return checker(a)
    if '1' == a and n < 0 or '2' == a and n < 0 or '3' == a and n < 0:
        print('The value you entered is incorrect')
        return checker(a)
    if '8' == a and n < 0:
        print('The value you entered is incorrect')
        return checker(a)
    return n


def chek_for8(a):
    b = input('Write ur 2 number (int format) \n')
    try:
        b = int(b)
    except:
        print('The value you entered is incorrect')
        return chek_for8(a)
    if b <= 1:
        print('The value you entered is incorrect')
        return checker(a)
    return b


def main(a):
    if '1' == a:
        print(f'U found factorial\n{factorial.factorial.fact(checker(a))}')
    elif '2' == a:
        print(f'U found square root\n{exp_root.root.root2(checker(a))}')
    elif '3' == a:
        print(f'U found root of the third degree\n{exp_root.root.root3(checker(a))}')
    elif '4' == a:
        print(f'U found square number\n{exp_root.exponentiation.exp2(checker(a))}')
    elif '5' == a:
        print(f'U found third degree\n{exp_root.exponentiation.exp3(checker(a))}')
    elif '6' == a:
        print(f'U found logarithm base 10\n{logarithm.logarithm.lg(checker(a))}')
    elif '7' == a:
        print(f'U found natural logarithm\n{logarithm.logarithm.ln(checker(a))}')
    elif '8' == a:
        print(f'U found  logarithm\n{logarithm.logarithm.log(checker(a), chek_for8(a))}')


if __name__ == '__main__':
    restart = ""
    while not restart == "-":
        is_correct = ''
        while not is_correct == '+':
            main_menu_select = input(main_menu_print)
            if main_menu_select != '[1-8]':
                restart = ""
            main(main_menu_select)
            break
        restart = ""
        while not (restart == "+") | (restart == "-"):
            restart = input("Do you want to repeat the operation (+/-):\n")
            if restart == "+":
                print("Start the program again\n")
            elif restart == "-":
                print("Thanks for using")
            else:
                print("The value you entered is incorrect")

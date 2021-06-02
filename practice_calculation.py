import random
import math
import sys


# 1  : Squares
# 2 : Cubes
# 3 : multiplication
# 4 : fraction value
# 5 : Percentage value
# 6 : addition of 2 digit numbers
# 7 : addition 3 digit numbers
# 8 : Factorial
# 9 : Percentage-Fraction conversion

percent_frac = [("25", "1/4"),("50", "1/2"),("75", "3/4"),("33.334","1/3"),("66.667", "2/3"),("20","1/5"),("40","2/5"),("60","3/5"),("80","4/5"),
         ("16.667","1/6"),("83.334","5/6"),("14.28","1/7"),("28.56","2/7"),("12.5","1/8"),("37.5","3/8"),("62.5","5/8"),("87.5","7/8"),
         ("11.11","1/9"),("22.22","2/9"),("44.44","4/9"),("9.09","1/11"),("18.18","2/11"),("7.7","1/13"),("7.14","1/14"),("6.67","1/15"),
         ("6.25","1/16"),("5.88","1/17"),("5.55","1/18"),("5.25","1/19"),("5","1/20"),("4.75","1/21"),("4.54","1/22"),("4.35","1/23"),
         ("4.16","1/24"),("4","1/25"),("3.84","1/26"),("3.703","1/27"),("3.45","1/29")]

def main():
    test_type = int(input("Do you want to do specific testing or random testing.\nEnter 1 for specific 0 for random : "))
    f = [squares, cubes, mul, fraction, percentage, add2digit, add3digit, fact, percentage_fraction_conversion]
    if test_type == 1:
        print("Enter the kind of testing you wish to do \n \
              # 1  : Squares \n \
              # 2 : Cubes \n \
              # 3 : multiplication \n \
              # 4 : fraction value \n \
              # 5 : fraction value to percentage \n \
              # 6 : addition of 2 digit numbers \n \
              # 7 : addition 3 digit numbers \n \
              # 8 : Factorial \n \
              # 9 : Percentage-Fraction conversion")

        ops = int(input("Enter Choice : "))

        while True:
            f[ops-1]()
            print()

    else:
        while True:
            ops = random.randint(1, 9)
            f[ops]()

def squares():

    num = random.randint(11,30)
    print("the square of {} is ".format(num))
    input()
    print(num**2)

def cubes():

    num = random.randint(2, 30)
    print("the cube of {} is ".format(num))
    input()
    print(num ** 3)

def mul():

    num1 = random.randint(2, 20)
    num2 = random.randint(2,20)
    print("the multiplication of {}*{} is ".format(num1,num2))
    input()
    print(num1*num2)

def fraction():

    num = random.randint(2,30)
    cal = 1/num
    print("Value of 1/{} is ".format(num))
    input()
    print("{:.3f}".format(cal))

def percentage():

    num = random.randint(2, 30)
    cal = 1 / num
    print("Percentage of 1/{} is ".format(num))
    input()
    print("{:.3f}%".format(cal*100))

def add2digit():
    num1 = random.randint(11, 99)
    num2 = random.randint(11, 99)
    print("the addition of {}+{} is ".format(num1, num2))
    input()
    print(num1 + num2)

def add3digit():
    num1 = random.randint(101, 999)
    num2 = random.randint(101, 999)
    print("the addition of {}+{} is ".format(num1, num2))
    input()
    print(num1 + num2)

def fact():
    num = random.randint(3, 10)
    print("factorial of {} is ".format(num))
    input()
    print(math.factorial(num))

def percentage_fraction_conversion():

    num = random.randint(0,len(percent_frac)-1)
    t = percent_frac[num]
    percent = t[0]
    frac = t[1]
    if num&2 == 0:

        print("Convert percentage {}% to fraction ".format(percent))
        input()
        print(frac)
    else:
        print("Convert fraction {} to percentage ".format(frac))
        input()
        print("{}%".format(percent))


if __name__ == '__main__':
    main()

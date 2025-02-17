#Artem Mochuliak
#17/02/2025
#a program that checks if number is perfect




from divisors import divisors


def perfectNumber(num):
    is_perfect = False
    


    list = []

    list = divisors(num)
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
        

    if(sum == num):
        is_perfect = True

      
    return is_perfect


def main():
    if (perfectNumber(8128)):
        print("8128 is a perfect number")



main()



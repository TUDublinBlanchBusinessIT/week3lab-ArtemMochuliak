#Artem Mochuliak
#17/02/2025
#a progarm with function divisors and returns a list of all the divisors(factors) of that that number



def divisors(num):
    list = []

   
    for i in range(1,num):
        if(num%i == 0):
            list.append(i)

     
    return list        



def main():
    print(divisors(30))


main()


    

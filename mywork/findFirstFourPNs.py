#Artem Mochuliak
#17/02/2025
#a program here that finds the first four perfect numbers.




from perfectNumber import perfectNumber

totalPF = 0

testnum = 1


while(totalPF < 4):
    if(totalPF == 4):
        break
    if(perfectNumber(testnum) == True):
       print(f"{testnum} is a perfect number") 
       totalPF+=1

    testnum += 1









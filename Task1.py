#Задана натуральная степень k. 
#Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени 
import random
def create_equ ():
    result = ''
    k = int (input("Введите максимальную степень многочлена "))
    equ = {}
    equ[k] = random.randint(1,100)
    result=str(equ[k])+"*x**"+str(k)
    for i in range (k-1,-1,-1):
        equ[i] = random.randint(0,100)
        if equ[i] > 0:
            if i == 1:
                 result+= "+" + str(equ[i])+"*x"
            elif i == 0:
                result+= "+" + str(equ[i])
            else:
                result+= "+"+ str(equ[i])+"*x**"+ str(i)
    result += " = 0" 
    return result
filename = 'file1.txt'
with open (filename,'w') as file_object:
    file_object.write(create_equ())
with open (filename,'r') as file_object:
    line1 = file_object.read()    
print('Результат записан в файл file1.txt')
print("Полученный многочлен:")
print(line1)



 

 
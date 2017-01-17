# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:35:59 2017

@author: fexun
"""

import time
t0 = time.time()

dic = {0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta', 80: 'oitenta', 90: 'noventa', 100: 'cento', 200: 'duzentos', 300: 'trezentos', 400: 'quatrocentos', 500: 'quinhentos', 600: 'seiscentos', 700: 'setecentos', 800: 'oitocentos', 900: 'novecentos', 1000: 'mil' }

def extenso():
        
    x = input('Digite um número: ')
    
    x = int(x)
    x = str(x)
    
    fun = lambda x:dic[x]

    if x.isdigit == False:
        print('O número não pode ser uma letra')
        extenso()

    if int(x) > 1000 or int(x) < -1000:
        print('O número precisa ter valor absoluto menos ou igual a 1000')
        extenso()
            
    tam = len(x)
    
    if int(x) >= 0:
    
        if tam == 4:
            return print(dic[int(x)])
    
        elif tam == 3:
            
            if int(x[1]) != 0 and int(x[2]) != 0:
                aux = list(map(fun, [int(x[0])*100, int(x[1])*10, int(x[2])]))
                return print('{} e {} e {}'.format(aux[0], aux[1], aux[2]))
        
            elif int(x[1]) == 0 and int(x[2]) != 0:
                aux = list(map(fun, [int(x[0])*100, int(x[2])]))
                return print('{} e {}'.format(aux[0], aux[1]))
            
            elif int(x[1]) != 0 and int(x[2]) == 0:
                aux = list(map(fun, [int(x[0])*100, int(x[1])]))
                return print('{} e {}'.format(aux[0], aux[1]))
                
            else:
                aux = list(map(fun, [int(x[0])*100]))
                if aux[0] == 'cento':
                    return print('cem')
                else:
                    return print('{}'.format(aux[0]))
           
        elif tam == 2:
            
            if int(x[1]) != 0:
                aux = list(map(fun, [int(x[0])*10, int(x[1])]))
                return print('{} e {}'.format(aux[0], aux[1]))
                
            else:
                aux = list(map(fun, [int(x[0])*100]))
                return print('{}'.format(aux[0]))
                
        else:
            if int(x[1]) != 0 and int(x[2]) != 0:
                aux = list(map(fun, [int(x[0])]))
                return print('{}'.format(aux[0]))
'''            
    else:
        
        if tam == 4:
            return print('menos', dic[x])
    
        elif tam == 3:
            aux = list(map(fun, [int(x[0])*100, int(x[1])*10, int(x[2])]))
            return print('menos {} e {} e {}'.format(aux[0], aux[1], aux[2]))
        
        elif tam == 2:
            aux = list(map(fun, [int(x[0])*10, int(x[1])]))
            return print('menos {} e {}'.format(aux[0], aux[1]))
            
        else:
            aux = list(map(fun, [int(x[0])]))
            return print('menos {}'.format(aux[0]))
'''            
        
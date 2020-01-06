import math

while True:
  print('#############################')
  print('#  calculo areas e volumes  #')
  print('#############################\n')
  print('1.  circulo')
  print('2.  triangulo')
  print('3.  trapezio')
  print('4.  retangulo')
  print('5.  paralelepipedo')
  print('6.  piramide')
  print('7.  esfera')
  print('8.  tetraedro')
  print('9.  icosaedro')
  print('10. cone ')
  print('11. tronco do cone ')
  print('12. sair \n')
  f = input('opçao: ')
  print('\n')
#circulo

  if f == '1':  
    r = int(input('qual o raio: '))
    a = 3.14 * (r * r)
    p = 2 * 3.14 * r
    print('perimetro: ',p,'\narea: ',a,'\n\n\n')


#triangulo
  if f == '2':
    b = int(input('qual e a base: '))
    h = int(input('qual e a altura: '))
    a = (b * h) / 2
    p = math.sqrt(b * b + h * h) + h + b)
    print('perimetro: ',p,'\narea: ',a,'\n\n\n')


#trapezio 
  if f == '3':  
    B = int(input("qual e a base maior: "))
    b = int(input("qual e a base menor: "))
    h = int(input("qual e a altura: "))
    a = (B + b) * h /2
    p = b + B + h + math.sqrt(b - B + h * h)
    print ("perimetro: ",a,"\narea: ",p,'\n\n\n')


#retangulo 
  if f == '4':
    b = int(input('qual e a base: '))
    l = int(input('qual e a altura: '))
    a = b * l
    p = b + l + b + l
    print('perimetro: ',p,'\narea: ',a,'\n\n\n')


#paralelepido
  if f == '5':  
    al =int(input('qual e a altura: '))
    b = int(input('qual e a base: '))
    c = int(input('qual e o comprimento: '))
    v = c * b * al
    a = 2 * (al * b + b * c + al * c)
    print('volume: ',v,'\narea: ',a,'\n\n\n')


#piramide
  if f == '6':  
    ar =int(input('qual e a aresta: '))
    ap = int(input('qual e a apotema: '))
    ab = ar * ar
    at = 2 / ar * ap 
    v = 1/3 * ab * at
    a = ab + at * 4
    print('volume: ',v,'\narea: ',a,'\n\n\n')


#esfera
  if f == '7':  	
    r = int(input('qual e o raio: '))
    v = 4 * 3.14 *(r * r * r) / 3 
    a =  4 * 3.14 * (r * r) 
    print('volume: ',v,'\narea: ',a,'\n\n\n')


#tetraedro
  if f == '8':  
    a = int(input('qual e a aresta: '))
    h = (a * a) * math.sqrt(6) / 3 
    s1 = (a * a)*math.sqrt(3) / 4
    ar = s1 * 4
    v =  1/3 * s1 * h   
    print('volume: ',v,'\narea: ',ar,'\n\n\n')


#icosaedro
  if f == '9':  
    ar = int(input('qual e a aresta: '))
    v = 5/12 * (3 + math.sqrt(5)) * 3 *(ar*ar*ar)
    a =  5 * math.sqrt(3) * (ar * ar)
    print('volume: ',v,'\narea: ',a,'\n\n\n')


#cone
  if f == '10':  
    r = int(input('qual e o raio: '))
    h = int(input('qual e a altura: '))

    g = math.sqrt(r * r + h * h)
    Ab = 3.14 * r * r
    Al = 3.14 * r * g    
    v = 3.14 * (r * r) * h / 3
    a = 3.14 * r * (g + r)  
    print('volume: ',v,'\narea: ',a,'\n\n\n')

#tronco de cone
  if f == '11':  
    r = int(input('qual e o raio da base menor: '))
    R = int(input('qual e o raio da base maior: '))
    g = int(input('qual e a geratriz: '))
    
    AB = 3.14 * r * r
    Al = 3.14 * g * (r + R)
    Ab = 3.14 * r * r
    v = 3.14 * h /3 * (R*2 + R * r +r*2)
    a = AB + Ab + Al  
    print('volume: ',v,'\narea: ',a,'\n\n\n')


#sair
  if f == '12':
    exit(1)

  else:
    print('\nERRO(numero invalido)\n')
    break

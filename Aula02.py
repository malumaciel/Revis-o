num = int(input("Digite um número: "))
if num>0:
   if num%2==0:
       print(f"{num} é par e positivo:")
   else:
       print(f"{num} é impar e positivo:")
else:
    if num%2==0:
        print(f"{num} é par e negativo:")
    else:
        print(f"{num} é impar e negativo:")

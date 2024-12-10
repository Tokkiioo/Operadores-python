numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

igual = numero1 == numero2
diferente = numero1 != numero2
menor_que = numero1 < numero2
menor_igual_que = numero1 <= numero2
mayor_que = numero1 > numero2
mayor_igual_que = numero1 >= numero2

print("Primer numero es Igual a Segundo numero: ",igual)
print("Primero numero es Diferente a segundo numero: ",diferente)
print("Primer numero es Menor que segundo numero: ",menor_que)
print("Primer numero es Menor o igual que segundo numero: ",menor_igual_que)
print("Primer numero es Mayor que segundo numero: ",mayor_que)
print("Primer numero es Mayor o igual que segundo numero: ",mayor_igual_que)
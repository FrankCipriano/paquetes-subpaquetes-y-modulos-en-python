#-IMPORTANDO PAQUETES CON SUS MODULOS
import paquete_phyton.funciones_matematicas as fmath
import paquete_phyton.funciones_cadena as fString
#-IMPORTANDO UN SUB-PAQUETE CON SUS MODULOS
import paquete_phyton.sub_paquete.saludo as fs

print('FrankDev\n\n')
print(f'Potencia: {fmath.potenciar(3,3)}')
print(f'Tamaño: {fString.contar("Hola Mundo")}')
print(f'Multiplicacion: {fmath.multiplicar(4,5)}')
print(f'Divison: {fmath.dividir(8,0)}')
print(f'Presentacion: {fs.Saludo("Frank")}')
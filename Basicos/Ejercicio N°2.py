# Solicita al usuario su nombre y edad, y después imprime ambos en la pantalla.

# Creamos las variables
nombre = input("Ingrese el nombre: ") # input() -> Sirve para ingresar datos por teclado, como parametros se puede dejar un string el cual se va a imprimir en consola. El dato que se ingrese se considera tipo string.
edad = int(input("Ingrese la edad: ")) # Anteponiendo el tipo de dato, se parsea el valor ingresado en el input. En este caso el input ingresado se parsea con un valor tipo 'int'.

# Imprimimos el mensaje
print(f"{nombre} - {edad} años") # Indicar f antes de un string nos permite que al insertar llaves podamos ingresar variables de una forma mas dinamica.
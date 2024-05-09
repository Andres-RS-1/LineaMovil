#_______ POO _______
print(" _______ POO _______ ")

# Definir una clase para representar una línea móvil
class LineaMovil:
    def __init__(self, numero):
        self.numero = numero  # Asignar un número de línea móvil al objeto
        self.llamadas_nacionales = []  # Inicializar una lista vacía para llamadas nacionales
        self.llamadas_internacionales = []  # Inicializar una lista vacía para llamadas internacionales

    def agregar_llamada_nacional(self, tiempo):
        costo_por_minuto = 500  # Definir el costo por minuto para llamadas nacionales
        costo_total = tiempo * costo_por_minuto  # Calcular el costo total de la llamada
        self.llamadas_nacionales.append(costo_total)  # Agregar el costo total a la lista de llamadas nacionales

    def agregar_llamada_internacional(self, tiempo):
        costo_por_minuto = 1000  # Definir el costo por minuto para llamadas internacionales
        costo_total = tiempo * costo_por_minuto  # Calcular el costo total de la llamada
        self.llamadas_internacionales.append(costo_total)  # Agregar el costo total a la lista de llamadas internacionales

    def costo_total_nacional(self):
        return sum(self.llamadas_nacionales)  # Calcular y devolver el costo total de todas las llamadas nacionales

    def costo_total_internacional(self):
        return sum(self.llamadas_internacionales)  # Calcular y devolver el costo total de todas las llamadas internacionales

    def costo_total_general(self):
        return self.costo_total_nacional() + self.costo_total_internacional()  # Calcular y devolver el costo total general

# Función para obtener la entrada del usuario para una llamada
def obtener_tiempo_llamada(tipo_llamada, numero_llamada):
    tiempo = float(input(f"Duración de llamada {tipo_llamada} {numero_llamada} (minutos): "))  # Solicitar la duración de la llamada al usuario
    return tiempo  # Devolver el tiempo ingresado por el usuario

# Crear dos líneas móviles
linea1 = LineaMovil(1)  # Crear la primera línea móvil con número 1
linea2 = LineaMovil(2)  # Crear la segunda línea móvil con número 2

# Solicitar información para la primera línea móvil
print(f"Línea móvil {linea1.numero}")  # Imprimir el número de la primera línea móvil
num_llamadas_nacionales = int(input("Número de llamadas nacionales: "))  # Solicitar al usuario el número de llamadas nacionales
num_llamadas_internacionales = int(input("Número de llamadas internacionales: "))  # Solicitar al usuario el número de llamadas internacionales

# Iniciar un bucle para ingresar la duración de cada llamada nacional
for i in range(1, num_llamadas_nacionales + 1):
    tiempo = obtener_tiempo_llamada("nacional", i)  # Llamar a la función para obtener el tiempo de la llamada
    linea1.agregar_llamada_nacional(tiempo)  # Llamar al método de la línea móvil para agregar la llamada nacional

# Iniciar un bucle para ingresar la duración de cada llamada internacional
for i in range(1, num_llamadas_internacionales + 1):
    tiempo = obtener_tiempo_llamada("internacional", i)  # Llamar a la función para obtener el tiempo de la llamada
    linea1.agregar_llamada_internacional(tiempo)  # Llamar al método de la línea móvil para agregar la llamada internacional

# Solicitar información para la segunda línea móvil
print(f"Línea móvil {linea2.numero}")  # Imprimir el número de la segunda línea móvil
num_llamadas_nacionales = int(input("Número de llamadas nacionales: "))  # Solicitar al usuario el número de llamadas nacionales
num_llamadas_internacionales = int(input("Número de llamadas internacionales: "))  # Solicitar al usuario el número de llamadas internacionales

# Iniciar un bucle para ingresar la duración de cada llamada nacional para la segunda línea móvil
for i in range(1, num_llamadas_nacionales + 1):
    tiempo = obtener_tiempo_llamada("nacional", i)  # Llamar a la función para obtener el tiempo de la llamada
    linea2.agregar_llamada_nacional(tiempo)  # Llamar al método de la línea móvil para agregar la llamada nacional

# Iniciar un bucle para ingresar la duración de cada llamada internacional para la segunda línea móvil
for i in range(1, num_llamadas_internacionales + 1):
    tiempo = obtener_tiempo_llamada("internacional", i)  # Llamar a la función para obtener el tiempo de la llamada
    linea2.agregar_llamada_internacional(tiempo)  # Llamar al método de la línea móvil para agregar la llamada internacional

# Calcular y mostrar los costos totales para la primera línea móvil
print(f"Costo total de llamadas nacionales para la línea {linea1.numero}: ${linea1.costo_total_nacional()}")
print(f"Costo total de llamadas internacionales para la línea {linea1.numero}: ${linea1.costo_total_internacional()}")
print(f"Costo total de todas las llamadas para la línea {linea1.numero}: ${linea1.costo_total_general()}")

# Calcular y mostrar los costos totales para la segunda línea móvil
print(f"Costo total de llamadas nacionales para la línea {linea2.numero}: ${linea2.costo_total_nacional()}")
print(f"Costo total de llamadas internacionales para la línea {linea2.numero}: ${linea2.costo_total_internacional()}")
print(f"Costo total de todas las llamadas para la línea {linea2.numero}: ${linea2.costo_total_general()}")
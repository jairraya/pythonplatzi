class Vehiculo:
  def __init__(self, precio, marca, modelo):
    self.precio = precio
    self.marca = marca
    self.modelo = modelo
    self.disponible = True
    
  def comprar_vehiculo(self):
    self.disponible = False

class Persona:
  def __init__(self,Nombre,Cedula):
    self.Nombre = Nombre
    self.Cedula = Cedula
    self.VehiculosComprados = []
    
  def comprar_vehiculo(self,vehiculo,consecionario,pago):
    if pago >= vehiculo.precio:
      print (f"\nEl vehiculo {vehiculo.marca} ha sido comprado por  el usuario {self.Nombre}")
      vehiculo.comprar_vehiculo()
      consecionario.ventaVehiculo(vehiculo)
      consecionario.verVehiculos()
    else:
      print (f"\nEl pago dado por el usuario {self.Nombre} es Insuficuente")

      print("\n")


class Consecionario:
  def __init__(self):
    self.Usuarios = []
    self.Vehiculos = []
    
  def agregarUsuarios(self, usuario):
    self.Usuarios.append(usuario)
    print(f"El usuario {usuario.Nombre} fue agregado a la base de datos")

  print("\n")

  def agregarVehiculo(self, vehiculo):
    self.Vehiculos.append(vehiculo)
    print(f"El vehiculo {vehiculo.modelo} de la marca {vehiculo.marca} fue agregado a la base de datos")

  print("\n")

  def ventaVehiculo (self, vehiculo):
    self.Vehiculos.remove(vehiculo)

  print("\n")

  def verVehiculos (self):
    print("\nLos vehiculos disponibles son:")
    for vehicle in self.Vehiculos:
      if vehicle.disponible:
        print(f"{vehicle.marca}")

#Crear Vehiculos

Ferrari = Vehiculo(100000,"Ferrari",2020)
Ford = Vehiculo(10000,"Ford",2010)
Nissan = Vehiculo(1000,"Nissan",2006)
Ferrari_Jaguar = Vehiculo(100000,"Ferrari Jaguar",2020)
Ford_Raptor = Vehiculo(10000,"Ford Raptor",2010)
Nissan_nitro = Vehiculo(1000,"Nissan nitro",2006)

#Crear Uusraios

Pablo = Persona("Pablo","1")
Natalia = Persona("Natalia","2")
Jose = Persona("Jose","3")
Maria = Persona("Maria","4")
Beatriz = Persona("Beatriz","5")

#Crear Consecionario

consecionario = Consecionario()

#Agregar Usuarios y Vehiculos

consecionario.agregarVehiculo(Ferrari)
consecionario.agregarVehiculo(Ford)
consecionario.agregarVehiculo(Nissan)
consecionario.agregarVehiculo(Ferrari_Jaguar)
consecionario.agregarVehiculo(Ford_Raptor)
consecionario.agregarVehiculo(Nissan_nitro)

consecionario.agregarUsuarios(Pablo)
consecionario.agregarUsuarios(Natalia)
consecionario.agregarUsuarios(Jose)
consecionario.agregarUsuarios(Maria)
consecionario.agregarUsuarios(Beatriz)

#Ver Vehiculos

consecionario.verVehiculos()

#Comprar y Venta

Pablo.comprar_vehiculo(Ferrari_Jaguar,consecionario,10000)
Pablo.comprar_vehiculo(Ferrari_Jaguar,consecionario,100000)
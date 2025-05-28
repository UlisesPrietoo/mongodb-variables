from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv('MONGO_URI')

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Conexión
db = client["Ejercicios"]
usuarios_collection = db["usuarios"]
ordenes_collection = db["ordenes"]
empleados_collection = db["empleados"]
clientes_collection = db["clientes"]
ventas_collection = db["ventas"]

usuarios = []
ordenes = []
empleados = []
clientes = []
ventas = []

# def crear_usuarios():
#     global usuarios
#     usuarios = [
#         {
#             "nombre": "Ana Díaz",
#             "direccion": {
#                 "ciudad": "Santiago",
#                 "calle": "Av. Providencia 123"
#             }
#         },
#         {
#             "nombre": "Mario Torres",
#             "direccion": {
#                 "ciudad": "Valparaíso",
#                 "calle": "Calle Condell 55"
#             }
#         }
#     ]
#     usuarios_collection.insert_many(usuarios)
#     print("Usuarios creados y guardados en la base de datos.")

# def crear_ordenes():
#     global ordenes
#     ordenes = [
#         {
#             "cliente": "Luis Rojas",
#             "productos": [
#                 { "nombre": "Teclado", "precio": 25 },
#                 { "nombre": "Monitor", "precio": 200 }
#             ]
#         },
#         {
#             "cliente": "Carla Méndez",
#             "productos": [
#                 { "nombre": "Mouse", "precio": 15 },
#                 { "nombre": "Impresora", "precio": 120 }
#             ]
#         }
#     ]
#     ordenes_collection.insert_many(ordenes)
#     print("Órdenes creadas y guardadas en la base de datos.")

# def crear_empleados():
#     global empleados
#     empleados = [
#         {
#             "nombre": "Valentina Campos",
#             "historial": [
#                 { "cargo": "Asistente", "año": 2018 },
#                 { "cargo": "Gerente", "año": 2021 }
#             ]
#         },
#         {
#             "nombre": "David Soto",
#             "historial": [
#                 { "cargo": "Técnico", "año": 2019 },
#                 { "cargo": "Supervisor", "año": 2022 }
#             ]
#         },
#         {
#             "nombre": "Elena Muñoz",
#             "departamento": {
#                 "nombre": "IT",
#                 "salario": 1200
#             }
#         },
#         {
#             "nombre": "Jorge Castro",
#             "departamento": {
#                 "nombre": "Ventas",
#                 "salario": 1300
#             }
#         }
#     ]
#     empleados_collection.insert_many(empleados)
#     print("Empleados creados y guardados en la base de datos.")

# def crear_clientes():
#     global clientes
#     clientes = [
#         {
#             "nombre": "Pedro Salinas",
#             "facturas": [
#                 { "numero": 101, "monto": 300 },
#                 { "numero": 102, "monto": 750 }
#             ]
#         },
#         {
#             "nombre": "Rosa Pérez",
#             "facturas": [
#                 { "numero": 201, "monto": 150 },
#                 { "numero": 202, "monto": 180 }
#             ]
#         },
#         {
#             "nombre": "Sofía Herrera",
#             "empresa": "Empresa A",
#             "facturas": [
#                 { "monto": 800 },
#                 { "monto": 1200 }
#             ]
#         },
#         {
#             "nombre": "Pablo Núñez",
#             "empresa": "Empresa B",
#             "facturas": [
#                 { "monto": 2000 }
#             ]
#         }
#     ]
#     clientes_collection.insert_many(clientes)
#     print("Clientes creados y guardados en la base de datos.")

# def crear_ventas():
#     global ventas
#     ventas = [
#         {
#             "cliente": "Andrés Silva",
#             "productos": [
#                 { "nombre": "Tablet", "precio": 150 },
#                 { "nombre": "Laptop", "precio": 850 }
#             ]
#         },
#         {
#             "cliente": "Camila Ríos",
#             "productos": [
#                 { "nombre": "Tablet", "precio": 200 }
#             ]
#         }
#     ]
#     ventas_collection.insert_many(ventas)
#     print("Ventas creadas y guardadas en la base de datos.")

# crear_usuarios()
# crear_ordenes()
# crear_empleados()
# crear_clientes()
# crear_ventas()



#Ejercicio 1 (Buscar usuarios por su ciudad almacenada en un subdocumento)
resultado = usuarios_collection.find({
    "$or": [
        { "direccion.ciudad": { "$regex": "Santiago", "$options": "i" } },
        { "direccion.ciudad": { "$regex": "Valparaíso", "$options": "i" } }
    ]
})

for usuario in resultado:
    print(usuario)


#Ejercicio 2 (Buscar órdenes que contengan productos con un nombre específico)
resultado = ordenes_collection.find({
    "$or": [
        { "productos.nombre": { "$regex": "Teclado", "$options": "i" } },
        { "productos.nombre": { "$regex": "monitor", "$options": "i" } },
        { "productos.nombre": { "$regex": "mouse", "$options": "i" } },
        { "productos.nombre": { "$regex": "Impresora", "$options": "i" } }
    ]
})

for ordenes in resultado:
    print(ordenes)

# Ejercicio 3 (Encontrar empleados con cargo 'Gerente' en su historial laboral)
resultado = empleados_collection.find({
    "historial.cargo": { "$regex": "Gerente", "$options": "i" }
})

for empleados in resultado:
    print(empleados)

#Ejercicio 4 (Obtener clientes con al menos una factura mayor a $500)
resultado = clientes_collection.find({
    "facturas": { "$elemMatch": { "monto": { "$gt": 500 } } }
}, {
    "facturas": {
        "$elemMatch": { "monto": { "$gt": 500 } }
    }
})

for cliente in resultado:
    print(cliente)

#Ejercicio 5 (Buscar empleados con un salario mayor a $1000 y que trabajen en 'IT')
resultado = empleados_collection.find({
    "departamento.nombre": "IT",
    "departamento.salario": { "$gt": 1000 }
})

for empleado in resultado:
    print(empleado)

#Ejercicio 6 (Encontrar documentos con al menos un producto que cumpla dos condiciones a la vez)
resultado = ventas_collection.find({
    "productos": {
        "$elemMatch": {
            "nombre": "Tablet",
            "precio": { "$gt": 150 }
        }
    }
})

for venta in resultado:
    print(venta)

#Ejercicio 7 (Mostrar solo los nombres de productos de una orden)
resultado = ordenes_collection.find(
    {},
    { "productos.nombre": 1, "_id": 0 } 
)

# Mostrar los resultados
for orden in resultado:
    print(orden)

#Ejercicio 8 (Encontrar clientes de 'Empresa A' que tengan una factura mayor a $1000)
resultado = clientes_collection.find({
    "empresa": "Empresa A",
    "facturas": {
        "$elemMatch": {
            "monto": { "$gt": 1000 }
        }
    }
})

for cliente in resultado:
    print(cliente)




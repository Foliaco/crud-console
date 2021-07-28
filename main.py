from DB import select,insert,delete,update
from colorama import Fore,Style
print('welcome to my CRUD')
print('Please enter a option\n')

print("1. Select items")
print("2. Insert items")
print("3. Update items")
print("4. Delete items")
opts=[1,2,3,4]
op=int(input())

if op in opts:
    if op==1:
        select()

    if op==2:
        name=input("Producto: ")
        precio=int(input("Precio: "))
        cantidad=int(input("Cantidad: "))        
        insert([name,precio,cantidad])

    if op==3:
        print("Ingresa los nuevos datos")
        nombre=input("nombre: ")
        precio=int(input("precio: "))
        cantidad=int(input("cantidad: "))
        print("ahora el ID del producto")
        id=int(input())
        update([nombre,precio,cantidad,id])
    
    if op==4:
        print(Fore.RED+"Usted quiere eliminar")
        print(Style.RESET_ALL+"Enter id product")
        id=int(input())
        delete(id)

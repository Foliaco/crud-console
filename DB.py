import mysql.connector
from colorama import Fore,Style

conex=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="root",
        db="productos"
        )
cur=conex.cursor()

def select():
    sql="select * from productos"
    cur.execute(sql)

    for product in cur.fetchall():
        print("Id: ",product[0])
        print("Product: "+product[1])
        print("Precie: "+str(product[2]))
        print("Quantity: "+str(product[3]))
        print(Fore.BLUE+"__________________________________")
        print(Style.RESET_ALL+"")

def insert(data):
    sql="insert into productos values(null,%s,%s,%s)"
    try:
        cur.execute(sql,data)
        conex.commit()
        print(cur.rowcount,"Insertado correctament")
    except Exception as e:
        raise

def delete(id):
    sql="delete from  productos where id_producto={}".format(id)
    try:
        cur.execute(sql,id)
        conex.commit()
        if cur.rowcount==1:
            print("Eliminado correctamente")
        else:
            print("No hay un elemento con id: ",id)
    except Exception as e:
        raise


def update(newValues):
    sql="update productos set nombre=%s, precio=%s, cantidad=%s where id_producto=%s"
    try:
        cur.execute(sql,newValues)
        conex.commit()
        if cur.rowcount==1:
            print("Actualizado correctamente")
        else:
            print("No hay un elemento con el ID"+str(cur.rowcount())+" que actualizar")
    except Exception as e:
        raise

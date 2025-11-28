import csv
import unicodedata
import os


def quitar_tildes(texto):
    if texto is None:
        return None
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


traducciones = {
    "Delivery": "Domicilio",
    "Take Away": "Para llevar",
    "Salad": "Ensalada",
    "Pasta": "Pasta",
    "Pizza": "Pizza",
    "Chicken": "Pollo",
    "Soup": "Sopa",
    "Beverage": "Bebida",
    "Hot": "Caliente",
    "Cold": "Frio",
    "paid": "pagado",
    "waiter": "camarero",
    "unit_price": "precio_unitario",
    "quantity" : "cantidad",
    "category" : "categoria",
    "dish_name" : "nombre_del_plato",
    "channel" : "canal",
    "table" : "mesa",
    "orden_table" : "fecha_del_pedido",
    "order_id" : "id_del_pedido"




}


def traducir(texto):
    if texto is None:
        return None
    for eng, esp in traducciones.items():
        texto = texto.replace(eng, esp)
    return texto



def limpiar_csv(archivo_original):
    nombre, ext = os.path.splitext(archivo_original)
    archivo_limpio = f"{nombre}_limpio{ext}"

    with open(archivo_original, "r", encoding="utf-8") as file_in, \
        open(archivo_limpio, "w", encoding="utf-8", newline="") as file_out:

        reader = csv.reader(file_in)
        writer = csv.writer(file_out)

        for fila in reader:
            nueva_fila = []
            for campo in fila:

                
                if campo.strip().upper() == "NA":
                    nueva_fila.append("None")
                    continue

            
                campo = quitar_tildes(campo)

                
                campo = traducir(campo)

                nueva_fila.append(campo)

            writer.writerow(nueva_fila)

    print("✔ Proceso completado.")
    print(f"📄 Archivo limpio creado como: {archivo_limpio}")



limpiar_csv(r"C:\Users\Aprendiz\Downloads\josephsanchez\restaurante\dataset6_restaurant_orders.csv")


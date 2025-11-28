import csv

class ControladorRestaurante:
    def __init__(self, archivo):
        self.pedidos = []
        self.cargar_csv(archivo)

    def cargar_csv(self, archivo):
        with open(archivo, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                # Convertimos algunos valores numéricos
                fila["order_id"] = int(fila["order_id"])
                fila["quantity"] = int(fila["quantity"])
                fila["unit_price"] = float(fila["unit_price"])
                fila["total"] = float(fila["total"])
                self.pedidos.append(fila)

    def listar_pedidos(self):
        print(" Lista de Pedidos ")
        for p in self.pedidos:
            print(p)

    def filtrar_por_categoria(self):
        print(" Filtrar por Categoría ")
        categoria = input("Ingrese categoría: ").lower()

        resultado = [p for p in self.pedidos if p["category"].lower() == categoria]

        if not resultado:
            print("No hay pedidos para esa categoría.")
        else:
            for p in resultado:
                print(p)

    def total_por_mes(self):
        print(" Total Vendido por Mes ")
        totales = {}

        for p in self.pedidos:
            fecha = p["order_date"]  
            mes = int(fecha.split("-")[1])  

            totales[mes] = totales.get(mes, 0) + p["total"]

        for mes, valor in totales.items():
            print(f"Mes {mes}: ${valor}")

    def ventas_por_mesero(self):
        print("\n--- Ventas por Mesero ---")
        totales = {}

        for p in self.pedidos:
            mesero = p["waiter"]
            totales[mesero] = totales.get(mesero, 0) + p["total"]

        for m, valor in totales.items():
            print(f"{m}: ${valor}")

    def buscar_pedido(self):
        print(" Buscar Pedido por ID ")
        try:
            order_id = int(input("Ingrese ID del pedido: "))
        except:
            print("ID inválido.")
            return

        for p in self.pedidos:
            if p["order_id"] == order_id:
                print("Pedido encontrado:")
                print(p)
                return

        print("No se encontró un pedido con ese ID.")
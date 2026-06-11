from decimal import Decimal
from productos.models import Producto  # cambia "productos" por el nombre real de tu app


# =========================
# CREATE - Crear productos
# =========================

productos_data = [
    {
        "nombre": "Notebook Lenovo ThinkPad",
        "descripcion": "Notebook empresarial para desarrollo y oficina.",
        "precio": Decimal("899990.00"),
    },
    {
        "nombre": "Mouse Logitech MX Master",
        "descripcion": "Mouse inalámbrico ergonómico de alta precisión.",
        "precio": Decimal("79990.00"),
    },
    {
        "nombre": "Monitor Samsung 24 pulgadas",
        "descripcion": "Monitor Full HD ideal para trabajo y estudio.",
        "precio": Decimal("129990.00"),
    },
]

for data in productos_data:
    producto, creado = Producto.objects.get_or_create(
        nombre=data["nombre"],
        defaults={
            "descripcion": data["descripcion"],
            "precio": data["precio"],
        }
    )

    if creado:
        print(f"Producto creado: {producto}")
    else:
        print(f"Producto ya existía: {producto}")


# =========================
# READ - Leer productos
# =========================

print("\nListado de productos:")
productos = Producto.objects.all()

for producto in productos:
    print(
        f"ID: {producto.id} | "
        f"Nombre: {producto.nombre} | "
        f"Precio: ${producto.precio}"
    )


# =========================
# READ ONE - Buscar uno
# =========================

producto = Producto.objects.filter(nombre="Notebook Lenovo ThinkPad").first()

if producto:
    print("\nProducto encontrado:")
    print(producto.id, producto.nombre, producto.descripcion, producto.precio)


# =========================
# UPDATE - Actualizar producto
# =========================

producto = Producto.objects.filter(nombre="Notebook Lenovo ThinkPad").first()

if producto:
    producto.precio = Decimal("849990.00")
    producto.descripcion = "Notebook empresarial actualizado con mejor precio."
    producto.save()
    print(f"\nProducto actualizado: {producto.nombre} - ${producto.precio}")


# =========================
# DELETE - Eliminar producto
# =========================

producto = Producto.objects.filter(nombre="Mouse Logitech MX Master").first()

if producto:
    producto.delete()
    print("\nProducto eliminado: Mouse Logitech MX Master")


# =========================
# READ FINAL - Ver resultado final
# =========================

print("\nProductos finales en la base de datos:")

for producto in Producto.objects.all():
    print(
        f"ID: {producto.id} | "
        f"{producto.nombre} | "
        f"{producto.descripcion} | "
        f"${producto.precio}"
    )
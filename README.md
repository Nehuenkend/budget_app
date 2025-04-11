# 💸 App de Presupuesto en Python

Este proyecto simula una aplicación de gestión de presupuesto personal mediante programación orientada a objetos. Permite registrar depósitos, retiros y transferencias entre categorías, y genera un gráfico de barras de los porcentajes de gasto por categoría.

---

## 📌 Objetivos del Proyecto

- Practicar conceptos fundamentales de **POO en Python**.
- Simular un sistema básico de presupuesto.
- Implementar una visualización textual del gasto por categoría.

---

## 🧰 Características

### ✅ Clase `Category`
- Crea una categoría de presupuesto (como "Alimentación", "Transporte", etc).
- Permite realizar:
  - `deposit()`: Añadir dinero a la categoría.
  - `withdraw()`: Retirar dinero si hay fondos suficientes.
  - `transfer()`: Transferir fondos a otra categoría.
  - `get_balance()`: Consultar el saldo actual.
  - `check_funds()`: Verificar si hay suficiente saldo.
  - Representación amigable con `__str__()`.

### 📊 Función `create_spend_chart()`
- Genera un gráfico de barras en consola que muestra el porcentaje de gasto por categoría.

---

## 🧪 Ejemplo de Uso

```python
food = Category("Alimentación")
clothing = Category("Ropa")
entertainment = Category("Ocio")

food.deposit(1000, "Depósito inicial")
food.withdraw(150.75, "Compra supermercado")
clothing.deposit(500)
clothing.withdraw(200, "Zapatos")
entertainment.deposit(300)
entertainment.withdraw(120, "Cine")

food.transfer(50, entertainment)

print(food)
print(create_spend_chart([food, clothing, entertainment]))

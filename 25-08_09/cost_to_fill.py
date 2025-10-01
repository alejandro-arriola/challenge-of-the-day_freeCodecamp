from decimal import Decimal

def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    valor = Decimal((tank_size - fuel_level) * price_per_gallon)

    return f"${valor:.2f}"

print(cost_to_fill(20, 0, 4.00))




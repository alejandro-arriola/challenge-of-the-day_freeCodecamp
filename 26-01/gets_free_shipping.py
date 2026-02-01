def gets_free_shipping(cart, minimum):
    prices = {
        "shirt":34.25,
        "jeans":48.50,
        "shoes":75.00,
        "hat":19.95,
        "socks":15.00,
        "jacket":109.95,
    }

    return sum(prices[p] for p in cart) >= minimum
    
print(gets_free_shipping(["socks", "socks", "hat"], 75))
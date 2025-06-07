def calculate_discount(price, percentage):
    if price < 0 or percentage < 0 or percentage > 100:
        raise ValueError("Invalid price or discount percentage")
    discount = price * (percentage / 100)
    return price - discount

# 範例使用
original_price = 1000
discount_percent = 15

final_price = calculate_discount(original_price, discount_percent)
print(f"原價: {original_price}，折扣: {discount_percent}%，折後價格: {final_price}")

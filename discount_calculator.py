def calculate_discount(price, discount_percent):
    """
    Calculate the discounted price only if discount_percent >= 20%.
    Otherwise, return the original price.
    """
    discount_price = price - price * discount_percent / 100
    if discount_percent >= 20:
        return discount_price
    else:
        return price

def discounted_price(get_user_input):
    """
    Get user input to calculate and display the discounted price.
    Expects a function get_user_input(prompt) to receive inputs.
    """
    print("=== Discount Calculator ===")
    
    # Get user input using the provided input function
    price = float(get_user_input("Enter price: "))
    discount_percent = float(get_user_input("Enter discount percent: "))
    
    
    result = calculate_discount(price, discount_percent)
    

    print(f"Discounted price: {result}")

def get_input(prompt):
    
    return input(prompt)


if __name__ == "__main__":
    discounted_price(get_input)

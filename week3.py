# Define the function to calculate the discounted price
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage.
    
    Returns:
    - float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Use the calculate_discount function to determine the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
    else:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")

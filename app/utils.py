def to_usd(my_price):
    """
    This is a docstring.
    It tells us what this function is about.
    What its responsibilities are.
    What the params are about.
    What datatypes the params are.
    What this function will return.
    Example of invoking the function.
    
    This function formats prices with a dollar sign ("$") before it and two decimal places.
    
    Parameters:
        my_price (float): A floating point number of a monetary value
    
    Returns:
        formatted string

    Invoke like this: to_usd(9.9999)
    Example return value: "$9.99"
    """
    return '${:,.2f}'.format(my_price)

if __name__ == "__main__":

    price = input("Please choose a price like 4.9999.")

    print(to_usd(float(price)))




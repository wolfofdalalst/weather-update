def to_celcius(kelvin:float, round_digit=2) -> float:
    """Convert Kelvin to Celcius

    Args:
        kelvin (float): 
        round_digit (int, optional): Defaults to 2.

    Returns:
        float: celcius
    """       
    return round(kelvin-273.15, round_digit)

#TODO: Add a function to convert Fahrenheit to Celcius and vice versa

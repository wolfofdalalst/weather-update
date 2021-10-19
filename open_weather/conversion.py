def to_celsius(kelvin:float, round_digit=2) -> float:
    """Convert Kelvin to Celsius

    Args:
        kelvin (float): 
        round_digit (int, optional): Defaults to 2.

    Returns:
        float: celcius
    """       
    return round(kelvin-273.15, round_digit)

#TODO  Fahrenheit to Celsius conversion
def fahr_to_celsius(fahr):
    cel=(fahr-32)*(5/9)
    return round(cel)

def celsius_to_fahr(celsius):
    fahr=(9*cel)/5+32
    return round(fahr)

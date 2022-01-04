# How's the weather?
def describe_weather(degrees_fahrenheit):
    """ Describes the weather (according to Austin)

    Uses conditional logic to return a string description of the weather based
    on degrees fahrenheit.

    Parameters
    ----------
    degrees_fahrenheit : int
        The temperature in degrees fahrenheit.  Used to reason about weather
          conditions.

    Returns
    -------
    string
        String description of weather conditions.

    """

    # Begins conditional logic with our baseline "if."
    if degrees_fahrenheit < -40:
        return(f"{degrees_fahrenheit} is unbelievably cold!")
    # Elif means 'if the previous condition wasn't true, see if this one is true,"
    #  so there's no reason to state "if temperature >= -40 and temperature < 0.
    elif degrees_fahrenheit < 0:
        return(f"{degrees_fahrenheit} is too cold to do anything outside.")
    elif degrees_fahrenheit < 30:
        return(f"{degrees_fahrenheit} is freezing.")
    elif degrees_fahrenheit < 50:
        return(f"{degrees_fahrenheit} is chilly but manageable")
    elif degrees_fahrenheit < 75:
        return(f"{degrees_fahrenheit} is beautiful!")
    elif degrees_fahrenheit < 100:
        return(f"{degrees_fahrenheit} is pretty warm.")
    else:
        return(f"{degrees_fahrenheit} is hot!")


# Vinyl record sales
def percent_difference(year_1_sales, year_2_sales):
    """ Calculates the percentage difference in year 1 and year 2 sales.

    Simple function that calculates and returns the difference in sales for 2
    years.

    Parameters
    ----------
    year_1_sales : float
        Total sales for year 1.

    year_2_sales : float
        Total sales for year 2.

    Returns
    -------
    float
        The percentage difference from year_1 to year_2
    """
    return ((year_2_sales - year_1_sales) / year_1_sales) * 100

# "main" is usually the 'driver' part of the program.  We define all our logic
#  using function definitions, then we call those functions using main.
def main():
    print(describe_weather(-42))
    print(describe_weather(42))
    print(describe_weather(142))
    print(percent_difference(10, 11.5))


# This is funky syntax that you don't really need to worry about right now.  It
#  essentially means "if we called this program directly (as opposed to importing)
#  then run the main method."  It's a good example of the "double underscores have
#  a special purpose" principle.
if __name__ == '__main__':
    main()

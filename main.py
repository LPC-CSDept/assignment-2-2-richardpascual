def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    celsius = float(input('Please provide the temperature in degrees celsius:'))

    fahrenheit = (9/5) * celsius + 32

    print (f'The calculated temperature in degrees fahrenheit is \t {fahrenheit:.2f}')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()

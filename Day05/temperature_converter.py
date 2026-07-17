def celcius_to_farenheit(celcius):
    return (celcius * 9/5) + 32

temperature = float(input("Enter temperature in Celcius: "))

farenheit = celcius_to_farenheit(temperature)

print(f"{temperature}°C = {farenheit}°F")
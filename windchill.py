def windchill(wind_chill):
    return wind_chill

def celcius(c):
    return c


t = int(input('Please enter the temperature? '))
temp_decision = input('fahrenheit or celsius (F/C)? ').upper()
c = (9 / 5 * t) + 32
    
for v in range (5,65,5):
    if temp_decision == 'C':
        wind_chill = 35.74 + 0.6215 * c - 35.75 * v ** 0.16 + 0.4275 * c * v ** 0.16
        print(f'at temperature {c}F, and wind speed {v} mph, the wind chill is: {wind_chill:6.2f}F')
    
    elif temp_decision == 'F':
        wind_chill = 35.74 + 0.6215 * t - 35.75 * v ** 0.16 + 0.4275 * t * v ** 0.16
        print (f'At temperature {t}F, and wind speed {v} mph, the wind chill is:{wind_chill:6.2f}F')

  

        
          
temp = int(input('what is the temperature'))
temp_decision = input ('fahrenheit or celsius (F/C)?').upper()
C = (9/5*temp)+ 32

    
for v in range (5,65,5):
    if temp_decision == 'C':
        wind_chill = 35.74 + 0.6215*C - 35.75*v** 0.16 + 0.4275*C*v**0.16 
        print(f'at temperature {C}F , and wind speed {v} mph, the wind chill is: {wind_chill:6.2f}F')
    if temp_decision == 'F':
        wind_chill = 35.74 + 0.6215*temp - 35.75*v** 0.16 + 0.4275*temp*v**0.16
        print (f'at temperature {temp}F , and wind speed {v} mph, the wind chill is:{wind_chill:6.2f}F')




  

        
          
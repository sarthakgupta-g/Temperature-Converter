def CtoF(temperature):
  return temperature * 9 / 5 + 32

def FtoC(temperature):
  return (temperature -32) * 5 / 9 

temp=int(input("enter the temperature"))
unit=input("enter the unit of measurement (F or C)")

if (unit=="F"):
  temp=FtoC(temp)
  print(f"{temp} degrees celcius")
else:
  temp=CtoF(temp)
  print(f"{temp} degrees farenheight")

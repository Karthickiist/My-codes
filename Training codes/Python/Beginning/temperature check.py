print("The machine is running")
t=200
while t>105:
    t=float(input("Enter the temperature: "))
    if t>105:
        print("Ovet temperature, reduce thermostat and check after 5 minutes")
    if t<105:
        print("Temperature is under control, check after 15 minutes")
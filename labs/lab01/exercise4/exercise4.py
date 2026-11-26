# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type, hour):
    if vehicle_type == "Electric":
        hourly = 2.00
    elif vehicle_type == "Hybrid":
        if hour >= 22 or hour <= 6:
            hourly = 2.00
        else:
            hourly = 5.00
    else:
        hourly = 5.00
    return hourly

print(get_hourly_rate("Hybrid", 23))
print(get_hourly_rate("Hybrid", 13))
print(get_hourly_rate("Sedan", 2))

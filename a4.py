def hotel_cost(nights):
    return 150*nights
def plane_ride_cost(city):
    if "ISLAMABAD" == city:
        return 200
    elif "LAHORE"==city:
        return 270
    elif "BALOCHISTAN"==city:
        return 360
    elif "KARACHI"==city:
        return 490
def rental_car_cost(days):
    if days>=7:
        return 55*days -33
    elif days>=3:
        return 55*days -20
    else:
       return 55*days
Numofdaysforhotel=int(input("how many days u want to stay in the hotel:"))
Numofdaysforvehicle=int(input("for hoe many days u want to rant a vehicle:"))
city=input("which city u want to go:")
totalcost=hotel_cost(Numofdaysforhotel)+plane_ride_cost(city)+rental_car_cost(Numofdaysforvehicle)
print("total expenditure for trip is:",totalcost)

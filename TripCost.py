def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 200
    elif city == "Los Angles":
        return 475
def rental_car_cost(days):
    carcost = 40* days
    if days >= 7:
        carcost -= 50
    elif days >= 3:
        carcost -= 20
    return carcost
def trip_cost (city,days,spending_money):
    return plane_ride_cost(city) + hotel_cost(days) + rental_car_cost(days) + spending_money
print trip_cost ("Tampa", 5, 600)
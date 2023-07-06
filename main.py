# this is a python based app to provide an easy solution to split the costs of fuel after a trip with mates

def main():
    trip_info()

def trip_info():
    print('When going on a trip with friends you should start a car trip to measure the distance travelled. When filling up petrol, note the cost of fuel per litre. You should also note your cars litres per 100km fuel economy.')
    fuel_cost = float(input('What was the cost of petrol per litre?:'))
    fuel_economy = float(input('How many litres per 100km does your car use?:'))
    travel_dist = float(input('What was the total distance travelled?:'))
    people = int(input('How many people?:'))
    petrol_used = fuel_economy*(travel_dist/100)
    total_price = (petrol_used*fuel_cost)
    final_price = (petrol_used*fuel_cost)/people
    
    print(f'The total amount of fuel used is {petrol_used}L, the cost of fuel is ${total_price} and the cost per person is ${final_price}')

main()
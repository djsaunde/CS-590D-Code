import random, sys

def MontyHallSwitch():
    doors = set([1,2,3])
    car = random.sample(doors, 1)[0]
    
    goats = doors.difference([car])
    
    choice = random.sample(doors, 1)[0]
    
    monty = None
    if choice == car:
        monty = random.sample(goats, 1)[0]
    else:
        monty = goats.difference([choice]).pop()
    
    switch = doors.difference(set([choice, monty]))

    if car in switch:
        return 1
    return 0
    
if __name__ == "__main__":
    results = []
    for i in range(int(sys.argv[1])):
        results.append(MontyHallSwitch())
        
    print sum(results) / float(len(results))

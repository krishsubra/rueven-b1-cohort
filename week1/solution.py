''' This is week1 attempt of the problem '''
from collections import defaultdict, Counter
import sys

visits = defaultdict(list)

def collect_places():
    while True:
        placesvisited = input("Enter the City, Country combo, Enter 'quit' to exit: ")
        
        if len(placesvisited) == 0:
            break

        if ',' not in placesvisited:
            sys.exit("FAIL: Please enter the city/Country combo okay - Expect comma separated entry\n")

        city, country = placesvisited.split(',')
        visits[country].append(city)


def display_places():
    print("You visited: ")
    for key, value in visits.items():
        print(key)
        print(Counter(value))


if __name__ == "__main__":
    collect_places()
    display_places()


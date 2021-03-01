#!/usr/local/bin/python3

from collections import defaultdict,Counter

visits = defaultdict(Counter)  # This will be counter 

def collect_values():
    visits.clear()

    while True:
        location = input("Tell me where you went: ").strip()
        if not location:
            break

        if location.count(',') != 1:
            print(" That was not a correct entry, please make a legal entry: ")
            continue

        city, country = location.split(',')
        visits[country.strip()][city.strip()] += 1


def display_places():
    for country, city in sorted(visits.items()):
        print(country)

        for one_city, counter in sorted(city.items()):
            if counter == 1:
                print(f"\t{one_city}")
            else:
                print(f"\t{one_city} {counter}")


if __name__ == "__main__":
    collect_values()
    display_places()

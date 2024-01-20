from time import time
from typing import List

from greedy.flight import Flight


def solution(b):
    return len(b) > 0


def select_most_promising(candidates: List[Flight]):
    return candidates[-1]


def acceptable(current_solution: List[Flight]):
    if len(current_solution) <= 1:
        return True

    last_flight_added = current_solution[-1]
    return last_flight_added.ora_plecare > current_solution[-2].ora_sosire


def flight_selection_greedy(candidates: List[Flight]):
    b = []

    while len(candidates) > 0:
        most_promising_candidate = select_most_promising(candidates)
        candidates.pop()
        if acceptable(b + [most_promising_candidate]):
            b.append(most_promising_candidate)

    if solution(b):
        return b
    return None


flight1 = Flight("Roma", "Berlin", 3, 4)
flight2 = Flight("Cluj", "Madrid", 5, 9)
flight3 = Flight("Paris", "Milano", 1, 2)
flight4 = Flight("Viena", "Cluj", 5, 7)
flight5 = Flight("New York", "Londra", 0, 6)
flight6 = Flight("Cluj", "Bucuresti", 8, 9)

all_flights = [flight1, flight2, flight3, flight4, flight5, flight6]
all_flights.sort(key=lambda flight: flight.ora_sosire, reverse=True)

schedule = flight_selection_greedy(all_flights)

for flight in schedule:
    print(flight)

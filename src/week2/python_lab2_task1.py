def average(values: list[float]) -> float:
    """Return the average of values, or 0.0 for an empty list."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def largest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the largest population."""
    if not populations:
        return ("", 0)
    # max() returns the first maximal key, so ties go to the earlier city
    name = max(populations, key=populations.get)
    return (name, populations[name])


def smallest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the smallest population."""
    if not populations:
        return ("", 0)
    # min() also returns the first minimal key, so ties go to the earlier city
    name = min(populations, key=populations.get)
    return (name, populations[name])


def total_population(populations: dict[str, int]) -> int:
    """Return the sum of all populations."""
    return sum(populations.values())


if __name__ == "__main__":
    # Keep all input() and print() calls inside this block, otherwise the
    # autograder cannot import your file.

    temperatures = [3, 5, 2, 6, 4, 7, 3]
    city_population = {
        "Riga": 605000,
        "Daugavpils": 78000,
        "Liepaja": 67000,
        "Jelgava": 55000,
        "Valmiera": 23000,
    }

    print(f"Average temperature: {average(temperatures):.1f}")

    city, pop = largest_city(city_population)
    print(f"Largest city: {city} - {pop}")

    city, pop = smallest_city(city_population)
    print(f"Smallest city: {city} - {pop}")

    print(f"Total population: {total_population(city_population)}")

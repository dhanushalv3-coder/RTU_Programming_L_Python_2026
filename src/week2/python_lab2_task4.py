# ---------- Part A: functional style ----------

def item_totals(prices: list[float], quantities: list[int]) -> list[float]:
    """Return price * quantity for each item, using map() and a lambda."""
    return list(map(lambda p, q: p * q, prices, quantities))


def filter_above(totals: list[float], threshold: float = 30) -> list[float]:
    """Return totals greater than threshold, using filter() and a lambda."""
    return list(filter(lambda t: t > threshold, totals))


def pair_up(prices: list[float], quantities: list[int]) -> list[tuple]:
    """Return a list of (price, quantity) tuples, using zip()."""
    return list(zip(prices, quantities))


# ---------- Part B: list comprehensions ----------

def item_totals_comp(prices: list[float], quantities: list[int]) -> list[float]:
    """Same as item_totals(), but with a list comprehension."""
    return [p * q for p, q in zip(prices, quantities)]


def filter_above_comp(totals: list[float], threshold: float = 30) -> list[float]:
    """Same as filter_above(), but with a list comprehension."""
    return [t for t in totals if t > threshold]


if __name__ == "__main__":
    # Keep all input() and print() calls inside this block, otherwise the
    # autograder cannot import your file.
    totals = item_totals(PRICES, QUANTITIES)
    print(f"Totals: {totals}")
    print(f"Totals > 30: {filter_above(totals)}")
    print(f"Price-quantity pairs: {pair_up(PRICES, QUANTITIES)}")

    totals_comp = item_totals_comp(PRICES, QUANTITIES)
    print(f"Totals (comprehension): {totals_comp}")
    print(f"Totals > 30 (comprehension): {filter_above_comp(totals_comp)}")

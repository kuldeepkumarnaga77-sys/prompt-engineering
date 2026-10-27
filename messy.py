students = {
    "Alice": 88,
    "Bob": 72,
    "Charlie": 95,
    "Dana": 64,
    "Eve": 81,
}

EMPTY_COLLECTION_RESULT = 0


def class_average(scores):
    """Return the mean of scores, or 0 if the list is empty."""
    if not scores:
        return EMPTY_COLLECTION_RESULT
    return sum(scores) / len(scores)


def count_above_average(scores):
    """Return how many scores are strictly above the class average."""
    if not scores:
        return EMPTY_COLLECTION_RESULT
    average = class_average(scores)
    return sum(1 for score in scores if score > average)


if __name__ == "__main__":
    scores = list(students.values())
    average = class_average(scores)
    above_average = count_above_average(scores)

    print(f"Class average: {average:.2f}")
    print(f"Students above average: {above_average}")

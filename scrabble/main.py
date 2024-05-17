import random


def calculate_score_for_word(word: str) -> int:
    "Returns the total points for a given word"

    if not isinstance(word, str):
        raise ValueError("Input word should be of type string.")

    total_points = 0
    for letter in word:
        letter_points = get_points_for_single_letter(letter)
        total_points += letter_points
    return total_points


def get_points_for_single_letter(letter: str) -> int:
    "Returns the points for a single letter"

    if not isinstance(letter, str):
        raise ValueError("Letter can only be of type string.")

    points_dict = {"E": 1, "A": 1, "I": 1, "O": 1,
                   "N": 1, "R": 1, "T": 1, "L": 1, "S": 1, "U": 1, "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3,
                   "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10}
    return points_dict.get(letter)


def get_random_letters() -> int:
    "Returns 7 randomly chosen letters from the alphabet"
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return random.choices(alphabet, k=7)


def create_bag() -> list[str]:
    "Returns a list of strings of all the letters in a bag."
    distribution_dict = {"E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6, "T": 6, "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2,
                         "C": 2, "M": 2, "P": 2, "F": 2, "H": 2, "V": 2, "W": 2, "Y": 2, "K": 1, "J": 1, "X": 1, "Q": 1, "Z": 1}

    bag = []
    for letter, quantity in distribution_dict.items():
        for i in range(quantity):
            bag.append(letter)
    return bag


def get_seven_tiles_from_bag(bag: list[str]) -> list[str]:
    "Returns 7 letters from our bag."
    rack = random.choices(bag, k=7)
    return rack


def load_file():
    "Loads a file"
    with open('dictionary.txt', 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    print(load_file())

from main import calculate_score_for_word, get_points_for_single_letter, get_random_letters, create_bag, get_seven_tiles_from_bag
import pytest


def test_calculate_score_for_word_valid_input():
    assert calculate_score_for_word("GUARDIAN") == 10


def test_calculate_score_for_word_invalid_input():
    with pytest.raises(ValueError):
        calculate_score_for_word(76543)


def test_get_points_for_single_letter_valid_input():
    assert get_points_for_single_letter('N') == 1


def test_get_points_for_single_letter_invalid_input():
    with pytest.raises(ValueError):
        get_points_for_single_letter(9)


def test_get_random_letters():
    assert len(get_random_letters()) == 7


def test_create_bag():
    assert create_bag().count('E') == 12


def test_get_seven_tiles_from_bag():
    assert len(get_seven_tiles_from_bag(
        ['E', 'Y', 'S', 'P', 'Q', 'A', 'B', 'C', 'D'])) == 7

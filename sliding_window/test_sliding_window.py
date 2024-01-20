from sliding_window.sliding_window import (
    average_contiguous_sub_arrays_with_target,
    closest_to_zero,
    count_negative_numbers,
    find_factorial,
    find_middle_number,
    get_counted_negatives_per_target,
    count_letter_sequence,
    collectDuplicates,
    fruits_into_basket,
    get_last_digits,
    longest_string_no_vowel,
    find_duplicate,
    find_max_sum,
    perfect_number,
    smallest_sub_array_equal_target,
    find_min_max_diff,
)


def test_average_contiguous_sub_arrays_with_target() -> None:
    assert average_contiguous_sub_arrays_with_target(
        [1, 3, 2, 6, -1, 4, 1, 8, 2], target=5
    ) == [2.2, 2.8, 2.4, 3.6, 2.8]


def test_closest_to_zero() -> None:
    assert closest_to_zero([-2, 5, -5, -1]) == -1


def test_find_factorial() -> None:
    assert find_factorial(5) == 120
    assert find_factorial(2) == 2
    assert find_factorial(0) == 1


def test_get_counted_negatives_per_target() -> None:
    assert get_counted_negatives_per_target([-1, 2, -2, 3, 5, -7, -5], target=3) == [2, 1, 1, 2,]


def test_count_letter_sequence() -> None:
    assert count_letter_sequence("abbccca") == "a1b2c3a1"
    assert count_letter_sequence("ayaabapee") == "a1y1a2b1a1p1e2"
    assert count_letter_sequence("eerggtt") == "e2r1g2t2"


def test_longest_string_no_vowel() -> None:
    assert longest_string_no_vowel("") == None
    assert longest_string_no_vowel("codeforintelligents") == "nts"


def test_find_duplicate() -> None:
    assert find_duplicate([5, 6, 8, 2, 4, 6, 9], 2) == False
    assert find_duplicate([5, 6, 8, 2, 4, 6, 9], 6) == True


def test_find_max_sum() -> None:
    assert find_max_sum([], None) == None
    assert find_max_sum(None, 2) == None
    assert find_max_sum(None, None) == None
    assert find_max_sum([1, 2, 4, 6, -1, 10], 2) == 10
    assert find_max_sum([1, 2, 4, 6, -1, 10], 3) == 15


def test_smallest_sub_array_equal_target() -> None:
    assert smallest_sub_array_equal_target(None, None) == None
    assert smallest_sub_array_equal_target([2, 1, 5, 2, 3, 2], 7) == 2
    assert smallest_sub_array_equal_target([2, 1, 5, 2, 3, 2], 8) == 3


def test_find_min_max_diff() -> None:
    assert find_min_max_diff([3, 8, 9, 15], 2) == 6.5


def test_perfect_number() -> None:
    assert perfect_number(22) == True
    assert perfect_number(220) == False
    # assert perfect_number(0) == False


def test_find_middle_number() -> None:
    assert find_middle_number([1, 2, 3]) == 2
    assert find_middle_number([1, 2, 3, 4]) == 2.5
    assert find_middle_number([1, 2, 3, 4, 5, 6]) == 3.5
    assert find_middle_number([1, 2, 3, 4, 5, 6, 7]) == 4


def test_get_last_digits() -> None:
    assert get_last_digits(122345, 2) == [4, 5]


def test_count_negative_numbers() -> None:
    assert count_negative_numbers([-1, 3, 4, 6, 7, -5]) == 2


def test_findDuplicate() -> None:
    assert collectDuplicates([2, 1, 3, 3, 5, 4, 4, 1]) == [1, 3, 4]


def test_fruits_in_basket() -> None:
    assert fruits_into_basket(["A", "B", "C", "A", "C"]) == 3
    assert fruits_into_basket(["B", "C", "B", "B", "C"]) == 5


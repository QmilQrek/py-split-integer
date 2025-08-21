from app.split_integer import split_integer


def _assert_properties(result, value, number_of_parts):
    # length equals number_of_parts
    assert len(result) == number_of_parts
    # all elements are integers
    assert all(isinstance(x, int) for x in result)
    # list is sorted ascending (non-decreasing)
    assert all(result[i] <= result[i + 1] for i in range(len(result) - 1))
    # max-min difference <= 1
    assert (max(result) - min(result)) <= 1
    # sum equals value
    assert sum(result) == value


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, parts = 8, 8
    result = split_integer(value, parts)
    assert result == [1] * 8
    _assert_properties(result, value, parts)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, parts = 8, 2
    result = split_integer(value, parts)
    assert result == [4, 4]
    _assert_properties(result, value, parts)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, parts = 8, 1
    result = split_integer(value, parts)
    assert result == [8]
    _assert_properties(result, value, parts)


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, parts = 8, 3
    result = split_integer(value, parts)
    assert result == [2, 3, 3]
    _assert_properties(result, value, parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 1, 3
    result = split_integer(value, parts)
    assert result == [0, 0, 1]
    _assert_properties(result, value, parts)

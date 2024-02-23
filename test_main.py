import pytest
from main import is_number, TypeCheck, MakeSave, MakeSafeWithLambda, \
    make_pair, sizes, odd_len_only, make_fib, bigram_frequencies


# test_is_number
@pytest.mark.parametrize("input_value, expected_result", [
    (5, True),
    (-10, True),
    ('10', True),
    ('bad', False),
    (False, False)
], ids=["int", "negative_int", "str_digit", "str_non_digit", "bool"])
def test_is_number(input_value, expected_result):
    assert is_number(input_value) == expected_result


# TypeCheck
@pytest.mark.parametrize("func, pred, arg, expected_result", [
    (TypeCheck.doubling, TypeCheck.is_positive_integer, 5, 10),
    (lambda x: x + 3, TypeCheck.is_positive_integer, 5, 8),
    (TypeCheck.doubling, TypeCheck.is_positive_integer, 'bad', False),
], ids=["doubling_positive_int", "lambda_plus3_positive_int", "doubling_str"])
def test_type_check(func, pred, arg, expected_result):
    result = TypeCheck.type_check(func, pred, arg)
    assert result == expected_result


# MakeSafe
@pytest.fixture
def safe_square():
    return MakeSave.make_safe(MakeSave.doubling, MakeSave.is_positive_integer)


@pytest.mark.parametrize("arg, expected_result", [
    (5, 10),
    ('bad', False),
    (3, 6),
    ('hello', False)
], ids=["positive_int_square", "illegal_argument", "lambda_plus3_positive_int", "str_predicate"])
def test_make_safe(safe_square, arg, expected_result):
    result = safe_square(arg)
    assert result == expected_result


# MakeSafeWithLambda
@pytest.fixture
def safe_square_sec():
    return MakeSafeWithLambda.make_safe(MakeSafeWithLambda.doubling, MakeSafeWithLambda.is_positive_integer)


@pytest.mark.parametrize("arg, expected_result", [
    (5, 10),
    ('bad', False),
    (3, 6),
    ('hello', False)
], ids=["positive_int_square", "illegal_argument", "lambda_plus3_positive_int", "str_predicate"])
def test_make_safe_with_lambda(safe_square, arg, expected_result):
    result = safe_square(arg)
    assert result == expected_result


# make_pair
@pytest.fixture
def pair_func():
    return make_pair(10, 'hello')


@pytest.mark.parametrize("selector, expected_result", [
    (0, 10),
    (1, 'hello'),
    ('pair', (10, 'hello'))
], ids=["select_first", "select_second", "select_pair"])
def test_make_pair(pair_func, selector, expected_result):
    result = pair_func(selector)
    assert result == expected_result


def test_make_pair_invalid_selector(pair_func):
    with pytest.raises(ValueError):
        pair_func('invalid_selector')


# sizes
def test_sizes():
    result = sizes([(1, 2), (3, 4, 5), (6, 7, 8, 9)])
    assert result == [2, 3, 4]


# odd_len_only
def test_odd_len_only():
    result = odd_len_only([(1, 2), (3, 4, 5), (6, 7, 8, 9), (), ('a', 'b', 'c'), ('apple', 'orange', 'banana')])
    assert result == [(3, 4, 5), ('a', 'b', 'c'), ('apple', 'orange', 'banana')]


# make_fib
@pytest.mark.parametrize("n, expected_result", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5)
], ids=["fibonacci_0", "fibonacci_1", "fibonacci_2", "fibonacci_3", "fibonacci_4"])
def test_make_fib_with_specific_calls(n, expected_result):
    fibonacci_func = make_fib()

    for _ in range(n):
        fibonacci_func()

    assert fibonacci_func() == expected_result


# bigram_frequencies
def test_bigram_frequencies():
    result = bigram_frequencies("Viva la vida")
    assert result['vi'] == 0.2222222222222222

#!/usr/local/bin/python
from numbers import Number
from collections import Counter


def is_number(arg: any) -> bool:
    """
    Checks if the given argument is a number.

    Parameters:
    - arg (any): The argument to be checked.

    Returns:
    - bool: True if arg is a number, False otherwise.
    """
    if isinstance(arg, bool):
        return False
    if isinstance(arg, Number):
        return True
    else:
        return arg.isdigit()


class DoublingMixin:
    @staticmethod
    def doubling(x):
        return x * 2


class PositiveIntegerMixin:
    @staticmethod
    def is_positive_integer(x):
        return isinstance(x, int) and x > 0


class TypeCheck(DoublingMixin, PositiveIntegerMixin):
    @staticmethod
    def type_check(one_arg_func, type_predicate, arg):
        """
        Applies the given function to the argument if the argument is legal according to the type predicate.

        Parameters:
        - func (callable): A function taking a single argument.
        - type_predicate (callable): A predicate function that returns True if the argument is legal.
        - arg (any): The argument to be checked and passed to the function.

        Returns:
        - result: The result of applying the function to the argument if it is legal, False otherwise.
        """
        if type_predicate(arg):
            return one_arg_func(arg)
        else:
            return False


class MakeSave(DoublingMixin, PositiveIntegerMixin):
    @staticmethod
    def make_safe(one_arg_func, type_predicate):
        """
        Returns a new function that applies the given function to the argument if the argument is legal according to
        the type predicate, otherwise returns False.

        Parameters:
        - one_arg_func (callable): A function taking a single argument.
        - type_predicate (callable): A predicate function that returns True if the argument is legal.

        Returns:
        - callable: A new function that checks the type using the type_predicate before applying the one_arg_func.
        """
        def safe_function(arg):
            if type_predicate(arg):
                return one_arg_func(arg)
            else:
                return False
        return safe_function


class MakeSafeWithLambda(DoublingMixin, PositiveIntegerMixin):
    @staticmethod
    def make_safe(one_arg_func, type_predicate):
        """
        Returns a new function that applies the given function to the argument if the argument is legal according to
        the type predicate, otherwise returns False.

        Parameters:
        - one_arg_func (callable): A function taking a single argument.
        - type_predicate (callable): A predicate function that returns True if the argument is legal.

        Returns:
        - callable: A new function that checks the type using the type_predicate before applying the one_arg_func.
        """
        return lambda arg: one_arg_func(arg) if type_predicate(arg) else False


def make_pair(first, second):
    """
    Returns a function that takes a selector message as an argument and returns the corresponding result.

    Parameters:
    - first: The first argument.
    - second: The second argument.

    Returns:
    - callable: A function that handles the selector message and returns the appropriate result.
    """
    def pair_selector(selector):
        if selector == 0:
            return first
        elif selector == 1:
            return second
        elif selector == 'pair':
            return (first, second)
        else:
            raise ValueError("Invalid selector message. Use 0, 1, or 'pair'.")

    return pair_selector


def sizes(sequence_of_tuples):
    """
    Returns a sequence of sizes for each tuple in the input sequence.

    Parameters:
    - sequence_of_tuples (iterable): A sequence containing tuples.

    Returns:
    - list: A list of sizes for each tuple.
    """
    return list(map(len, sequence_of_tuples))


def odd_len_only(sequence_of_tuples):
    """
    Returns a sequence containing only those tuples from the input sequence that have odd length.

    Parameters:
    - sequence_of_tuples (iterable): A sequence containing tuples.

    Returns:
    - list: A list of tuples with odd lengths.
    """
    return list(filter(lambda x: len(x) % 2 != 0, sequence_of_tuples))


def make_fib():
    """
    Returns a function that, when called, returns the next number in the Fibonacci sequence.

    Returns:
    - callable: A function that generates the next Fibonacci number on each call.
    """
    a, b = 1, 1
    
    def fib():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return result

    return fib


def bigram_frequencies(text):
    """
    Returns a dictionary with bigrams as keys and normalized frequencies as values.

    Parameters:
    - text (str): The input text.

    Returns:
    - dict: A dictionary with bigrams as keys and normalized frequencies as values.
    """
    text = text.lower().replace(" ", "")
    bigrams = [text[i:i+2] for i in range(len(text)-1)]
    total_bigrams = len(bigrams)

    bigram_counts = Counter(bigrams)

    normalized_frequencies = {bigram: count / total_bigrams for bigram, count in bigram_counts.items()}

    return normalized_frequencies

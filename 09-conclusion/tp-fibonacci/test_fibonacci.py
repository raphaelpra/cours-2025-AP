"""
Tests pour les implementations de Fibonacci.

Lancez avec :
    pytest test_fibonacci.py -v
"""

import pytest

# Valeurs de reference
EXPECTED = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5,
    6: 8,
    7: 13,
    8: 21,
    9: 34,
    10: 55,
    20: 6765,
    30: 832040,
}


class TestFibNaive:
    """Tests pour l'implementation naive (petites valeurs seulement)."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (10, 55),
        ],
    )
    def test_small_values(self, n, expected):
        """Test avec petites valeurs (naive est trop lent pour n > 30)."""
        from fibonacci import fib_naive

        assert fib_naive(n) == expected


class TestFibMemo:
    """Tests pour l'implementation avec memoisation."""

    @pytest.mark.parametrize("n,expected", list(EXPECTED.items()))
    def test_values(self, n, expected):
        from fibonacci import fib_memo

        assert fib_memo(n) == expected


class TestFibIterative:
    """Tests pour l'implementation iterative."""

    @pytest.mark.parametrize("n,expected", list(EXPECTED.items()))
    def test_values(self, n, expected):
        from fibonacci import fib_iterative

        assert fib_iterative(n) == expected


class TestFibonacciGenerator:
    """Tests pour l'implementation objet."""

    @pytest.mark.parametrize("n,expected", list(EXPECTED.items()))
    def test_default_values(self, n, expected):
        """Test avec valeurs par defaut (0, 1)."""
        from fibonacci import FibonacciGenerator

        gen = FibonacciGenerator()
        assert gen.compute(n) == expected

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 2),
            (1, 1),
            (2, 3),
            (3, 4),
            (4, 7),
            (5, 11),
            (6, 18),
            (7, 29),
        ],
    )
    def test_lucas_sequence(self, n, expected):
        """Test suite de Lucas : u0=2, u1=1."""
        from fibonacci import FibonacciGenerator

        lucas = FibonacciGenerator(u0=2, u1=1)
        assert lucas.compute(n) == expected


class TestFibBinet:
    """Tests pour la formule fermee (Binet)."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (10, 55),
            (20, 6765),
        ],
    )
    def test_values(self, n, expected):
        """Test avec valeurs moderees (precision limitee pour grands n)."""
        from fibonacci import fib_binet

        assert fib_binet(n) == expected

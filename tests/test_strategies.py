import pytest

from grid_strategy import strategies


@pytest.fixture
def rectangular_strategy():
    return strategies.RectangularStrategy()


@pytest.fixture
def square_strategy():
    return strategies.SquareStrategy()


# Test the rectangular strategy to see if the get_grid_arrangement returns the right tuple.
@pytest.mark.parametrize(
    "num_plots, grid_arrangement",
    [
        (1, (1,)),
        (2, (2,)),
        (3, (3,)),
        (4, (2, 2)),
        (5, (5,)),
        (6, (3, 3)),
        (10, (5, 5)),
        (12, (4, 4, 4)),
        (20, (5, 5, 5, 5)),
    ],
)
def test_rectangular_strategy(rectangular_strategy, num_plots, grid_arrangement):
    assert rectangular_strategy.get_grid_arrangement(num_plots) == grid_arrangement


@pytest.mark.parametrize(
    "num_plots, grid_arrangement",
    [
        (1, (1,)),
        (2, (2,)),
        (3, (2, 1)),
        (4, (2, 2)),
        (5, (2, 3)),
        (6, (3, 3)),
        (7, (2, 3, 2)),
        (8, (3, 2, 3)),
        (9, (3, 3, 3)),
        (10, (3, 4, 3)),
        (12, (4, 4, 4)),
        (14, (3, 4, 4, 3)),
        (17, (3, 4, 3, 4, 3)),
        (20, (5, 5, 5, 5)),
        (31, (6, 6, 7, 6, 6)),
        (34, (6, 5, 6, 6, 5, 6)),
        (58, (7, 8, 7, 7, 7, 7, 8, 7)),
        (94, (9, 10, 9, 10, 9, 9, 10, 9, 10, 9)),
    ],
)
def test_square_strategy(square_strategy, num_plots, grid_arrangement):
    assert square_strategy.get_grid_arrangement(num_plots) == grid_arrangement


# Test for bad input
@pytest.mark.parametrize("n", [-1, -1000])
def test_rectangular_strategy_with_bad_input(rectangular_strategy, n):
    with pytest.raises(ValueError):
        rectangular_strategy.get_grid(n)


@pytest.mark.parametrize("n", [-1, -1000])
def test_square_strategy_with_bad_input(square_strategy, n):
    with pytest.raises(ValueError):
        square_strategy.get_grid(n)


# Test for the `stripe_even` functions - it is not entirely clear that these
# will remain public, so do not take the fact that it is tested as an
# indication that this is a critical part of the public interface
@pytest.mark.parametrize(
    "args, exp", [((4, 3, 2, 4), (3, 4, 3, 3, 4, 3)), ((3, 2, 1, 1), (2, 2, 1, 2))]
)
def test_stripe_even(args, exp):
    act = strategies.SquareStrategy.stripe_even(*args)

    assert act == exp


def test_stripe_even_value_error():
    # This fails when the total number (n_more + n_less) is not even
    with pytest.raises(ValueError):
        strategies.SquareStrategy.stripe_even(3, 1, 4, 1)

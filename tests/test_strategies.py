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
        (20, (5, 5, 5, 5)),
    ],
)
def test_square_strategy(square_strategy, num_plots, grid_arrangement):
    assert square_strategy.get_grid_arrangement(num_plots) == grid_arrangement

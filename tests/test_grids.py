import pytest
from unittest import mock

from grid_strategy.strategies import SquareStrategy


class SpecValue:
    def __init__(self, rows, cols, parent=None):
        self.rows = rows
        self.cols = cols
        self.parent = parent

    def __repr__(self):  # pragma: nocover
        return f"{self.__class__.__name__}({self.rows}, {self.cols})"

    def __eq__(self, other):
        return self.rows == other.rows and self.cols == other.cols


class GridSpecMock:
    def __init__(self, nrows, ncols, *args, **kwargs):
        self._nrows_ = nrows
        self._ncols_ = ncols

        self._args_ = args
        self._kwargs_ = kwargs

    def __getitem__(self, key_tup):
        return SpecValue(*key_tup, self)


@pytest.fixture
def gridspec_mock():
    class Figure:
        pass

    def figure(*args, **kwargs):
        return Figure()

    with mock.patch(f"grid_strategy._abc.gridspec.GridSpec", new=GridSpecMock) as g:
        with mock.patch(f"grid_strategy._abc.plt.figure", new=figure):
            yield g


@pytest.mark.parametrize(
    "align, n, exp_specs",
    [
        ("center", 1, [(0, slice(0, 1))]),
        ("center", 2, [(0, slice(0, 1)), (0, slice(1, 2))]),
        ("center", 3, [(0, slice(0, 2)), (0, slice(2, 4)), (1, slice(1, 3))]),
        ("left", 3, [(0, slice(0, 2)), (0, slice(2, 4)), (1, slice(0, 2))]),
        ("right", 3, [(0, slice(0, 2)), (0, slice(2, 4)), (1, slice(2, 4))]),
        ("justified", 3, [(0, slice(0, 1)), (0, slice(1, 2)), (1, slice(0, 2))]),
        (
            "center",
            8,
            [
                (0, slice(0, 2)),
                (0, slice(2, 4)),
                (0, slice(4, 6)),
                (1, slice(1, 3)),
                (1, slice(3, 5)),
                (2, slice(0, 2)),
                (2, slice(2, 4)),
                (2, slice(4, 6)),
            ],
        ),
        ("left", 2, [(0, slice(0, 1)), (0, slice(1, 2))]),
    ],
)
def test_square_spec(gridspec_mock, align, n, exp_specs):
    ss = SquareStrategy(align)

    act = ss.get_grid(n)
    exp = [SpecValue(*spec) for spec in exp_specs]

    assert act == exp

# grid-strategy

[![PyPI version](https://img.shields.io/pypi/v/grid-strategy.svg?style=flat-square)](https://pypi.org/project/grid-strategy/)
[![Build Status](https://dev.azure.com/matplotlib/matplotlib/_apis/build/status/matplotlib.grid-strategy?branchName=master)](https://dev.azure.com/matplotlib/matplotlib/_build/latest?definitionId=2&branchName=master)
[![Documentation Status](https://readthedocs.org/projects/grid-strategy/badge/?version=latest)](https://grid-strategy.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/matplotlib/grid-strategy/branch/master/graph/badge.svg)](https://codecov.io/gh/matplotlib/grid-strategy)


Grid-strategy is a python package that enables the user
organize _matplotlib_ plots using different **grid strategies**.

## Abstract

This package adds a mechanism for creating a grid of
subplots based on the number of axes to be plotted and
a strategy for how they should be arranged, with some
sensible strategy as the default.

## Detailed Description

It is often the case that you have some number of
plots to display (and this number may be unknown
ahead of time), and want some sensible arrangement
of the plots so that they are all roughly equally
aligned. However, the `subplots` and `gridspec`
methods for creating subplots require both an `x`
and a `y` dimension for creation and population of
a grid. This package would allow users to specify a
strategy for the creation of a grid, and then specify
how many axes they want to plot, and they would
get back a collection of axes arranged according
to their strategy.

The SquareStrategy alternates rows of x and x-1 columns
to get as close as possible to a square shape for the plots.
Some examples featuring this technique:

<img src="https://gist.github.com/pganssle/afde3d9ae1e9f1d9349cff4a00ddead0/raw/b82d5c2fa3ab34579cfdd4e28be058230fdde199/grid_arrangement06.png" width="300" alt="n=6"> <img src="https://gist.github.com/pganssle/afde3d9ae1e9f1d9349cff4a00ddead0/raw/b82d5c2fa3ab34579cfdd4e28be058230fdde199/grid_arrangement07.png" width="300" alt="n=7">

<img src="https://gist.github.com/pganssle/afde3d9ae1e9f1d9349cff4a00ddead0/raw/b82d5c2fa3ab34579cfdd4e28be058230fdde199/grid_arrangement08.png" width="300" alt="n=8"> <img src="https://gist.github.com/pganssle/afde3d9ae1e9f1d9349cff4a00ddead0/raw/b82d5c2fa3ab34579cfdd4e28be058230fdde199/grid_arrangement17.png" width="300" alt="n=17">

This makes use of a `GridStrategy` object, which populates a `GridSpec`. In general, this concept can likely be implemented as a layer of abstraction *above* `gridspec.GridSpec`.

Some basic strategies that will be included in the first release:

- `"Square"` - As implemented in the pictures above - currently this is centered, but the base `SquareStrategy` object has options for `alignment` which include:
    - `'center'` (default), `'left'`, `'right'` - empty spaces either center the plots or leave them ragged-left or ragged-right
    - `'justified'` - This will fill every column as "fully-justified", with some plots being stretched to fill all of the colums in the row.

- `"Rectangular"` - Similar to `"Square"`, this would find the largest pair of factors of the number of plots and use that to populate a rectangular grid - so `6` would return a 3x2 grid, `7` would return a 7x1 grid, and `10` would return a 5x2 grid.


### Higher dimensions

Currently the package is limited to 2-dimensional
grid arrangements, but a "nice-to-have" might be
a higher-order API for `GridStrategy` that also allows
for the proliferation of additional *figures* (e.g.
"if I have more than 10 axes to plot, split them
up as evenly as possible among `n / 10` different
figures"). This would be no harder to implement
in terms of the creation of such strategies, but
may be harder to work with since it would
necessarily spawn axes across multiple figures.

### Installation Instructions
Simply run:
`pip install grid-strategy`
Then, in your project, do
`from grid_strategy import strategies`
and the strategies class has all usable strategies.
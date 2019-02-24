"""Proof of concept code for MEP 30: Automatic subplot management."""
import itertools as it

from abc import ABCMeta, abstractmethod

from matplotlib import gridspec
import matplotlib.pyplot as plt
import numpy as np


class GridStrategy(metaclass=ABCMeta):
    """
    Static class used to compute grid arrangements given the number of subplots
    you want to show. By default, it goes for a symmetrical arrangement that is
    nearly square (nearly equal in both dimensions).
    """

    def __init__(self, alignment="center"):
        self.alignment = alignment

    def get_grid(self, n):
        """  
        Return a list of axes designed according to the strategy.
        Grid arrangements are tuples with the same length as the number of rows,
        and each element specifies the number of colums in the row.
        Ex (2, 3, 2) leads to the shape
             x x 
            x x x
             x x
        where each x would be a subplot.
        """

        grid_arrangement = self.get_grid_arrangement(n)
        return self.get_gridspec(grid_arrangement)

    @classmethod
    @abstractmethod
    def get_grid_arrangement(cls, n):
        pass

    def get_gridspec(self, grid_arrangement):
        nrows = len(grid_arrangement)
        ncols = max(grid_arrangement)

        # If it has justified alignment, will not be the same as the other alignments
        if self.alignment == "justified":
            return self._justified(nrows, grid_arrangement)
        else:
            return self._ragged(nrows, ncols, grid_arrangement)

    def _justified(self, nrows, grid_arrangement):
        ax_specs = []
        num_small_cols = np.lcm.reduce(grid_arrangement)
        gs = gridspec.GridSpec(
            nrows, num_small_cols, figure=plt.figure(constrained_layout=True)
        )
        for r, row_cols in enumerate(grid_arrangement):
            skip = num_small_cols // row_cols
            for col in range(row_cols):
                s = col * skip
                e = s + skip

                ax_specs.append(gs[r, s:e])
        return ax_specs

    def _ragged(self, nrows, ncols, grid_arrangement):
        if len(set(grid_arrangement)) > 1:
            col_width = 2
        else:
            col_width = 1

        gs = gridspec.GridSpec(
            nrows, ncols * col_width, figure=plt.figure(constrained_layout=True)
        )

        ax_specs = []
        for r, row_cols in enumerate(grid_arrangement):
            # This is the number of missing columns in this row. If some rows
            # are a different width than others, the column width is 2 so every
            # column skipped at the beginning is also a missing slot at the end.
            if self.alignment == "left":
                # This is left-justified (or possibly full justification)
                # so no need to skip anything
                skip = 0
            elif self.alignment == "right":
                # Skip two slots for every missing plot - right justified.
                skip = (ncols - row_cols) * 2
            else:
                # Defaults to centered, as that is the default value for the class.
                # Skip one for each missing column - centered
                skip = ncols - row_cols

            for col in range(row_cols):
                s = skip + col * col_width
                e = s + col_width

                ax_specs.append(gs[r, s:e])

        return ax_specs

###
## simple_package - Module graphics.py
## Basic graphics for statistics
###

"""Simple plotting helpers for simple_package.

Provides a histogram plotter that marks mean and median.
Importing this module does not require matplotlib; attempting to
plot without matplotlib will raise an informative ImportError.
"""

try:
    import numpy as np
except Exception:
    np = None

try:
    import matplotlib.pyplot as plt
except Exception:
    plt = None


def _require_numpy():
    if np is None:
        raise ImportError(
            "Oops! It looks like NumPy isn't installed.\n"
        "The graphics module needs NumPy to work.\n"
        "You can install it by running: pip install numpy"
        )


def _require_matplotlib():
    if plt is None:
        raise ImportError(
            "Oops! It looks like Matplotlib isn't installed.\n"
            "The graphics module needs Matplotlib to create plots.\n"
            "You can install it by running: pip install matplotlib"
        )


def plot_histogram(data, bins=30, show=True, filename=None, label=None):
    """Plot a histogram of `data`, marking mean and median.

    Parameters
    - data: list or numpy array
    - bins: number of histogram bins
    - show: whether to call plt.show()
    - filename: if provided, save the figure to this path
    - label: optional label printed in the title

    Returns (fig, ax)
    """
    _require_numpy()
    _require_matplotlib()

    arr = np.array(data)
    if arr.size == 0:
        raise ValueError("It seems the input has no data.\n"
    "Please add some values and try again.")

    mean = float(np.mean(arr))
    median = float(np.median(arr))

    fig, ax = plt.subplots()
    ax.hist(arr, bins=bins, alpha=0.7)
    ax.axvline(mean, color='red', linestyle='--', label=f'mean={mean:.4f}')
    ax.axvline(median, color='green', linestyle='-.', label=f'median={median:.4f}')
    title = "Histogram"
    if label:
        title += f" - {label}"
    ax.set_title(title)
    ax.legend()

    if filename:
        fig.savefig(filename)

    if show:
        plt.show()

    return fig, ax

if __name__ == "__main__":
    # Simple demo for manual testing
    print("Running a quick test of plot_histogram...")

    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    try:
        plot_histogram(sample_data, bins=5, label="sample_data")
        print("Histogram test completed successfully.")
    except Exception as e:
        print("Test failed:", e)
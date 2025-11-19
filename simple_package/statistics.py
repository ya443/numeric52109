###
## simple_package - Module statistics.py
## Basic statistics calculations
###

## Here I need functions to take in data and do the
## following:
##
## 1) Calculate the mean, median, and standard deviation. 
##
## 2) Display the result with a clear and pretty print 
##    statement.
##
## 3) Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4) Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5) Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.
##

"""Small statistics helpers for simple_package.

Provides mean, median and standard deviation helpers plus a
pretty-print summary. The module defers requiring numpy until
the functions are called so importing the package won't raise
if numpy is missing; calling the functions will raise an
informative ImportError when numpy is required but not present.
"""

try:
	import numpy as np
except Exception:
	np = None


def _require_numpy():
	if np is None:
		raise ImportError(
			 "Oops! It looks like NumPy isn't installed.\n"
            "The statistics module needs NumPy to work.\n"
            "You can install it by running: pip install numpy"
		)


def _ensure_array(data):
	"""Convert input to a numpy array and validate it.

	Accepts lists or numpy arrays. Raises informative errors for
	missing numpy or empty input.
	"""
	_require_numpy()

	if isinstance(data, list):
		arr = np.array(data)
	elif isinstance(data, np.ndarray):
		arr = data
	else:
		try:
			arr = np.array(data)
		except Exception:
			raise TypeError("Please provide your data as a list or a NumPy array.")

	if arr.size == 0:
		raise ValueError("It looks like the input is empty, please add some data.")

	return arr


def mean(data):
	"""Return the mean of the data as a float."""
	arr = _ensure_array(data)
	return float(np.mean(arr))


def median(data):
	"""Return the median of the data as a float."""
	arr = _ensure_array(data)
	return float(np.median(arr))


def std(data, ddof=0):
	"""Return the standard deviation of the data as a float.

	ddof is forwarded to numpy.std (default 0).
	"""
	arr = _ensure_array(data)
	return float(np.std(arr, ddof=ddof))


def summary(data):
	"""Return a dict with mean, median and std for the input data."""
	return {"mean": mean(data), "median": median(data), "std": std(data)}


def pretty_print(data, label=None):
    """Compute and print a user-friendly summary of the data.

    Example output:
        ----------------------
        | Data: sample       |
        ----------------------
        | Count:   10        |
        | Mean:    2.3400    |
        | Median:  2.0000    |
        | Std:     1.2300    |
        ----------------------
    """
    s = summary(data)
    count = len(_ensure_array(data))

    # Title formatting
    title = f"Data: {label}" if label else "Data Summary"
    line = "-" * (len(title) + 4)

    print(line)
    print(f"| {title} |")
    print(line)
    print(f"| Count:   {count:<9} |")
    print(f"| Mean:    {s['mean']:.4f}    |")
    print(f"| Median:  {s['median']:.4f}    |")
    print(f"| Std:     {s['std']:.4f}    |")
    print(line)




if __name__ == '__main__':
    # Simple test/demo
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pretty_print(sample_data, label="sample_data")
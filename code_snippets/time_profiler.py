"""
A Python decorator to measure the execution time of a method ( e.g Django Views etch )

Usage: in a django view

from wnenever.the.decorator.code.is import function_timer

@function_timer()
def home_view(request):
    ...
    return (request, template, context)

"""
from functools import wraps
import time
import logging
logger = logging.getLogger(__name__)

def function_timer(func):
	""" prints the execution time of the decorated function """

	@wraps(func)
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = func(*args, **kwargs)
		t2 = time.time()
		logger.warning("{} run in {}s".format(func.__name__, round(t1 - t2, 2)))
		return result
	return wrapper
#!/usr/bin/python3

"""
| --------------------- Py include <Mauro Baladés> ---------------------
|  ___   _         _   _      __    _     _     ___   ____ 
| | |_) \ \_/     | | | |\ | / /`  | |   | | | | | \ | |_  
| |_|    |_|      |_| |_| \| \_\_, |_|__ \_\_/ |_|_/ |_|__ 
| ----------------------------------------------------------------------
| MIT License
| 
| Copyright (c) 2022 Mauro Baladés
|
| Permission is hereby granted, free of charge, to any person obtaining a copy
| of this software and associated documentation files (the "Software"), to deal
| in the Software without restriction, including without limitation the rights
| to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
| copies of the Software, and to permit persons to whom the Software is
| furnished to do so, subject to the following conditions:
|
| The above copyright notice and this permission notice shall be included in all
| copies or substantial portions of the Software.
|
| THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
| IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
| FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
| AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
| LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
| OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
| SOFTWARE.
|
"""

def _exec_modules(*args, **kwargs):
  pass

def _ret_modules(*args, **kwargs):
  pass

def include(*args, **kwargs):
  """Here is where all the magic ocour. This function takes an
  infinite amount of paths and they are being executend to 
  feel like user imported it.

  Note: 
    It can  also be used to store it into a variable if user
    needs it. This can be done by adding the argument `ret`
    to True (more detail in #Args).

  Note:
    Please note how (for the import statement) you will need a
    `__init__.py` and paths separated by dots. With py-include,
    you don't need. Py-include will make your path supported
    by the current platform and it will open it's content and 
    execute it, so you don't need a path divided by `.` or 
    a `__init__.py`

  Args:
    files [list(str)]: A list of paths to include.
    ret [bool]: If it is set to True, return the module (defaults to False).

  Note: 
    If `ret` is set to `True`, the function will return all modules
    as user will need to unpack them.
  """

  # Get the value whether user whan't to execute
  # the module or to return it. (defaults to False)
  ret = kwargs.get("ret", False)
  
  # Check if user inserted `ret` as True. If it not,
  # we will open the file and execute it's content.
  # If it is True, we will return the module they
  # whanted to import.
  if not ret:
    _exec_modules(*args, **kwargs)

  return _ret_modules(*args, **kwargs)
  

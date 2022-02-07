import unittest
from py_include import include

class ExecuteModuleTest(unittest.TestCase):
  def include_var(self):
    include("./test_module.py", local=locals())
    self.assertEqual(name, 'Include')


if __name__ == '__main__':
  ExecuteModuleTest().include_var()
  
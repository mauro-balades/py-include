import unittest
from py_include import include

class ExecuteModuleTest(unittest.TestCase):
  def include_var(self):
    include("../test/test_module.py")
    self.assertEqual(name, 'Include')


if __name__ == '__main__':
  unittest.main()
  
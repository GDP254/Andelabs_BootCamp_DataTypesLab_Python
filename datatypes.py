import unittest

def data_type(data):
  t = type(data)
  if data is None:
    return 'no value'
  elif t is int:
    if data < 100:
      return 'less than 100'
    elif data > 100:
      return 'more than 100'
    else:
      return 'equal to 100'
  elif t is list:
    if len(data) > 2:
      return data[2]
    else:
      return None
  elif t is str:
    return len(data)
  elif t is bool:
    return data
  else:
    raise ValueError("This function does not support the provided data type")



class DataTypeTestCase(unittest.TestCase):

  def test_none_type(self):
    self.assertEqual('no value', data_type(None))

  def test_array_type(self):
    self.assertEqual(3, data_type([1, 2, 3]))

  def test_small_array_type(self):
    self.assertEqual(None, data_type([1, 2]))

  def test_small_booleans_type(self):
    self.assertEqual(True, data_type(True))

  def test_small_integer_type(self):
    self.assertEqual('less than 100', data_type(3))

  def test_large_integer_type(self):
    self.assertEqual('more than 100', data_type(200))
  
  def test_str_type(self):
    self.assertEqual(6, data_type('andela'))

  def test_float_type(self):
    with self.assertRaises(ValueError):
      data_type(4.5)

if __name__ == "__main__":
  unittest.main()
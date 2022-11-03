import unittest
from string_operations import title_name , join_names

class TestString(unittest.TestCase):
    
    def test_string(self):
        self.assertEqual(title_name('nadia', 'vali'), '(Nadia Vali)')
        self.assertEqual(join_names(['nadia','vali']), 'nadia vali')


if __name__=='__main__':
    unittest.main()
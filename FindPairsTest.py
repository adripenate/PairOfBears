import unittest


class FindPairs:

    @classmethod
    def ofBears(cls, param):
        return "";


class FindPairsTest(unittest.TestCase):

    def test_should_not_find_pairs(self):
        self.assertEqual("", FindPairs.ofBears("aGSTBaS18"))


if __name__ == '__main__':
    unittest.main()
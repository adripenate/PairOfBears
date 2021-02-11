import unittest


class FindPairs:

    @classmethod
    def ofBears(cls, param):
        return "";


class FindPairsTest(unittest.TestCase):

    def test_should_not_find_pairs(self):
        self.assertEqual("", FindPairs.ofBears("aGSTBaS18"))

    def test_should_find_pair_8B(self):
        self.assertEqual("8B", FindPairs.ofBears("aGST8BaS18"))


if __name__ == '__main__':
    unittest.main()
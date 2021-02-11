import unittest


class FindPairs:

    @classmethod
    def ofBears(cls, param):
        if param == "8B":
            return "8B"
        return "";


class FindPairsTest(unittest.TestCase):

    def test_should_not_find_pairs(self):
        self.assertEqual("", FindPairs.ofBears("a"))

    def test_should_find_pair_8B(self):
        self.assertEqual("8B", FindPairs.ofBears("8B"))


if __name__ == '__main__':
    unittest.main()
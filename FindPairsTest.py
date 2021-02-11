import unittest


class FindPairs:

    @classmethod
    def ofBears(cls, param):
        for position in range(1, len(param)):
            target = param[position-1] + param[position]
            if target == "8B":
                return "8B"
            if target == "B8":
                return "B8"
        return ""


class FindPairsTest(unittest.TestCase):

    def test_should_not_find_pairs(self):
        self.assertEqual("", FindPairs.ofBears("a"))

    def test_should_find_pair_8B(self):
        self.assertEqual("8B", FindPairs.ofBears("8B"))

    def test_should_find_pair_B8(self):
        self.assertEqual("B8", FindPairs.ofBears("B8"))

    def test_should_find_pair_8B_in_long_chains(self):
        self.assertEqual("8B", FindPairs.ofBears("a28Bsdf3w"))


if __name__ == '__main__':
    unittest.main()
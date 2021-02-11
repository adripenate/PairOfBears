import unittest

PAIR_TYPE_1 = "8B"
PAIR_TYPE_2 = "B8"


class FindPairs:

    @classmethod
    def ofBears(cls, bears):
        pairs = ""
        position = 1
        while position < len(bears):
            target = bears[position - 1] + bears[position]
            if target == PAIR_TYPE_1 or target == PAIR_TYPE_2:
                pairs += target
                position += 1
            position += 1
        return pairs


class FindPairsTest(unittest.TestCase):

    def test_should_not_find_pairs(self):
        self.assertEqual("", FindPairs.ofBears("a"))

    def test_should_find_pair_8B(self):
        self.assertEqual("8B", FindPairs.ofBears("8B"))

    def test_should_find_pair_B8(self):
        self.assertEqual("B8", FindPairs.ofBears("B8"))

    def test_should_find_pair_8B_in_long_chains(self):
        self.assertEqual("8B", FindPairs.ofBears("a28Bsdf3w"))

    def test_should_find_multiple_pairs(self):
        self.assertEqual("8BB8", FindPairs.ofBears("a2Bs8BdB8f3w"))

    def test_should_not_find_more_than_one_pair(self):
        self.assertEqual("B8", FindPairs.ofBears("a2BsB8Bdf3w"))


if __name__ == '__main__':
    unittest.main()
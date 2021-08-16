import unittest
import WordBucket


class WordBucketTest(unittest.TestCase):

    def test_getString_to_arrayOfword(self):
        string_to_split = "she sells sea shells by the sea"
        self.assertEqual(string_to_split.split(), ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea'])

    def test_cut_last_character(self):
        self.assertEqual(WordBucket.cut_last_character("me "), "me")

    def test_bucketize(self):
        self.assertEqual(WordBucket.bucketize("she sells sea shells by the sea", 10),
                         ["she sells", "sea shells", "by the sea"])
        self.assertEqual(WordBucket.bucketize("the mouse jumped over the cheese", 7),
                         ["the", "mouse", "jumped", "over", "the", "cheese"])
        self.assertEqual(WordBucket.bucketize("fairy dust coated the air", 20), ["fairy dust coated", "the air"])
        self.assertEqual(WordBucket.bucketize("a b c d e", 2), ["a", "b", "c", "d", "e"])


if __name__ == '__main__':
    unittest.main()

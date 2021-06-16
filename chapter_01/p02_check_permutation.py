# O(N)
import unittest
from collections import Counter


def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def check_permutation_by_count(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256
    for c in str1:
        counter[ord(c)] += 1
    for c in str2:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1
    return True

#sliding window algorithm - TC: O(n+m)
def find_permutation(str, pattern):
      window_start, matched = 0, 0
      char_frequency = {}

      for chr in pattern:
        if chr not in char_frequency:
          char_frequency[chr] = 0
        char_frequency[chr] += 1

      # our goal is to match all the characters from the 'char_frequency' with the current window
      # try to extend the range [window_start, window_end]
      for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
          # decrement the frequency of matched character
          char_frequency[right_char] -= 1
          if char_frequency[right_char] == 0:
            matched += 1

        if matched == len(char_frequency):
          return True

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
          left_char = str[window_start]
          window_start += 1
          if left_char in char_frequency:
            if char_frequency[left_char] == 0:
              matched -= 1
            char_frequency[left_char] += 1

      return False
    
def check_permutation_pythonic(str1, str2):
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)


class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        check_permutation_by_sort,
        check_permutation_by_count,
        check_permutation_pythonic,
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()

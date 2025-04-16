# Anagram string
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

def anagram_string(strs):
    result_dict = defaultdict(list)
    for word in strs:
        new_word = ''.join(sorted(word))
        result_dict[new_word].append(word)
    return list(result_dict.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = anagram_string(strs)
print(result)
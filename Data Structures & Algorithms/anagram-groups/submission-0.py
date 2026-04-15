class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anograms = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in anograms:
                anograms[key] = []
            anograms[key].append(word)
        return list(anograms.values())
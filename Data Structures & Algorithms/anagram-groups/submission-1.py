class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedDict = defaultdict(list)
        for i in strs:
            j = "".join(sorted(i))
            sortedDict[j].append(i)
        return list(sortedDict.values())
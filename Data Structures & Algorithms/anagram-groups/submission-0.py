class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedDict = {}
        for i in strs:
            j = "".join(sorted(i))
            if j not in sortedDict:
                sortedDict[j] = [i] 
            else:
                sortedDict[j].append(i)
        return list(sortedDict.values())
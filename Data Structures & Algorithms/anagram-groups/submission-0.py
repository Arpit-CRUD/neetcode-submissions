class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
           sorted_s="".join(sorted(s))

           if sorted_s not in hmap:
            hmap[sorted_s]=[]
           
           hmap[sorted_s].append(s)
        return list(hmap.values())
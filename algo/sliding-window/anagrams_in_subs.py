"""https://leetcode.com/problems/find-all-anagrams-in-a-string/"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slow = fast = counter = 0
        plen = len(p)
        result = []
        # Store counter of the target string.
        pmap = {}
        for i in p:
            pmap[i] = pmap.get(i, 0) + 1
        # smap keeps the current window counter
        # i.e. all characters in s[slow:fast] counter is stored in smap
        smap = {}

        while fast < len(s):
            c = s[fast]
            smap[c] = smap.get(c, 0) + 1
            counter += 1
            if counter == plen:
                # If both pmap and smap matches, we got one result
                if smap == pmap:
                    result.append(slow)
                # Since we are going to increment slow, decrease it's counter in smap
                smap[s[slow]] -= 1
                # < 0? Pop it because it's not part of window anymore
                if smap[s[slow]] <= 0:
                    smap.pop(s[slow])
                counter -= 1
                slow += 1
            fast += 1
        return result

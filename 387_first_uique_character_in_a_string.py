class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = 0
        # letter = s[0]
        count = {}
        # for i in range(0, len(s)):
        for j in s:
            if j in count:
                count[j] += 1
            else:
                count [j] = 1

        print(s)
        for i in count:
            # print(count[i])
            if count[i] == 1:
                return s.index(i)
        return -1
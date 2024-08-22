class Solution:
    def hIndex(self, citations: list[int]) -> int:
        if citations.count(0) == len(citations) or not citations:
            return 0
        else:
            citations.sort(reverse=True)
            counter = 0
            for i in range(len(citations)):
                if citations[i] >= (counter + 1):
                    counter += 1
        return counter
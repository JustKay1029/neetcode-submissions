import itertools
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        x = max(count_dict, key=count_dict.get)
        output = []
        sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
        for key in itertools.islice(sorted_dict, k):
            output.append(key)
        return output 




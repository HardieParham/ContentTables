# groupA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sumA = 9

# groupB = [1, 2, 4, 5]
# sumB = 9



# {1: 8, 2: 7, 4: 5, 5: 4}


# def sum_checking_loop(group, sum):
#     pairs = []
#     cache = {}
#     for i in group:
#         if i in cache.keys():
#             j = cache[i]
#             pairs.append((j, i))

#         else:
#             key = sum - i
#             cache[key] = i


#     return pairs


    # print(sum_checking_loop(groupA, sumA))
    # print(sum_checking_loop(groupB, sumB))




class Grouping():
    def __init__(self, target: int, group: list):
        self.target = target
        self.group = group
        self.pairs = []
        self.cache = {}

        self.target_check()
        self.get_pairs()

    def target_check(self):
        for i in self.group:
            if i in self.cache.keys():
                j = self.cache[i]
                self.pairs.append((i, j))

            else:
                key = self.target - i
                self.cache[key] = i


    def get_pairs(self):
        if len(self.pairs) == 0:
            print('No Pairs')
        else:
            for pair in self.pairs:
                print(pair)

    
if __name__ == "__main__":
    Grouping(8, [1, 2, 4, 5])
    Grouping(9, [1, 2, 3, 4, 5, 6, 7, 8, 9])
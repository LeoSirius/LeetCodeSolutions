from typing import *
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        mapper = {}  # k is table number, value is a sub dict
        food_names = set()
        for order in orders:
            table_no = int(order[1])
            food_name = order[2]
            food_names.add(food_name)
            if table_no not in mapper:
                mapper[table_no] = defaultdict(int)
            mapper[table_no][food_name] += 1

        food_names = sorted(list(food_names))
        row1 = ['Table'] + food_names
        res = [row1]

        for table_no, sub_dict in sorted(mapper.items()):
            row = [str(table_no)]
            for food_name in food_names:
                row.append(str(sub_dict[food_name]))
            res.append(row)
        return res


def test(test_name, orders, expected):
    res = Solution().displayTable(orders)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    orders1 = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
    expected1 = [
        ["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],
        ["3","0","2","1","0"],
        ["5","0","1","0","1"],
        ["10","1","0","0","0"]]
    test('test1', orders1, expected1)

    orders2 = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
    expected2 = [
        ["Table","Canadian Waffles","Fried Chicken"],
        ["1","2","0"],
        ["12","0","3"]]
    test('test2', orders2, expected2)

    orders3 = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
    expected3 = [
        ["Table","Bean Burrito","Beef Burrito","Soda"],
        ["2","1","1","1"]]
    test('test3', orders3, expected3)




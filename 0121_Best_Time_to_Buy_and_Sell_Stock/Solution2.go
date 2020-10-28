package main

import (
	"fmt"
)

func maxProfit(prices []int) int {
	res := 0
	if len(prices) <= 1 {
		return res
	}

	curMin := prices[0]
	for i := 1; i < len(prices); i++ {
		if curMin > prices[i] {
			curMin = prices[i]
		}
		if res < prices[i] - curMin {
			res = prices[i] - curMin
		}
	}
	return res
}


func test(testName string, prices []int, expected int) {
	res := maxProfit(prices)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}


func main() {
	prices1 := []int{7,1,5,3,6,4}
	expected1 := 5
	test("test1", prices1, expected1)

	prices2 := []int{7,6,4,3,1}
	expected2 := 0
	test("test2", prices2, expected2)

}

// Example 1:

// Input: [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
//              Not 7-1 = 6, as selling price needs to be larger than buying price.
// Example 2:

// Input: [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transaction is done, i.e. max profit = 0.

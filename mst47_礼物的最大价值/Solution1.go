package main

import (
	"fmt"
)

func maxValue(grid [][]int) int {
	m, n := len(grid), len(grid[0])

	// init 2-d slice, copy from grid
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
		copy(dp[i], grid[i])
	}

	// 初始化第一列和第一行
	for i := 1; i < m; i++ {
		dp[i][0] += dp[i-1][0]
	}
	for j := 1; j < n; j++ {
		dp[0][j] += dp[0][j-1]
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if dp[i-1][j] < dp[i][j-1] {
				dp[i][j] += dp[i][j-1]
			} else {
				dp[i][j] += dp[i-1][j]
			}
		}
	}
	return dp[m-1][n-1]
}

func test(testName string, grid [][]int, expected int) {
	res := maxValue(grid)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	grid1 := [][]int {
		{1,3,1},
		{1,5,1},
		{4,2,1},
	}
	expected1 := 12
	test("test1", grid1, expected1)

}

// 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
// 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
// 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

// 示例 1:
// 输入: 
// [
//   [1,3,1],
//   [1,5,1],
//   [4,2,1]
// ]
// 输出: 12

// 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
//  
// 提示：
// 0 < grid.length <= 200
// 0 < grid[0].length <= 200
package main

import (
	"fmt"
)

func isValidSudoku(board [][]byte) bool {
	usedRows := make([][]int, 9)
	usedCols := make([][]int, 9)
	usedSqrs := make([][]int, 9)
	for i := range usedRows {
		usedRows[i] = make([]int, 9)
		usedCols[i] = make([]int, 9)
		usedSqrs[i] = make([]int, 9)
	}

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[i][j] == '.' {continue}
			k := i / 3 * 3 + j / 3
			n := int(board[i][j]) - int('0') - 1
			if usedRows[i][n] == 1 || usedCols[j][n] == 1 || usedSqrs[k][n] == 1 {
				return false
			}
			usedRows[i][n] = 1
			usedCols[j][n] = 1
			usedSqrs[k][n] = 1
		}
	}
	return true
}

func test(testName string, board [][]byte, expected bool) {
	res := isValidSudoku(board)
	if res == expected {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	board1 := [][]byte{
		{'5','3','.','.','7','.','.','.','.'},
		{'6','.','.','1','9','5','.','.','.'},
		{'.','9','8','.','.','.','.','6','.'},
		{'8','.','.','.','6','.','.','.','3'},
		{'4','.','.','8','.','3','.','.','1'},
		{'7','.','.','.','2','.','.','.','6'},
		{'.','6','.','.','.','.','2','8','.'},
		{'.','.','.','4','1','9','.','.','5'},
		{'.','.','.','.','8','.','.','7','9'},
	}
	expected1 := true
	test("test1", board1, expected1)

	board2 := [][]byte{
		{'8','3','.','.','7','.','.','.','.'},
		{'6','.','.','1','9','5','.','.','.'},
		{'.','9','8','.','.','.','.','6','.'},
		{'8','.','.','.','6','.','.','.','3'},
		{'4','.','.','8','.','3','.','.','1'},
		{'7','.','.','.','2','.','.','.','6'},
		{'.','6','.','.','.','.','2','8','.'},
		{'.','.','.','4','1','9','.','.','5'},
		{'.','.','.','.','8','.','.','7','9'},
	}
	expected2 := false
	test("test2", board2, expected2)

}

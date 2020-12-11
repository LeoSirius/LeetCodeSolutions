package main

import (
	"fmt"
	"reflect"
)

func rotate(matrix [][]int) {
	for i, j := 0, len(matrix)-1; i < j; i, j = i+1, j-1 {
		matrix[i], matrix[j] = matrix[j], matrix[i]
	}

	for i := 0; i < len(matrix); i++ {
		for j := i+1; j < len(matrix); j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
}


func test(testName string, matrix [][]int, expected [][]int) {
	rotate(matrix)
	if reflect.DeepEqual(matrix, expected) {
		fmt.Println(testName + " success.")
	} else {
		fmt.Println(testName + " failed.")
	}
}

func main() {
	matrix1 := [][]int{
		{1,2,3},
		{4,5,6},
		{7,8,9},
	}
	expected1 := [][]int{
		{7,4,1},
		{8,5,2},
		{9,6,3},
	}
	test("test1", matrix1, expected1)

	matrix2 := [][]int{
		{5, 1, 9,11},
		{2, 4, 8,10},
		{13, 3, 6, 7},
		{15,14,12,16},
	}
	expected2 := [][]int{
	{15,13, 2, 5},
	{14, 3, 4, 1},
	{12, 6, 8, 9},
	{16, 7,10,11},
	}
	test("test2", matrix2, expected2)

}

// 给定一个 n × n 的二维矩阵表示一个图像。

// 将图像顺时针旋转 90 度。

// 说明：

// 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

// 示例 1:

// 给定 matrix = 
// [
//   [1,2,3],
//   [4,5,6],
//   [7,8,9]
// ],

// 原地旋转输入矩阵，使其变为:
// [
//   [7,4,1],
//   [8,5,2],
//   [9,6,3]
// ]
// 示例 2:

// 给定 matrix =
// [
//   [ 5, 1, 9,11],
//   [ 2, 4, 8,10],
//   [13, 3, 6, 7],
//   [15,14,12,16]
// ], 

// 原地旋转输入矩阵，使其变为:
// [
//   [15,13, 2, 5],
//   [14, 3, 4, 1],
//   [12, 6, 8, 9],
//   [16, 7,10,11]
// ]


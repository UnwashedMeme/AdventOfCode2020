package main

import (
	"bufio"
	"fmt"
//	"log"
	"os"
	"strconv"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func readfile() ([]int) {
	f, err := os.Open("input")
	defer f.Close()
	check(err)
	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)
	var numbers []int
	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())
		check(err)
		numbers = append(numbers, i)
	}
	return numbers
}

func main() {
	numbers := readfile()
	count := len(numbers)
	for idx1, i := range numbers[0:count-2] {
		for idx2, j := range numbers[idx1 + 1:count-1] {
			if i + j == 2020 {
				fmt.Println(i * j)
			} else if (i + j < 2020) {
				for _, k := range numbers[idx2 + 1:count] {
					if i + j + k == 2020 {
						fmt.Println(i * j * k)
					}
				}
			}
		}
	}
}

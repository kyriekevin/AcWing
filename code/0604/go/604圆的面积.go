package main

import "fmt"

func main() {
	const pi = 3.14159
	var r float64
	fmt.Scanln(&r)
	fmt.Printf("A=%.4f", pi*r*r)
}

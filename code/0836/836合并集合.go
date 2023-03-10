package main

import (
	"bufio"
	"fmt"
	"os"
)

const N int = 100010

var p [N]int

func find(x int) int {
	if p[x] != x {
		p[x] = find(p[x])
	}

	return p[x]
}

func main() {
	out := bufio.NewWriter(os.Stdout)
	in := bufio.NewReader(os.Stdin)
	defer out.Flush()

	var n, m int
	fmt.Fscan(in, &n, &m)

	for i := 0; i < N; i++ {
		p[i] = i
	}

	for ; m > 0; m-- {
		var op string
		var a, b int

		fmt.Fscan(in, &op, &a, &b)
		a, b = find(a), find(b)
		if op == "M" {
			p[a] = b
		} else {
			if a == b {
				fmt.Fprintln(out, "Yes")
			} else {
				fmt.Fprintln(out, "No")
			}
		}
	}
}

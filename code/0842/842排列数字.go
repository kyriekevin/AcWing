package main

import "fmt"

const N = 10

var g [N]int
var st [N]bool

func dfs(u, n int) {
	if u == n {
		for i := 0; i < n; i++ {
			fmt.Printf("%d ", g[i])
		}
		fmt.Println("")
		return
	}

	for i := 1; i <= n; i++ {
		if st[i] == false {
			st[i] = true
			g[u] = i
			dfs(u+1, n)
			st[i] = false
		}
	}
}

func main() {
	var n int
	fmt.Scan(&n)
	dfs(0, n)
}

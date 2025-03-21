func numJewelsInStones(jewels string, stones string) int {
    jewelSet := make(map[rune]bool)
    count := 0

    for _, j := range jewels {
        jewelSet[j] = true
    }

    for _, s := range stones {
        if jewelSet[s] {
            count++
        }
    }

    return count
}

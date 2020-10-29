def solution(n: int = 1000) -> int:
    """Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """

    count = 0
    total = 0

    while True:
        count += 1
        if count == n:
            break
        digits = str(count)
        if sum(int(digit) for digit in digits) % 3 == 0:
            total += count
        elif digits[-1] == "0" or digits[-1] == "5" :
            total += count


    return total

print(solution())
def find_num(n):
    if n < 10:
        return n

    seq = list(range(11))  # 0..10 already known
    used = set(seq)
    forbidden = set(str(seq[-1]))

    while len(seq) <= n:
        candidate = 0
        while True:
            if candidate not in used and is_valid(candidate, forbidden):
                seq.append(candidate)
                used.add(candidate)
                forbidden = set(str(candidate))
                break
            candidate += 1

    return seq[n]


def is_valid(num, forbidden):
    return not any(d in forbidden for d in str(num))

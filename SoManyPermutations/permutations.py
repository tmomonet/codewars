def permutations(s):
    results = set() #handles duplicates
    def backtrack(path, remaining):
        #if nothing left, permutation is complete
        if not remaining:
            results.add(path)
            return

        #handles duplicate characters on successive recursions
        used  = set()
        for i, ch in enumerate(remaining):
            if ch in used:
                continue
            used.add(ch)
            backtrack(path + ch, remaining[:i] + remaining[i+1:])
        
    backtrack("", s)
    return results  

### Community Solution
# import itertools

# def permutations(string):
#     return list("".join(p) for p in set(itertools.permutations(string)))

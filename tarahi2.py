def word_break(s, word_dict):
    # print(word_set)
    n = len(s)
    dp = [False] * (n + 1)
    # print(dp)
    dp[0] = True
    backtrack = [-1] * (n + 1)
    # print(backtrack)

    for i in range(1, n + 1):
        for j in range(i):

            if dp[j] and s[j:i] in word_dict:
                # print(s[j:i], '...')
                # print(dp[j])
                dp[i] = True

                backtrack[i] = j
                break

    if not dp[n]:
        return False, ""

    # Reconstruct the solution
    result = []
    idx = n
    while idx > 0:
        result.append(s[backtrack[idx]:idx])
        print(s[backtrack[idx]:idx])
        idx = backtrack[idx]
        # print(result)
        # print(idx)

    result.reverse()
    return True, " ".join(result)


# Example usage
dictionary = {"i", "like", "sam", "sung", "samsung", "s"}
input_string = input('enter your word:')
can_break, segmented_string = word_break(input_string, dictionary)
# print(can_break)
# print(segmented_string)
if can_break:
    print(f'yes you can write "{segmented_string}"')  # Output: "i like samsung"
else:
    print("Cannot be segmented")

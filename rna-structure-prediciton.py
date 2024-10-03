def predict_secondary_structure(rna_sequence):
    n = len(rna_sequence)

    # Step 2: Initialization
    DP = [[0] * n for _ in range(n)]

    # Step 3: Base Case
    for i in range(n):
        DP[i][i] = 0

    # Print initial DP matrix
    print("Initial Dynamic Programming Matrix:")
    for row in DP:
        print(row)

    # Step 4: Dynamic Programming Loop
    for k in range(1, n):
        for i in range(n - k):
            j = i + k

            # Step 5: Recurrence Relation
            case1 = DP[i + 1][j]
            case2 = 1 + DP[i + 1][j - 1] if (rna_sequence[i], rna_sequence[j]) in [('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G')] else 0

            # Handle the case when the iterable is empty
            case3_candidates = [DP[i][k] + DP[k + 1][j] for k in range(i + 1, j)]
            case3 = max(case3_candidates) if case3_candidates else 0

            DP[i][j] = max(case1, case2, case3)

            # Print the current DP matrix
            print(f"\nDynamic Programming Matrix at k={k}, i={i}, j={j}:")
            for row in DP:
                print(row)

    # Step 6: Backtracking
    secondary_structure = backtrack(0, n - 1, rna_sequence, DP)

    print("\nPredicted Secondary Structure:")
    print(rna_sequence)
    print(secondary_structure)


def backtrack(i, j, rna_sequence, DP):
    if i >= j:
        return ""
    
    # Check which case led to the current DP value
    if DP[i][j] == DP[i + 1][j]:
        return "." + backtrack(i + 1, j, rna_sequence, DP)
    elif DP[i][j] == 1 + DP[i + 1][j - 1] and (rna_sequence[i], rna_sequence[j]) in [('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G')]:
        return "(" + backtrack(i + 1, j - 1, rna_sequence, DP) + ")"
    else:
        for k in range(i + 1, j):
            if DP[i][j] == DP[i][k] + DP[k + 1][j]:
                return backtrack(i, k, rna_sequence, DP) + backtrack(k + 1, j, rna_sequence, DP)


# Example
rna_sequence = "AGCUUAGC"
predict_secondary_structure(rna_sequence)

# Define a function to perform the Needleman-Wunsch algorithm for global sequence alignment
def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-1):
    # Initialize the scoring matrix
    rows, cols = len(seq1) + 1, len(seq2) + 1
    matrix = [[0] * cols for _ in range(rows)]

    # Initialize the traceback matrix
    traceback = [[0] * cols for _ in range(rows)]

    # Initialize the first row and column of the scoring matrix with gap penalties
    for i in range(rows):
        matrix[i][0] = i * gap
        traceback[i][0] = 'U'  # U for up

    for j in range(cols):
        matrix[0][j] = j * gap
        traceback[0][j] = 'L'  # L for left

    # Fill in the scoring matrix and traceback matrix
    for i in range(1, rows):
        for j in range(1, cols):
            # Calculate the match/mismatch score based on the characters at the corresponding positions
            match_mismatch_score = match if seq1[i - 1] == seq2[j - 1] else mismatch

            # Calculate three possible scores for the current position
            scores = [matrix[i - 1][j - 1] + match_mismatch_score,
                      matrix[i - 1][j] + gap,
                      matrix[i][j - 1] + gap]

            # Fill in the scoring matrix with the maximum of the three scores
            matrix[i][j] = max(scores)

            # Update the traceback matrix based on the chosen direction
            if matrix[i][j] == scores[0]:
                traceback[i][j] = 'D'  # D for diagonal
            elif matrix[i][j] == scores[1]:
                traceback[i][j] = 'U'  # U for up
            else:
                traceback[i][j] = 'L'  # L for left

    # Perform traceback to find the aligned sequences
    aligned_seq1, aligned_seq2 = '', ''
    i, j = rows - 1, cols - 1

    while i > 0 or j > 0:
        # Follow the traceback path to reconstruct the aligned sequences
        if traceback[i][j] == 'D':
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1
            j -= 1
        elif traceback[i][j] == 'U':
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1

    # Print the scoring matrix, traceback matrix, and aligned sequences
    print("Scoring Matrix:")
    for row in matrix:
        print(row)

    print("\nTraceback Matrix:")
    for row in traceback:
        print(row)

    print("\nAligned Sequences:")
    print(aligned_seq1)
    print(aligned_seq2)

# Example usage:
seq1 = "AGTACGCA"
seq2 = "TATGC"
needleman_wunsch(seq1, seq2)

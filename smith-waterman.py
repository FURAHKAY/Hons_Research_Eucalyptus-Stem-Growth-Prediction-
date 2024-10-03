# Define a function to perform the Smith-Waterman algorithm for local sequence alignment
def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap=-1):
    # Initialize the scoring matrix
    rows, cols = len(seq1) + 1, len(seq2) + 1
    matrix = [[0] * cols for _ in range(rows)]

    # Initialize the traceback matrix
    traceback = [['' for _ in range(cols)] for _ in range(rows)]

    # Initialize variables to track the maximum score and its position
    max_score = 0
    max_i, max_j = 0, 0

    # Fill in the scoring matrix and traceback matrix
    for i in range(1, rows):
        for j in range(1, cols):
            # Calculate match/mismatch score based on characters at corresponding positions
            match_mismatch_score = match if seq1[i - 1] == seq2[j - 1] else mismatch

            # Calculate four possible scores for the current position
            scores = [matrix[i - 1][j - 1] + match_mismatch_score,
                      matrix[i - 1][j] + gap,
                      matrix[i][j - 1] + gap,
                      0]  # Reset to 0 if negative

            # Update the scoring matrix with the maximum of the four scores
            matrix[i][j] = max(scores)

            # Update the traceback matrix based on the chosen directions
            if matrix[i][j] == scores[0]:
                traceback[i][j] += 'D'  # D for diagonal
            if matrix[i][j] == scores[1]:
                traceback[i][j] += 'U'  # U for up
            if matrix[i][j] == scores[2]:
                traceback[i][j] += 'L'  # L for left

            # Track the position of the maximum score
            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_i, max_j = i, j

    # Perform traceback to find the aligned sequences
    aligned_seq1, aligned_seq2 = '', ''

    i, j = max_i, max_j
    while i > 0 and j > 0 and matrix[i][j] > 0:
        # Follow the traceback path to reconstruct the aligned sequences
        if 'D' in traceback[i][j]:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1
            j -= 1
        elif 'U' in traceback[i][j]:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1
        elif 'L' in traceback[i][j]:
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
seq1 = "TACGGGCCCGCTAC"
seq2 = "TAGCCCTATCGGTCA"
smith_waterman(seq1, seq2)

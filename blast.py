import numpy as np

# def blast_algorithm(query, database):
#     # Step 3: Seed Matches
#     seed_length = 3
#     for i in range(len(query) - seed_length + 1):
#         seed = query[i:i+seed_length]
#         print(f"\nStep 3: Seed Finding - Query Seed: {seed}")

#         # Step 4: Scoring
#         scores = [1 if a == b else -1 for a, b in zip(seed, database)]
#         print(f"Step 4: Scoring - Scores: {scores}")

#         # Step 5: High-Scoring Pairs
#         max_score_index = np.argmax(scores)
#         hsp_start = max(0, max_score_index - seed_length + 1)
#         hsp_end = min(len(database), max_score_index + seed_length)
#         hsp = database[hsp_start:hsp_end]
#         print(f"Step 5: High-Scoring Pairs (HSP) - Query HSP: {hsp}")

#         # Step 6: Extension
#         print("Step 6: Extension - Extending the HSP")

#         # Step 7: Evaluation (not implemented in this simplified example)

#         # Step 8: Report Results
#         print("Step 8: Report Results - Reporting the significant match")

# # Example
# query_sequence = "ATTAGC"
# database_sequence = "ATAGGCATGC"

# blast_algorithm(query_sequence, database_sequence)


# def blast_algorithm(query, database):
#     seed_length = 3

#     # Step 3: Seed Matches
#     for i in range(len(query) - seed_length + 1):
#         seed = query[i:i + seed_length]
#         print(f"\nStep 3: Seed Finding - Query Seed: {seed} (Position: {i})")

#         # Step 4: Scoring
#         scores = [1 if a == b else -1 for a, b in zip(seed, database)]
#         print(f"Step 4: Scoring - Scores: {scores}")

#         # Step 5: High-Scoring Pairs
#         max_score_index = scores.index(max(scores))
#         hsp_start = max(0, max_score_index - seed_length + 1)
#         hsp_end = min(len(database), max_score_index + seed_length)
#         hsp = database[hsp_start:hsp_end]
#         print(f"Step 5: High-Scoring Pairs (HSP) - Query HSP: {hsp}")

#         # Print Matching Seeds and Positions
#         matching_seeds = [query[j:j + seed_length] for j in range(i, i + seed_length)]
#         matching_positions = list(range(i, i + seed_length))
#         print(f"    Matching Seeds: {matching_seeds} (Positions: {matching_positions})")

#         # Step 6: Extension
#         print("Step 6: Extension - Extending the HSP")

#         # Step 7: Evaluation (not implemented in this simplified example)

#         # Step 8: Report Results
#         print("Step 8: Report Results - Reporting the significant match")

# # Example
# query_sequence = "ATTAGC"
# database_sequence = "ATAGGCATGC"

# blast_algorithm(query_sequence, database_sequence)
# def blast_algorithm(query, database):
#     seed_length = 3
#     num_iterations = len(query) - seed_length + 1

#     # Arrays to store information for each iteration
#     all_seeds = []
#     all_matching_seeds = []
#     all_scores = []

#     for i in range(num_iterations):
#         seed = query[i:i + seed_length]
#         all_seeds.append(seed)

#         # Print Matching Seeds
#         matching_seeds = [query[j:j + seed_length] for j in range(i, i + seed_length)]
#         matching_positions = list(range(i, i + seed_length))
#         all_matching_seeds.append(matching_seeds)

#         # Step 3: Seed Finding
#         print(f"\nStep 3: Seed Finding - Query Seed: {seed} (Position: {i})")
#         print(f"    All Seeds: {all_seeds}")

#         # Step 4: Scoring
#         scores = [1 if a == b else -1 for a, b in zip(seed, database)]
#         all_scores.append(scores)
#         print(f"Step 4: Scoring - Scores: {scores}")
#         print(f"    All Scores: {all_scores}")

#         # Step 5: High-Scoring Pairs
#         max_score_index = scores.index(max(scores))
#         hsp_start = max(0, max_score_index - seed_length + 1)
#         hsp_end = min(len(database), max_score_index + seed_length)
#         hsp = database[hsp_start:hsp_end]
#         print(f"Step 5: High-Scoring Pairs (HSP) - Query HSP: {hsp}")

#         # Print Matching Seeds
#         print(f"    Matching Seeds: {matching_seeds} (Positions: {matching_positions})")
#         print(f"    All Matching Seeds: {all_matching_seeds}")

#         # Step 6: Extension
#         print("Step 6: Extension - Extending the HSP")

#         # Step 7: Evaluation (not implemented in this simplified example)

#         # Step 8: Report Results
#         print("Step 8: Report Results - Reporting the significant match")

# # Example
# query_sequence = "ATTAGC"
# database_sequence = "ATAGGCATGC"

# blast_algorithm(query_sequence, database_sequence)


# Define a function to extract seeds and their positions from a sequence
def get_seeds(seq, seed_length):
    seeds = []
    positions = []
    for i in range(len(seq) - seed_length + 1):
        seed = seq[i:i + seed_length]
        seeds.append(seed)
        positions.append(i)
    return seeds, positions

# Define a function to perform BLAST alignment
def blast_alignment(seq1, seq2, seed_length=3, match=1, mismatch=-1, gap_open=-1, gap_extend=-0.5, threshold=5):
    # Get seeds and their positions for both sequences
    seeds_seq1, positions_seq1 = get_seeds(seq1, seed_length)
    seeds_seq2, positions_seq2 = get_seeds(seq2, seed_length)

    # Initialize the scoring matrix
    rows, cols = len(seeds_seq1) + 1, len(seeds_seq2) + 1
    matrix = [[0] * cols for _ in range(rows)]

    # Fill in the scoring matrix
    for i in range(1, rows):
        for j in range(1, cols):
            seed1, pos1 = seeds_seq1[i - 1], positions_seq1[i - 1]
            seed2, pos2 = seeds_seq2[j - 1], positions_seq2[j - 1]

            # Calculate the score for the current seed pair
            score = 0
            for k in range(seed_length):
                if seed1[k] == seed2[k]:
                    score += match
                else:
                    score += mismatch

            # Fill in the scoring matrix using the maximum score of three possibilities
            matrix[i][j] = max(matrix[i - 1][j] + gap_open, matrix[i][j - 1] + gap_open,
                              matrix[i - 1][j - 1] + score, 0)

    # Find high-scoring seeds
    high_scoring_seeds = []
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] >= threshold:
                high_scoring_seeds.append((seeds_seq1[i - 1], positions_seq1[i - 1], seeds_seq2[j - 1], positions_seq2[j - 1]))

    # Print high-scoring seeds
    print("High-Scoring Seeds:")
    for seed in high_scoring_seeds:
        print(seed)

    # Print scoring matrix
    print("\nScoring Matrix:")
    for row in matrix:
        print(row)

    # Perform traceback to find the aligned sequences
    aligned_seq1, aligned_seq2 = '', ''
    max_i, max_j = max(((i, j) for i in range(rows) for j in range(cols)), key=lambda x: matrix[x[0]][x[1]])

    while matrix[max_i][max_j] > 0:
        if matrix[max_i][max_j] == matrix[max_i - 1][max_j] + gap_open:
            # Gap in sequence 2
            aligned_seq1 = seq1[positions_seq1[max_i - 1]:positions_seq1[max_i - 1] + seed_length] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            max_i -= 1
        elif matrix[max_i][max_j] == matrix[max_i][max_j - 1] + gap_open:
            # Gap in sequence 1
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[positions_seq2[max_j - 1]:positions_seq2[max_j - 1] + seed_length] + aligned_seq2
            max_j -= 1
        else:
            # Match or mismatch
            aligned_seq1 = seq1[positions_seq1[max_i - 1]:positions_seq1[max_i - 1] + seed_length] + aligned_seq1
            aligned_seq2 = seq2[positions_seq2[max_j - 1]:positions_seq2[max_j - 1] + seed_length] + aligned_seq2
            max_i -= 1
            max_j -= 1

    # Print aligned sequences
    print("\nAligned Sequences:")
    print(aligned_seq1)
    print(aligned_seq2)

# Example usage:
seq1 = "TACGGGCCCGCTAC"
seq2 = "TAGCCCTATCGGTCA"
blast_alignment(seq1, seq2)

# import numpy as np
# import random
# import math
# from collections import defaultdict
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Given data
# otu_counts = {
#     'A': [10, 20, 30, 20, 10],
#     'B': [2, 20, 17, 3, 15],
#     'C': [40, 2, 10, 5, 30],
#     'D': [17, 19, 21, 23, 18],
#     'E': [24, 14, 5, 17, 27]
# }

# # Function to perform bootstrapped OTU estimates
# def bootstrap_otu_estimates(otu_counts, sample_size=50, iterations=10000):
#     # Initialize dictionary to store OTU estimates for each sample
#     otu_estimates = {sample: [] for sample in otu_counts}

#     for sample in otu_counts:
#         # Create a list of contigs based on OTU counts
#         contigs = []
#         for i, count in enumerate(otu_counts[sample]):
#             contigs.extend([i+1] * count)
        
#         # Perform the specified number of iterations
#         for _ in range(iterations):
#             # Randomly sample 50 contigs
#             sampled_contigs = random.choices(contigs, k=sample_size)
#             # Count the number of unique OTUs in the sampled contigs
#             unique_otus = len(set(sampled_contigs))
#             otu_estimates[sample].append(unique_otus)

#     # Calculate the mean OTU estimate for each sample
#     mean_otu_estimates = {sample: np.mean(otu_estimates[sample]) for sample in otu_estimates}
#     return mean_otu_estimates

# # Function to calculate expected OTU values using the factorial formula
# def combinations(n, k):
#     # Function to calculate combinations (n choose k)
#     if k > n or k < 0 or n < 0:
#         return 0
#     return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# def calculate_expected_otus(otu_counts, sample_size=50):
#     expected_otus = {}
    
#     for sample, counts in otu_counts.items():
#         total_contigs = sum(counts)
#         expected_otus_count = 0
        
#         for otu_count in counts:
#             if total_contigs == 0:
#                 prob_otu_in_sample = 0
#             else:
#                 # Calculate the probability that the OTU is present in the sample
#                 prob_otu_in_sample = 1 - (combinations(total_contigs - otu_count, sample_size) / combinations(total_contigs, sample_size))
#             expected_otus_count += prob_otu_in_sample
        
#         expected_otus[sample] = expected_otus_count
    
#     return expected_otus

# # Calculate bootstrapped OTU estimates
# bootstrapped_otus = bootstrap_otu_estimates(otu_counts)

# # Calculate expected OTU values
# expected_otus = calculate_expected_otus(otu_counts)

# # Print the results for bootstrapped OTU estimates
# print("Bootstrapped OTU Estimates:")
# print("Sample\tBootstrapped OTUs")
# for sample in bootstrapped_otus:
#     print(f"{sample}\t{bootstrapped_otus[sample]:.2f}")

# # Print the results for expected OTU values
# print("\nExpected OTU Values:")
# print("Sample\tExpected OTUs")
# for sample in expected_otus:
#     print(f"{sample}\t{expected_otus[sample]:.2f}")

# # Compare the bootstrapped OTU estimates with the expected OTU values
# print("\nComparison of Bootstrapped and Expected OTU Values:")
# print("Sample\tBootstrapped OTUs\tExpected OTUs")
# for sample in otu_counts:
#     print(f"{sample}\t{bootstrapped_otus[sample]:.2f}\t\t{expected_otus[sample]:.2f}")

# # Output the results in a table format using pandas
# results_df = pd.DataFrame({
#     'Sample': list(otu_counts.keys()),
#     'Bootstrapped OTUs': [bootstrapped_otus[sample] for sample in otu_counts],
#     'Expected OTUs': [expected_otus[sample] for sample in otu_counts]
# })

# print("\nResults Table:")
# print(results_df.to_string(index=False))

# # Create an image of the table
# fig, ax = plt.subplots(figsize=(10, 2))  
# ax.axis('tight')
# ax.axis('off')
# table = ax.table(cellText=results_df.values, colLabels=results_df.columns, cellLoc='center', loc='center')
# table.auto_set_font_size(False)
# table.set_fontsize(12)
# table.scale(1.2, 1.2)  

# plt.show()
# plt.savefig
# import random

# # Given data: OTU counts for each sample
# otu_counts = {
#     'A': [10, 20, 30, 20, 10],
#     'B': [2, 20, 17, 3, 15],
#     'C': [40, 2, 10, 5, 30],
#     'D': [17, 19, 21, 23, 18],
#     'E': [24, 14, 5, 17, 27]
# }

# # Function to estimate OTUs for a single sample
# def estimate_otu(sample_counts):
#     sampled_contigs = []
#     # Generate contigs based on OTU counts
#     for otu, count in enumerate(sample_counts, start=1):
#         sampled_contigs.extend([otu] * count)
#     # Randomly sample 50 contigs
#     sampled_contigs = random.sample(sampled_contigs, k=50)
#     # Count unique OTUs in the sampled contigs
#     unique_otus = len(set(sampled_contigs))
#     return unique_otus

# # Perform 10,000 iterations for each sample and store the results
# otu_estimates = {}
# for sample, counts in otu_counts.items():
#     estimates = [estimate_otu(counts) for _ in range(10000)]
#     otu_estimates[sample] = estimates

# # Print the results
# for sample, estimates in otu_estimates.items():
#     print(f"Sample {sample}: Mean OTUs = {sum(estimates) / len(estimates)}")

# import math

# # Given data: OTU counts for each sample
# otu_counts = {
#     'A': [10, 20, 30, 20, 10],
#     'B': [2, 20, 17, 3, 15],
#     'C': [40, 2, 10, 5, 30],
#     'D': [17, 19, 21, 23, 18],
#     'E': [24, 14, 5, 17, 27]
# }

# # Function to calculate combinations (n choose k) using the factorial formula
# def combinations(n, k):
#     return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

# # Function to calculate the expected number of OTUs for a sample
# def calculate_expected_otus(sample_counts):
#     total_contigs = sum(sample_counts)
#     expected_otus = 0
#     for count in sample_counts:
#         # Calculate the probability that the OTU is present in the sample
#         prob_otu_in_sample = 1 - combinations(total_contigs - count, 50) / combinations(total_contigs, 50)
#         expected_otus += prob_otu_in_sample
#     return expected_otus

# # Calculate the expected number of OTUs for each sample
# expected_otus = {}
# for sample, counts in otu_counts.items():
#     expected_otus[sample] = calculate_expected_otus(counts)

# # Print the results
# for sample, expected in expected_otus.items():
#     print(f"Expected OTUs for Sample {sample}: {expected}")
import numpy as np
import random
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Given data
otu_counts = {
    'A': [10, 20, 30, 20, 10],
    'B': [2, 20, 17, 3, 15],
    'C': [40, 2, 10, 5, 30],
    'D': [17, 19, 21, 23, 18],
    'E': [24, 14, 5, 17, 27]
}

def bootstrap_otu_estimates(otu_counts, sample_size=50, iterations=10000):
    # Initialize dictionary to store OTU estimates for each sample
    otu_estimates = {sample: [] for sample in otu_counts}

    for sample in otu_counts:
        # Create a list of contigs based on OTU counts
        contigs = []
        for i, count in enumerate(otu_counts[sample]):
            contigs.extend([i+1] * count)
        
        # Perform the specified number of iterations
        for _ in range(iterations):
            # Randomly sample 50 contigs
            sampled_contigs = random.choices(contigs, k=sample_size)
            # Count the number of unique OTUs in the sampled contigs
            unique_otus = len(set(sampled_contigs))
            otu_estimates[sample].append(unique_otus)

    # Calculate the mean OTU estimate for each sample
    mean_otu_estimates = {sample: np.mean(otu_estimates[sample]) for sample in otu_estimates}
    return mean_otu_estimates

def combinations(n, k):
    # Function to calculate combinations (n choose k)
    if k > n or k < 0 or n < 0:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def calculate_expected_otus(otu_counts, sample_size=50):
    expected_otus = {}
    
    for sample, counts in otu_counts.items():
        total_contigs = sum(counts)
        expected_otus_count = 0
        
        for otu_count in counts:
            if total_contigs == 0:
                prob_otu_in_sample = 0
            else:
                # Calculate the probability that the OTU is present in the sample
                prob_otu_in_sample = 1 - (combinations(total_contigs - otu_count, sample_size) / combinations(total_contigs, sample_size))
            expected_otus_count += prob_otu_in_sample
        
        expected_otus[sample] = expected_otus_count
    
    return expected_otus

# Calculate bootstrapped OTU estimates
bootstrapped_otus = bootstrap_otu_estimates(otu_counts)

# Calculate expected OTU values
expected_otus = calculate_expected_otus(otu_counts)
# Print the results for bootstrapped OTU estimates
print("Bootstrapped OTU Estimates:")
print("Sample\tBootstrapped OTUs")
for sample in bootstrapped_otus:
    print(f"{sample}\t{bootstrapped_otus[sample]:.2f}")

# Print the results for expected OTU values
print("\nExpected OTU Values:")
print("Sample\tExpected OTUs")
for sample in expected_otus:
    print(f"{sample}\t{expected_otus[sample]:.2f}")

# Compare the bootstrapped OTU estimates with the expected OTU values
print("\nComparison of Bootstrapped and Expected OTU Values:")
print("Sample\tBootstrapped OTUs\tExpected OTUs")
for sample in otu_counts:
    print(f"{sample}\t{bootstrapped_otus[sample]:.2f}\t\t{expected_otus[sample]:.2f}")
# Output the results in a table format using pandas
results_df = pd.DataFrame({
    'Sample': list(otu_counts.keys()),
    'Bootstrapped OTUs': [bootstrapped_otus[sample] for sample in otu_counts],
    'Expected OTUs': [expected_otus[sample] for sample in otu_counts]
})

print("\nResults Table:")
print(results_df.to_string(index=False))

# Create an image of the table
fig, ax = plt.subplots(figsize=(10, 2))  # Adjust the size as needed
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=results_df.values, colLabels=results_df.columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.2)  # Adjust the scaling as needed

# Save the table as an image
plt.savefig('otu_results_table.png')
plt.show()

# Calculate the differences between bootstrapped OTU estimates and expected OTUs
differences = {sample: bootstrapped_otus[sample] - expected_otus[sample] for sample in otu_counts}

# Print the differences
print("\nDifferences between Bootstrapped OTUs and Expected OTUs:")
print("Sample\tDifference")
for sample in differences:
    print(f"{sample}\t{differences[sample]:.2f}")

# Convert differences to a pandas DataFrame for easier computation
differences_df = pd.DataFrame.from_dict(differences, orient='index', columns=['Difference'])

# Compute mean, median, and standard deviation of the differences
mean_diff = differences_df['Difference'].mean()
median_diff = differences_df['Difference'].median()
std_diff = differences_df['Difference'].std()

# Print the statistics
print("\nStatistics of Differences:")
print(f"Mean Difference: {mean_diff:.2f}")
print(f"Median Difference: {median_diff:.2f}")
print(f"Standard Deviation of Difference: {std_diff:.2f}")


# Plot histograms and boxplots of the differences
plt.figure(figsize=(7, 3.5))

# Histogram
plt.subplot(1, 2, 1)
sns.histplot(differences_df['Difference'], kde=True)
plt.title('Histogram of Differences')
plt.xlabel('Difference')
plt.ylabel('Frequency')
# Annotate the statistics
plt.annotate(f'Mean: {mean_diff:.2f}', xy=(0.7, 0.9), xycoords='axes fraction')
plt.annotate(f'Median: {median_diff:.2f}', xy=(0.7, 0.85), xycoords='axes fraction')
plt.annotate(f'Std Dev: {std_diff:.2f}', xy=(0.7, 0.8), xycoords='axes fraction')

# Boxplot
plt.subplot(1, 2, 2)
sns.boxplot(y=differences_df['Difference'])
plt.title('Boxplot of Differences')
plt.ylabel('Difference')
# Annotate the statistics
plt.annotate(f'Mean: {mean_diff:.2f}', xy=(0.7, 0.9), xycoords='axes fraction')
plt.annotate(f'Median: {median_diff:.2f}', xy=(0.7, 0.85), xycoords='axes fraction')
plt.annotate(f'Std Dev: {std_diff:.2f}', xy=(0.7, 0.8), xycoords='axes fraction')

# Combine table header, column labels, and sample differences into a single string
annotated_differences = (
    "Differences between Bootstrapped OTUs and Expected OTUs:\n"
    "Sample\tDifference\n"
    + "\n".join([f"{sample}: {diff:.2f}" for sample, diff in differences.items()])
)
# Annotate differences at the bottom of the plot with heading and table
plt.figtext(0.5, -0.00001, annotated_differences, ha="center", fontsize=8)
# Show plots
plt.tight_layout()
#plt.savefig('otu_difference_plots.png')
plt.show()

# import numpy as np

# # Bootstrapped OTU estimates obtained previously
# bootstrapped_otus = {
#     'A': [4.99, 4.77, 4.63, 5.00, 4.95],
#     'B': [4.99, 4.94, 4.80, 4.92, 4.93],
#     'C': [4.98, 4.91, 4.92, 4.99, 4.87],
#     'D': [4.99, 4.79, 4.99, 5.00, 4.96],
#     'E': [4.97, 4.99, 4.96, 4.97, 4.93]
# }

# # Expected OTU values calculated previously
# expected_otus = {
#     'A': 5.00,
#     'B': 4.99,
#     'C': 4.81,
#     'D': 5.00,
#     'E': 4.99
# }

# # Calculate the difference between bootstrapped OTU estimates and expected OTUs for each sample
# differences = {sample: np.array(bootstrapped_otus[sample]) - expected_otus[sample] for sample in bootstrapped_otus}

# # Compute statistics
# mean_difference = {sample: np.mean(differences[sample]) for sample in differences}
# median_difference = {sample: np.median(differences[sample]) for sample in differences}
# std_dev_difference = {sample: np.std(differences[sample]) for sample in differences}

# # Print the statistics
# for sample in bootstrapped_otus:
#     print(f"Sample {sample}:")
#     print(f"Mean Difference: {mean_difference[sample]:.4f}")
#     print(f"Median Difference: {median_difference[sample]:.4f}")
#     print(f"Standard Deviation of Differences: {std_dev_difference[sample]:.4f}")
#     print()

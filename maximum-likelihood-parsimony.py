from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Scenario: Evolutionary Relationship of DNA Sequences

# Generate example sequence data
seq1 = SeqRecord(Seq("ACTG"), id="Seq1")
seq2 = SeqRecord(Seq("ACCG"), id="Seq2")
seq3 = SeqRecord(Seq("AGTG"), id="Seq3")

alignment = MultipleSeqAlignment([seq1, seq2, seq3])

# Step 1: Print the input Multiple Sequence Alignment
print("Step 1: Multiple Sequence Alignment")
print(alignment)

# Step 2: Calculate distances between sequences
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(alignment)

# Step 3: Print the Distance Matrix
print("\nStep 2: Distance Matrix")
print(dm)

# Step 4: Build a tree using Maximum Likelihood
constructor = DistanceTreeConstructor(calculator)

# Step 5: Print intermediate steps of tree construction
print("\nStep 3: Intermediate Steps of Tree Construction")
for i, tree in enumerate(constructor.build_trees(alignment)):
    print(f"\nSubstep {i + 1} - Tree:")
    print(tree)

# Step 6: Build the final Maximum Likelihood Tree
ml_tree = constructor.build_tree(alignment)

# Step 7: Print the Final Maximum Likelihood Tree
print("\nStep 4: Final Maximum Likelihood Tree")
Phylo.draw(ml_tree, do_show=True)

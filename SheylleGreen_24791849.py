from os.path import exists
from os.path import dirname
from os.path import join
#import os

class Fastq():

	def __init__(self):
		pass

	def read_fastq_format_file(self, filepath):
		file_text = []
		if exists(filepath) == False:
			print('The specified file does not exist. Please double-check.')
		else:
			### write code to read the lines from the FASTQ file as strings into the list 'file_text' ###
			### WRITE CODE HERE ###

			with open(filepath, 'r') as file:			# We open the file
				for line in file:						# Read each line of file

					file_text.append(line.strip())		# Put the line into preventing spaces

			### this function should return the lines in the FASTQ file as strings in the list 'file_text' ###
		return file_text

	def number_of_sequences(self,file_text):
		### WRITE CODE BELOW to count the number of sequences in the 'file_text' list

		number_of_sequences = 0

		for line in file_text:
			if line.startswith('@'):		# The sequence identifier line can give indication of number of sequences
				number_of_sequences +=1
			else:
				continue

		### return the number of sequences
		return number_of_sequences

	def get_sequences(self, file_text):
		### WRITE CODE BELOW to recover each sequence line from 'file_text' and adding the
		### sequence as a string member to the 'sequence' list
		number_of_lines = len(file_text)
		line = 0
		sequences = []

		while line < number_of_lines:
			if file_text[line].startswith('@'):

				sequences.append(file_text[line + 1])		# The line after the sequence identifier is the nucleotide sequence

			line += 1
        ### return the list of sequence strings
		return sequences

	def get_names(self, filetext):
		### WRITE CODE to retrieve the name of each sequence entry, and adding the name
		### as a string member to the 'names' list

		names=[]

		for line in filetext:
			if line.startswith('@'):
				names.append(line[1:].strip()) # We add line to list of names without the start index
			else:
				continue
		#
		### return the list of name strings
		return names

	def get_score_lines(self, file_text):
		### WRITE CODE to retrieve the Phred score entry for every sequence, and add this
		### score line as a string member to the 'scores' list
		number_of_lines = len(file_text)
		line = 0
		scores = []
		#
		while line < number_of_lines:
			if file_text[line].startswith('+'):
				scores.append(file_text[line + 1])		# Add the line the follows after the '+' line to the list

			line += 1
		### return a list of score strings
		return scores

	def get_average_Q(self, score_line):
		### WRITE CODE to calculate the average Q value for the string of Phred score symbols
		### passed as 'score_line' to this function.
		### You will need to select each symbol in turn, get the ASCII value of the symbol
		### by calling the 'self.get_ASCII_value(symbol)' function, convert the returned
		### value to a Q value by calling the 'self.convert_ASCII_value_to_Q(ASCII_value)'
		### function with the returned ASCII value, and add the Q value to the
		### 'sum_of_Q_values' variable.  This 'sum_of_Q_values' variable is finaly divided
		### by the number of symbols ('line_length'), and the average Q_value returned by
		### the 'get_average_Q(self, score_line)' function
		line_length = len(score_line)
		sum_of_Q_values = 0
		#
		for i in range(0, line_length):
			my_score = score_line[i]			# Get string line for first sequence
			score_len = len(my_score)

			for j in range(0, score_len):
				symbol= my_score[j]				# Get string character for scoreline
				ASCII_value = self.get_ASCII_value(symbol)
				Qvalue = self.convert_ASCII_value_to_Q(ASCII_value)
				sum_of_Q_values += Qvalue
		#
		average_Q_value = sum_of_Q_values/line_length
		### return the average Q value of the Phred symbol string 'score_line'
		return average_Q_value

	#------> This function must be used by NON inter-disciplinary BSc Bioinformatics and Computational <------
	#------> Biology students                                                                          <------

	def trim_sequence_in_while_loop(self, sequence, scoreline, minimum_average_Q_value, minimum_length):

		### WRITE CODE to calculate the average Q value of the sequence from the scoreline string
		### Use a while statement to test whether the average Q value is less than the
		### minimum_average_Q_value AND the length of the sequence is more than the
		### minimum_length. If it is True, remove one character from the end of the
		### sequence and scoreline string, decrease sequence length by 1, recalculate the average Q score,
		### and retest in the while statements.  Continue the while loop until it returns False.
		### The function then returns the resulting sequence and corresponding average Q value.
		#
		average_Q_score = self.get_average_Q(scoreline)
		len_sequence = len(sequence)
		len_scoreline = len(scoreline)

		while average_Q_score < minimum_average_Q_value and len_sequence > minimum_length:
			len_sequence -= 1
			len_scoreline -= 1
			sequence = sequence[:len_sequence]					# Make list of sequence one entry shorter
			scoreline = scoreline[:len_scoreline]				# Make list of scoreline one entry shorter
			average_Q_score = self.get_average_Q(scoreline)

		#
		return sequence,average_Q_score

	#------> This function must be used by inter-disciplinary BSc Bioinformatics and Computational <------
	#------> Biology students                                                                      <------

	#####def trim_sequence_by_recursion(self, sequence_line, ASCII_score_line, minimum_Q, minimum_length):

		### WRITE CODE to produce a recursive function that is called with a sequence string 'sequence_line'
		### a Phred symbol string 'ASCII_score_line', and minimum average Q value 'minimum_Q' and
		### minimum sequence length 'minimum_length'.  Calculate the average Q value of the
		### ASCII_score_line.  If it is less than the 'minimum_Q' and the length of the sequence
		### string 'sequencline' is longer than 'minimum length', reduce both the 'sequence_line' string
		### and the 'ASCII_score_line' string by one symbol from the right-hand side, and
		### call the 'trim_sequence_line' function with the shortened 'sequence_line' and
		### 'ASCII_score_line' strings.
		#
		#
		#
		### return the tuple 'sequence_line','average_Q_score' once the 'average_Q_score' is more than
		### 'minimum_Q' or the length of the sequence is equal to 'minimum_length'
		#### return sequence_line, average_Q_score

	def get_ASCII_value(self, symbol):
		### retrun the ASCII value of a letter. Use the 'ord()' function in Python.
		ASCII_value= ord(symbol)
		#
		return ASCII_value

	def convert_ASCII_value_to_Q(self, ASCII_value):
		### terun the Q value of the ASCII value.  Remember Q = Phred-33
		return ASCII_value-33


####### Do not change anything in the function 'main' below #######
####### except choosing either the "trim_sequence_in_while_loop" ##
####### or the 'trim_sequence_by_recursion' function.  See below ##

def main(filepath):
	minimum_average_Q_value = 35
	minimum_length = 10
	fastq = Fastq()
	### read the FASTQ text file as a list of strings
	filetext = fastq.read_fastq_format_file(filepath)
	print('Contents of FASTQ file\n')
	for line in filetext:
		print(line)

	### determine the number of sequences in the FATSQ file with 'number_of_sequences(filetext)'
	print('\nNumber of sequences =',fastq.number_of_sequences(filetext),'\n')

	### retrieve the names of the sequences in the FASTQ file with 'get_names(filetext)'
	names = fastq.get_names(filetext)
	for line in names:
		print(line)
	#
	print('')
	#
	### retrieve sequences in the FASTQ file as a list of sequence strings
	sequences = fastq.get_sequences(filetext)
	for i,line in enumerate(sequences):
		print('Sequence',i,'=',line)
	#
	print('')
	#
	### retrieve the Phred score string for each sequence in the FASTQ file as
	### a list of Phred score strings
	scorelines = fastq.get_score_lines(filetext)
	for line in scorelines:
		### determine the average Q score of a Phred score string in 'get_average_Q(line)'
		average_score = fastq.get_average_Q(line)
		print('Average score =',average_score)
	#
	print('')
	#
	number_of_sequences = len(sequences)
	for i in range(number_of_sequences):

		## If you are NOT an inter-disciplinary BSc Bioinformatics and Computational Biology student,
		## you must use the looping function below

		trimmed_sequence, average_score = fastq.trim_sequence_in_while_loop(sequences[i], scorelines[i], minimum_average_Q_value, minimum_length)


		print('sequence =',trimmed_sequence, 'score =',average_score)



if __name__ == "__main__":

	####### Substitute the string below to point to the locations of 'fastq_sequences.txt' on YOUR computer #######


	script_dir = dirname(__file__) 
	filename = "fastq sequences.txt"
	filepath = join(script_dir, filename) 
	main(filepath)



####### QUESTION 8 #######

# When we set the miniumum_average_Q_value in the main function to 40, then both the sequence and scoreline
# will continue to remove the 3' symbol until the condition of (length of sequence > minimum_length) is no longer met.
# This is because at the no point is the average Q values of a sequence greater than 40. We also know the since we are
# working with a while-block function and the test statement is the AND of the two tests, then when one condition is
# False, then the whole test becomes False.
# Our expected output:
# sequence = GTCTCCACAT score = 34.6
# sequence = CTCCACATTC score = 35.8
# sequence = TGCGGTTATC score = 35.8
# sequence = CCCCAGCCAA score = 35.8
# sequence = GCCCGCTGCG score = 35.2
# sequence = CTCCACATTC score = 35.8
# sequence = TCCCCACGCA score = 35.8
# sequence = GACGTAATCA score = 35.8
# sequence = GACCTGGCAT score = 35.8


from modeller import *
log.verbose()
env = Environ()
#-- Prepare the input files
#-- Read in the sequence database
sdb = SequenceDB(env)
sdb.read(seq_database_file='pdb_95.pir', seq_database_format='PIR',
         hains_list='ALL', minmax_db_seq_len=(30, 4000), clean_sequences=True)
#-- Write the sequence database in binary form
sdb.write(seq_database_file='pdb_95.bin', seq_database_format='BINARY',
          chains_list='ALL')
#-- Now, read in the binary database
sdb.read(seq_database_file='pdb_95.bin', seq_database_format='BINARY',
         chains_list='ALL')
#-- Read in the target sequence/alignment
aln = Alignment(env)
aln.append(file='2RSC_1_alignment.ali', alignment_format='PIR', align_codes='ALL')
#-- Convert the input sequence/alignment into
#   profile format
prf = aln.to_profile()
#-- Scan sequence database to pick up homologous sequences
prf.build(sdb, matrix_offset=-450, rr_file='${LIB}/blosum62.sim.mat',
          ap_penalties_1d=(-500, -50), n_prof_iterations=1,
          check_profile=False, max_aln_evalue=0.01)
#-- Write out the profile in text format
prf.write(file='build_profile.prf', profile_format='TEXT')
#-- Convert the profile back to alignment format
aln = prf.to_alignment()
#-- Write out the alignment file
aln.write(file='build_profile.ali', alignment_format='PIR')
from modeller import *
env = Environ()
aln = Alignment(env)
mdl = Model(env, file='1jse', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1jse', atom_files='1jse.pdb')
aln.append(file='2RSC_1_alignment.ali', align_codes='2RSC_1_alignment')
aln.align2d(max_gap_length=50)
aln.write(file='2RSC_1_alignment-1jse.ali', alignment_format='PIR')
aln.write(file='2RSC_1_alignment-1jse.pap', alignment_format='PAP')

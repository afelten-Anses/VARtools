VARCall README
================

Authors: Arnaud Felten, Nicolas Radomski

Affiliation: [Food Safety Laboratory – ANSES Maisons Alfort (France)](https://www.anses.fr/en/content/laboratory-food-safety-maisons-alfort-and-boulogne-sur-mer)

You can find the latest version of the tool at 
https://github.com/afelten-Anses/VARtools/tree/master/VARCall

HTML and pdf user technical documentation are available in the 'docs/' directory.


VARCall workflow
================

The differents workflow steps and scripts are presented below :

![](workflow.jpg?raw=true "VARCall workflow")

A driving script called 'VARCall' invokes 'BAMmaker', 'VCFmaker_SNP', 'VCFmaker_INDEL', and 'SNP-INDEL_merge', successively.  The script 'BAMmaker' allows trimming of single- and paired-end reads with Trimmomatic, read alignment against a reference genome with BWA, read sorting with Samtools, and potentially duplication removal and realignment around InDels with the Genome Analysis Toolkit (GATK), successively.  Following an approved framework for variant discovery, the scripts ‘VCFmaker_SNP’ and ‘VCFmaker_INDEL’ call and filter variants (i.e. SNPs and InDels) according to GATK best practices in order to retain high-confidence variants. 

Quick Start
===========

## run it on Linux/Mac OS X system

Simply run the command in the 'src/' directory:

	 ./VARCall

You must to set scripts in your $PATH variable:

	export PATH=$PATH:src/


Dependencies
============

VARCall needs python 2.7 (tested with 2.7.6), and the following librarires are require:

* [Biopython](http://biopython.org/wiki/Download)

VARCall requires the following programs in your $PATH:

* [BWA](http://bio-bwa.sourceforge.net/) - tested with 0.7.12
* [samtools](http://samtools.sourceforge.net/) - tested with 1.1 
* [picard-tools](http://picard.sourceforge.net/) - tested with 1.133
* [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic) - tested with 0.33	
* [GATK](www.broadinstitute.org) - tested with 3.4.0
* [SnpSift](http://snpeff.sourceforge.net/) - tested with 4.1


VARCall Parameters
===================

##  VARCall parameters

 * '-ref': reference genome in FASTA (REQUIRED)
 * '-reads': single-end reads FASTQ file or paired-end reads FASTQ files  (REQUIRED). Paired-end reads must be nammed as "prefix_R1.XXXX" and "prefix_R2.XXXX", example : E1_R1.fq and E1_R2.fq'
 * '-a': adaptaters FASTA file for trimming (REQUIRED)
 * '-TRIMJAR': Trimmomatic jar path (REQUIRED)
 * '-GATKJAR': GenomeAnalysisTK jar path (REQUIRED)
 * '-PICARDJAR': picard-tools jar path (REQUIRED) 
 * '-SNPSIFTJAR': SnpSift jar path (REQUIRED)
 * '-o': output prefix ['output']
 * '-q': min phred score per base for trimming ['30']
 * '-l': min read length for trimming ['50'] 
 * '-PL': sequencing plateform for RG line ['UNKNOWN']
 * '-PU': sequencer ID for RG line ['UNKNOWN']
 * '-LB': sequencing library ['UNKNOWN']
 * '-s': stand_call_conf parameter for GATK UnifiedGenotyper ['50']
 * '-T': maximum number of threads to use ['1']
 * '-m': max memory to use in Mb ['4000']
 * '--removeDuplicates': remove duplicates reads
 * '--indelRealigner': local realignment around indels
 * '--removeTmpFiles': remove temporary files


Ouputs
======

The workflow 'VARCall' produces a VCF file, matrices of pairwise distances ('VCFtoMATRIX'), a report about breadth and depth coverages ('reportMaker'), as wells as files of concatenated variants and pseudogenomes in order to be able to build fast or slow phylogenetic inferences, respectively. The pseudogenomes correspond to the reference genome where the genotypes of detected variants are replaced in each genome of the dataset.	


Citations
=========

[A. Felten, M. Vila Nova, K. Durimel, L. Guillier, M. Mistou and N. Radomski. First gene-ontology enrichment analysis based on bacterial coregenome variants: insights into adaptations of Salmonella serovars to mammalian- and avian-hosts. BMC Microbiology, 2017, 17:222.](https://doi.org/10.1186/s12866-017-1132-1)
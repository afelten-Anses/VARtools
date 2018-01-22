iVARCall2 README
================

Authors: Arnaud Felten, Nicolas Radomski

Affiliation: [Food Safety Laboratory - ANSES Maisons Alfort (France)](https://www.anses.fr/en/content/laboratory-food-safety-maisons-alfort-and-boulogne-sur-mer)

You can find the latest version of the tool at [https://github.com/afelten-Anses/VARtools/tree/master/iVARCall2](https://github.com/afelten-Anses/VARtools/tree/master/iVARCall2)

HTML and PDF technical documentations are available in the 'docs/' directory.


iVARCall2 workflow
==================

This workflow called iVARCall2 for "independant variant calling 2" aims to perform the variant calling analysis from Illumina paired-end reads based on the GATK HaplotypeCaller algorithm. Each sample are processed independently and a g.vcf file is produce for each of them. This allows combination of several iVARCall2 results if the same reference genome is used. 

The different steps and scripts of the workflow are presented below :

![](workflow.jpg?raw=true "iVARCall2 workflow")

- A driving script called 'iVARCall2' invokes 'BAMmaker', 'iVCFmaker', 'iVCFmerge', 'iVCFilter', 'VCFtoMATRIX', 'VCFtoFASTA', VCFtoPseudoGenome' and 'iReportMaker2' successively. 

- The script 'BAMmaker' allows trimming of paired-end reads with Trimmomatic, read alignment against a reference genome with BWA, read sorting with Samtools, and potentially duplication removal and realignment around InDels with the Genome Analysis Toolkit (GATK), successively.  

- Following an approved framework for variant discovery, the scripts 'iVCFmaker' call and filter variants (i.e. SNPs and InDels) according to GATK best practices in order to retain high-confidence variants and make a g.vcf file for each sample.

- The script 'iVCFmerge' merge all g.vcf in a single vcf file.

- All detected variants are filtrated by 'VCFilter' in order to remove variants presenting by missing data or only due to reference.

- The script 'VCFtoMATRIX' produces 3 distance matrices (SNPs, InDels and SNPs + InDels) from all variants selected by the workflow.

- All filtrated variants are concatenated in a 3 fasta files (SNPs, InDels and SNPs + InDels) by the 'VCFtoFASTA' script. These fasta files can be used to produce a phylogenetic tree.

- The 'VCFtoPseudoGenome' script replace for each sample all SNPs in the reference genome in order to obtain a 'PseudoGenome'. For this step, InDels are not included.

- Finaly, the script "iReportMaker2" produce a pdf file where several variant calling informations and parameters are listed. 

Each script can also be invoked independently.


Quick Start
===========

## Usage (Linux/Mac OS X)

If it's necessary, make all scripts excecutable :

	chmod +x src/*

Add the scripts to your bashrc (/home/username/.bashrc) :

	export PATH=$PATH:src/
	
Then you can run it as shell command :

	iVarCall2


Dependencies
============

iVARCall2 has been developped with python 2.7 (tested with 2.7.6).

## Important

This workflow needs 'BAMmaker', 'VCFtoMATRIX', 'VCFtoFASTA' and 'VCFtoPseudoGenome' scripts in your $PATH. This scripts are available in the VARCall/src directory of the VARtools git repository.


## External dependencies

* [BWA](http://bio-bwa.sourceforge.net/) - tested with 0.7.12
* [samtools](http://samtools.sourceforge.net/) - tested with 1.1 
* [picard-tools](http://broadinstitute.github.io/picard/) - tested with 1.133
* [Trimmomatic](http://www.usadellab.org/cms/index.php?page=trimmomatic) - tested with 0.33	
* [GATK](https://software.broadinstitute.org/gatk/) - tested with 3.7.0
* [vcftools (Vcf.pm)](http://vcftools.sourceforge.net/) - tested with 0.1.12b
* [pdflatex](https://ctan.org/pkg/pdftex) - tested with 3.14159265-2.6-1.40.16


Parameters
==========

Parameters of each scripts are available using the option below (example for iVCFmaker):

	iVCFmaker
	iVCFmaker -h
	iVCFmaker --help

## iVARCall2 parameters

* -a : adaptaters FASTA file (REQUIRED)
* -TRIMJAR : Trimmomatic jar path
* -GATKJAR : GenomeAnalysisTK jar path
* -PICARDJAR : picard-tools jar path
* -o : output prefix (default:output)
* -q : minimum phred score per base for trimming (default:30)
* -l : minimum read length for trimming (default:50)
* -PL : sequencing plateform for RG line (default:UNKNOWN)
* -PU : sequencer ID for RG line (default:UNKNOWN)
* -LB : sequencing library (default:UNKNOWN)
* -T : maximum number of threads to use (default:1)
* -m : maximum memory to use in Mb (default:4000)

## iVARCall2 options

* --removeDuplicates : remove duplicated regions of the chromosome (recommended)
* --indelRealigner : local realignment around indels (recommended)
* --removeTmpFiles : remove temporary files (recommended)
* --onlyVCF : stop process after making independent g.vcf files


Ouputs
======

iVARCall2 structures its output in a folder named with the command line argument '-o' ('output' as default). In this folder you can find :
* a 'REF' folder which contains a copy of the reference used for the variant calling and its index.
* a 'BAM' folder which stocks the final bam file and its bai index for each analyzed sample.
* a 'VCF' folder which contains the g.vcf file and its index for each sample and a 'output_SNP_INDEL_filtered.vcf' file which results from the merge of all g.vcf files.    
* a 'matrix' folder where 3 different matrices are stored in tabular separator values format (tsv). These matrices represente the pairwise distances. The matrix 'output_SNP.tsv' is calculated only with the SNP pairwise distance, the matrix 'output_INDEL.tsv' is calculated only with the INDEL pairwise distance and the last 'output_ALL.tsv' matrix combines both SNPs and InDels distance.
* a 'FASTA' folder which stores fasta files resulting from the concatenation of detected SNPs ('output_SNP.fasta'), detected InDels ('output_INDEL.fasta') and the concatenation of both SNPs and InDels ('output_ALL.fasta'). Furthermore, a 'output_pseudoGenomes.fasta' has been created from the reference genome where SNPs variants are replaced for each sample.    
* a 'output_report.pdf' file where different important informations are registered such as iVARCall arguments and parameters, version of external tools, reference, as well as statistic table about trimming and alignment.
* a 'output_statistic.tsv' file where the pdf table is stocked in tsv format.
* a log file 'output.log'.   

Note : without the '--removeTmpFiles' option, many others intermediate files are kept in the output directory. 

Citations
=========

[A. Felten, M. Vila Nova, K. Durimel, L. Guillier, M. Mistou and N. Radomski. First gene-ontology enrichment analysis based on bacterial coregenome variants: insights into adaptations of Salmonella serovars to mammalian- and avian-hosts. BMC Microbiology, 2017, 17:222.](https://doi.org/10.1186/s12866-017-1132-1)


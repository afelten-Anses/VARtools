Title: iVARCall2 README

Authors: Arnaud Felten, Nicolas Radomski

Affiliation: [Food Safety Laboratory – ANSES Maisons Alfort (France)](https://www.anses.fr/en/content/laboratory-food-safety-maisons-alfort-and-boulogne-sur-mer)


HTML and PDF technical documentation are available in the 'docs/' directory.


iVARCall2 workflow
==================

This workflow called iVARCall2 for "independant variant calling 2" aims to perform the variant calling analysis from Illumina paired-end reads based on the GATK HaplotypeCaller algorithm. Each sample are processing independently and a g.vcf file is produce for each of them. This allow to combin several iVARCall2 results if the same reference genome is used. 

The differents workflow steps and scripts are presented below :

![](workflow.jpg?raw=true "iVARCall2 workflow")

- A driving script called 'iVARCall2' invokes 'BAMmaker', 'iVCFmaker', 'iVCFmerge', 'iVCFilter', 'VCFtoMATRIX', 'VCFtoFASTA', VCFtoPseudoGenome' and 'iReportMaker2' successively. 

- The script 'BAMmaker' allows trimming of paired-end reads with Trimmomatic, read alignment against a reference genome with BWA, read sorting with Samtools, and potentially duplication removal and realignment around InDels with the Genome Analysis Toolkit (GATK), successively.  

- Following an approved framework for variant discovery, the scripts 'iVCFmaker' call and filter variants (i.e. SNPs and InDels) according to GATK best practices in order to retain high-confidence variants and obtain a g.vcf file for each sample.

- The script 'iVCFmerge' merge all g.vcf file in a single vcf file.

- All variants detected are filered by 'VCFilter' in order to remove variants caused by missing data or due to reference.

Each script can be invoked independently.
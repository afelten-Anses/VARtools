VARCall README
================

Authors: Arnaud Felten, Nicolas Radomski, Meryl Vila Nova

Affiliation: [Food Safety Laboratory – ANSES Maisons Alfort (France)](https://www.anses.fr/en/content/laboratory-food-safety-maisons-alfort-and-boulogne-sur-mer)

You can find the latest version of the tool at 
https://github.com/afelten-Anses/VARtools/tree/master/FixedVarTools

HTML and pdf user technical documentation are available in the 'docs/' directory.


phyloFixedVar and FixedVar scripts
==================================

The script called 'phyloFixedVar' uses a annotated VCF file (e.g. SnpEff) from the variant calling analysis and a newick file from a binary tree in order to identify sensitive and specific variants at each leaf of a phylogenetic inference.

This script ‘phyloFixedVar’ aims to 
* (a) identify all comparisons of genome groups referring to all nodes, 
* (b) select sensitive and specific variants, 
* (c) define if these variants are involved the effect of homoplasy.

With a view to be compared, leafs of right child are listed with corresponding leafs of left child at each node and reversely.  Both comparisons (i.e. right versus left children and reversely) are associated with comparison numbers which are attributed to identifiers of single nodes, all together grouped into node labels in a new newick file (a).  The sensitive variants are identified as presenting common genotypes into leaves of right or left child of previously listed comparisons.  Based on these sensitive variants, the specific variants are identified as presenting different genotypes in corresponding right or left children (b).  Focusing on these selected variants, the genotypes of all the other genomes are screened in order to tag variants presenting the effect of homoplasy (i.e. common genotypes between variants of independent phylogenetic clades) (c).

Finally, the sensitive and specific variants are listed in the xml file with the corresponding annotations (genotype, effect of homoplasy, NP numbers, gene IDs, gene names, type, position, phenotypical impact) for each node and all comparisons of leaf lists.

Based on the same principle that 'phyloFixedVar', another script called 'FixedVar' was also developed to identify fixed variants independently of the phylogenetic inference.  This script 'FixedVar' requires a VCF file, as well as lists of genomes IDs that have to be compared together.

Quick Start
===========

## run it on Linux/Mac OS X system

Simply run the command in the 'src/' directory:

	 ./phyloFixedVar

or:

	 ./FixedVar


We recommend to set scripts in your $PATH variable:

	export PATH=$PATH:src/


Parameters
===================

##  phyloFixedVar parameters

 * '-t': NEWICK file without node label (REQUIRED)
 * '-i': VCF file annotated with SNPEff (REQUIRED)
 * '-o': output prefix ['output']

##  FixedVar parameters

 * '-i': VCF file annotated with SNPEff (REQUIRED)
 * '-a': file with names of genomes of interest, one name per line (REQUIRED)
 * '-b': file with names of compared genomes, one name per line (REQUIRED)
 * '-o': output prefix ['output']


Ouputs
======

The sensitive and specific variants are listed in the XML file with the corresponding annotations (genotype, effect of homoplasy, NP numbers, gene IDs, gene names, type, position, phenotypical impact) for each node and all comparisons of leaf lists.

The 'phyloFixedVar' script produces also a newick file similar to the input newick file with node labels (nodes id and combinations id).
 

Citations
=========

[A. Felten, M. Vila Nova, K. Durimel, L. Guillier, M. Mistou and N. Radomski. First gene-ontology enrichment analysis based on bacterial coregenome variants: insights into adaptations of Salmonella serovars to mammalian- and avian-hosts. BMC Microbiology, 2017, 17:222.](https://doi.org/10.1186/s12866-017-1132-1)
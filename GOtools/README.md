Title: GOtools README

Authors: Kevin Durimel, Arnaud Felten, Nicolas Radomski

Affiliation: [Food Safety Laboratory – ANSES Maisons Alfort (France)](https://www.anses.fr/en/content/laboratory-food-safety-maisons-alfort-and-boulogne-sur-mer)


HTML and PDF technical documentation are available in the 'docs/' directory.


GoXML and EveryGO
=================

![](workflow.png?raw=true "GoXML and EveryGO workflow")

 'GetGOxML' aims to centralize the functional annotations of variants (i.e. genotype, effect of homoplasy, NP numbers, gene IDs, gene names, type, position, phenotypical impact) with the GO-terms information in a unique XML file.

Based on the accession numbers contained in the XML file, the driving script 'GetGOxML' invokes the scripts 'GOSlimmer_XML' and 'GOxML' in order to associate the identified variants with their respective and relevant GO-terms reachable in the [QuickGO browser](http://www.ebi.ac.uk/GOA) 

- 'GOSlimer_XML' generates prokaryote-specific subset of GO terms (go_prok.txt) from a Gene Ontology graph (i.e. [go-basic.obo](http://geneontology.org/page/download-ontology)  file)  in order to remove eukaryote-specific GO-terms from the dataset.

- 'GOxML' associates NCBI accession identifiers contained in the XML file with their respective relevant GO-terms


By using the XML file, the driving script 'EveryGO' selects non-synonymous variants (SNPs and InDels) at the selected nodes of the phylogeny, and distinguishes between GO-terms from the interest variants (i.e. tested sample) and all variants (i.e. universe) which are used for the hypergeometric test, then invokes 'GOWalker' and 'GOView', successively.

- 'GOWalker' counts the GO-terms from the sample (i.e. variants from compared leafs) and the universe (i.e. all variants) for each GO-term, as well as the sample (i.e. total GO-terms in the sample) and universe sizes (i.e. total GO-terms in the universe) in order to perform a GO-term enrichment analysis based on the hypergeometric test and the implemented Bonferroni correction.

-  'GOView' computes a graphical representation of the GO-term enrichment analysis.




Quick Start
===========

## Usage (Linux/Mac OS X)

### Solution 1 (faster)
Simply run the command in the 'src/' directory:

	 ./GoXML
	 ./EveryGO

### Solution 2 (simplier)

Add the scripts to your bashrc (/home/username/.bashrc) :

	export PATH=$PATH:src/
	export PATH=$PATH:src/otherScripts/
	
Then you can run it as shell commands :

	GoXML 
	EveryGO
	

Dependencies
============

GoXML and EveryGO need python 2.7 (tested with 2.7.6), and the following R librarires are required:

* [GGplot2]
* [gridExtra]
* [biocLite.R]


Parameters
===================

##  GoXML parameters

 * **'-i':** XML path (REQUIRED)
 * **'-obo':** go-basic.obo path (REQUIRED)
 * ** '-o':** output prefix (REQUIRED)
 * **'-d':** NP-EBI_databases.tsv path 
 * **'-g':** EBI-GO_databases.tsv path
 * **'--withHomoplasy'**: keep homoplasy variants

##  EveryGO parameters

 * **'-xml':** XML input file obtained from the GoXML including all variants (REQUIRED)
 * **'-xmlcomp': **XML input file obtained from the GoXML including variants of interest (REQUIRED)
 * **'-comp':** one or several values refering to XML comparison ids (ascending order, REQUIRED)
 * **'-rpath':** Rscripts folder path' (REQUIRED) 
 * **'--mkuniverse':** build universe
 * **'--view':** generate graphical representation

Ouputs
======

The script GoXML produces a XML file including GO-terms related to the variants functional annotation, and the script EveryGO produces a TSV file including results of hypergeometric tests with their optional graphical representation.
 

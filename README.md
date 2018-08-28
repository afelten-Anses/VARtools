<h1 align=center>
<img src="https://img.shields.io/badge/license-GNU-green.svg" alt="licence"/>
<img src="https://img.shields.io/badge/DOI-10.1186%2Fs12866--017--1132--1-blue.svg" alt="doi"/>
<br/>
<img src="https://github.com/afelten-Anses/VARtools/blob/master/sepbar.png" alt="sepbar"/>
VARtools: scripts for SNPs and INDELs analysis. 
<img src="https://github.com/afelten-Anses/VARtools/blob/master/sepbar.png" alt="sepbar"/>
</h1>


- [VARCall](#varcall)
- [FixedVarTools](#fixedvartools)
- [GOTools](#gotools)
- [iVARCall 1 & iVARCall2](#ivarcall-1---ivarcall2)


## VARCall

Identification of fixed SNPs and InDels distinguishing homoplastic and non-homoplastic coregenome variants. 

<img src="https://raw.githubusercontent.com/afelten-Anses/VARtools/master/VARCall/workflow.jpg" alt="Varcall workflow"/>

[VARCall readme](https://github.com/afelten-Anses/VARtools/tree/master/VARCall)

<br/>

## FixedVarTools

* Identify all comparisons of genome groups referring to all nodes, 
* Select sensitive and specific variants, 
* Define if these variants are involved the effect of homoplasy.

[FixedVAR readme](https://github.com/afelten-Anses/VARtools/tree/master/FixedVarTools)

<br/>

## GOTools

Gene ontology enrichment analysis based on hypergeometric tests, identifying genome groups and excluding
obsolete and non-prokaryotic GO-terms. 

<img src="https://github.com/afelten-Anses/VARtools/blob/master/GOtools/workflow.png" alt="GOtools workflow"/>

[GOTools readme](https://github.com/afelten-Anses/VARtools/tree/master/GOtools)

<br/>

## iVARCall 1 & iVARCall2

"Independant variant calling". Aims to perform a variant calling analysis from Illumina paired-end reads based 
on the GATK HaplotypeCaller algorithm. Each sample are processed independently and a g.vcf file is produce for each of
them. This allows combination of several iVARCall2 results if the same reference genome is used.

<img src="https://raw.githubusercontent.com/afelten-Anses/VARtools/master/iVARCall2/workflow.jpg" alt="iVARCall2 workflow"/>

[iVARCall readme](https://github.com/afelten-Anses/VARtools/tree/master/iVARCall)

[iVARCall2 readme](https://github.com/afelten-Anses/VARtools/tree/master/iVARCall2)

<br/>

<img src="https://github.com/afelten-Anses/VARtools/blob/master/sepbar.png" alt="sepbar"/>

Citations
=========

[A. Felten, M. Vila Nova, K. Durimel, L. Guillier, M. Mistou and N. Radomski. First gene-ontology enrichment analysis based on bacterial coregenome variants: insights into adaptations of Salmonella serovars to mammalian- and avian-hosts. BMC Microbiology, 2017, 17:222.](https://doi.org/10.1186/s12866-017-1132-1)


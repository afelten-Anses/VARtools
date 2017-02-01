**LIBRARIES REQUIRED**

    -PYTHON

        PyVCF :  pip install PyVCF

    -R
        GGplot2 :
        install.packages("ggplot2")

        gridExtra :
        install.packages("gridExtra")

        source("http://bioconductor.org/biocLite.R")
        biocLite("GO.db")

---------------------------------------------------------------------------------------------------------------------------
**PRO-TIP**

*Perform script with last Gene Ontology version

In order to have the last version of Prokaryota GO-terms, replace the old db/GO-basic.obo by a new one by donwload it here:
http://geneontology.org/ontology/go-basic.obo


*Personal R user environment / Install libraries from a proxy

[delete R from  /usr/bin make one in opt],then

Sys.setenv(http_proxy="=http://XXXXX:YYYYY@alfortproxy.afssa.fr:8080") # avec XXX ton ID Anses et YYYY ton pwd Anses
source("http://bioconductor.org/biocLite.R")
biocLite("GO.db")



---------------------------------------------------------------------------------------------------------------------------

**HOW TO USE GOWALKER**

Deposit the files you want to process (vcf,xml) at the root directory of GoWalker. (same level as EveryGO and GOxML)

1.VCFtoGO Workflow : In order to perform Go-term enrichment analysis from A VCF File
    -Start VCFtoGO
    -Then, start GOWalker_manual
    -Then, start GOview_manual in order to generate graphical outputs.

2.GOxML Workflow : In order to perform GO-term enrichmlent analysis from a VCF File (recommended)

    -Start GOxML in ordr to insert GO-terms in the XML file
    -Then, start EveryGO in order to perform automated enrichment analysis for each nodes you want to.
    -Take a cofee.


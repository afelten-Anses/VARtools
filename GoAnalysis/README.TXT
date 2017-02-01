
python module vcf : 

pip install PyVCF

ficher goprok :
peut être généré à partir de 
http://geneontology.org/ontology/go-basic.obo


[supprimer le R de /usr/bin et faire un alternative sur le R de l'opt]
Go.db pour R: 

Sys.setenv(http_proxy="=http://XXXXX:YYYYY@alfortproxy.afssa.fr:8080") # avec XXX ton ID Anses et YYYY ton pwd Anses
source("http://bioconductor.org/biocLite.R")
biocLite("GO.db")

GGplot2 :
install.packages("ggplot2")

gridExtra :
install.packages("gridExtra")

library(ggplot2)
library(gridExtra)
#Parse args
args <- commandArgs(TRUE)
compvalue=args[1]
filepath=args[2]
#Parse hypergeometric file results
resultats=read.delim((paste(compvalue,"/",filepath,sep="")),sep="\t")
x <-as.numeric(c(resultats$P.value))
profondeur <-as.numeric(resultats$Go.level)
y <- as.numeric(resultats$Go.level)
LogP <- as.numeric(c(log(resultats$P.value)))
yx <- resultats[1:2]

#Aspect=dataframe (value= MF,BP or CC)
MF=0
BP=0
CC=0

for(i in 1:length(resultats$Aspect))
{
  if(resultats$Aspect[i]=="MF")
  {
    MF=MF+1
  }
  if(resultats$Aspect[i]=="BP")
  {
    BP=BP+1
  }
  if(resultats$Aspect[i]=="CC")
  {
    CC=CC+1
  }
}
mini=0.5
for(i in 1:length(resultats$P.value))
{
  if(resultats$P.value[i]!=0)
  {
    if(log(resultats$P.value[i])<mini)
    {
      mini<-log(resultats$P.value[i])
    }
    }
  }
  Aspect <- as.factor(c(rep("Molecular function",MF), rep("Biological process",BP),rep("Cellular Component",CC))) # 800condition1+852condition2 soit 1652 de longueur comme les autres variables
  #ou 
  #Aspect <-as.factor(c(aspect))
  #ou
  #Aspect <-resultats[3]
  
  #placeholder plot - prints nothing at all
  empty <- ggplot()+geom_point(aes(1,1), colour="white") +
    theme(                              
      plot.background = element_blank(), 
      panel.grid.major = element_blank(), 
      panel.grid.minor = element_blank(), 
      panel.border = element_blank(), 
      panel.background = element_blank(),
      axis.title.x = element_blank(),
      axis.title.y = element_blank(),
      axis.text.x = element_blank(),
      axis.text.y = element_blank(),
      axis.ticks = element_blank()
    )
  
  #scatterplot of x and y variables
  scatter <- ggplot(yx,aes(LogP,profondeur)) + 
    geom_point(aes(color=Aspect)) + 
    scale_color_manual(values = c("orange", "purple","grey")) + 
    theme(legend.position=c(0,1),legend.justification=c(0,1))+
    scale_x_continuous(limits=c(min(mini),max(0)))
  
  #marginal density of x - plot on top
  plot_top <- ggplot(yx, aes(LogP, fill=Aspect)) + 
    geom_density(alpha=.5) + 
    scale_fill_manual(values = c("orange", "purple","grey")) + 
    theme(legend.position = "none")+
    scale_x_continuous(limits=c(min(-10),max(0)))+  
    scale_y_continuous(limits=c(min(0),max(x)))  #auto-scale graph
  
  #marginal density of y - plot on the right
  plot_right <- ggplot(yx, aes(profondeur, fill=Aspect)) + 
    geom_density(alpha=.5) + 
    coord_flip() + 
    scale_fill_manual(values = c("orange", "purple","grey"))+ 
    theme(legend.position = "none") +
    scale_x_continuous(limits=c(min(4.9),max(y))) #auto-scale graph
  
  
  #arrange the plots together, with appropriate height and width for each row and column
  scatter<-scatter+geom_smooth()
  pdf(paste(compvalue,"/","GO_distribution.pdf",sep="")) #auto-generate pdf
  grid.arrange(plot_top, empty, scatter, plot_right, ncol=2, nrow=2, widths=c(4, 1), heights=c(1, 4))
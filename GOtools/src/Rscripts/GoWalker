######################################################################################################################
############# GO-TERMS ENRICHMENT
######################################################################################################################

#######################################################
#GENERAL SETTINGS
#######################################################

#Load GOdb silently
suppressMessages(library(GO.db))

#Raise number of printable strings in order to be able to capture large outputs
options(max.print=99999999)

#parse arguments from EveryGO.py
args <- commandArgs(TRUE)

#Load VCFtoGO.py and EveryGO.py output 
go_file=readLines("univers.txt")                                #VCFtoGO output (non-enriched list of GO-terms for universe)
compvalue=args[1]                                               #Folder name will be the same thant "value" of <COMPARISON>
compvalue=gsub(" ", "",compvalue, fixed = TRUE)                 #Fix 10.08.16
go_ech_file=readLines(paste(compvalue,"/","go_ech.txt",sep="")) #EveryGO output (non-enriched list of GO-terms for sample)

#####################################################################
#GO-TERMS WALKING
#####################################################################
##GO-term walking goal: Retrieve all ancestor GO-terms of the GO-term three for each GO-ID's and categorize them by one file per aspect(CC,BP,MF)


################### ASPECT 1: CC ################################

###RETRIEVE UNIVERSE GO-TERMS ANCESTORS###

capture.output(for(i in 1:length(go_file))
{
  aspect=1
  #Try, in order to avoid errors if GO-term is not a CC or dont have any ancestors
  try(print(aspect<-get(go_file[i],GOCCANCESTOR)),TRUE)
  options(warn=-1) #This test is valid but generate msgerr, so, turn-off msgerr
  if(aspect!=1) #if aspect!=1 aspect is an GOCC
  {
    print(go_file[i]) #print first GO-term if is its a CC
  }
  options(warn=0) # test ok, turn-on msgerr
},file=(paste(compvalue,"/gocc_univ.txt",sep="")))

#Open file and keep GO terms only (update file and erase old version)
data=scan(paste(compvalue,"/","gocc_univ.txt",sep=""),what="character"())#opened with fonction scan (+as character) in order to grep efficiently with go_only

#Special function in order to dont show columns and row names during the writing of the output file
print.go_only <- function(m)
{
  write.table(format(m, justify="right"),
              row.names=F, col.names=F, quote=F)
}


#Save results which only contains GO Id's
capture.output(print.go_only(grep(pattern ="GO:" , data, value = TRUE, fixed = TRUE)),file=paste(compvalue,"/gocc_univ.txt",sep=""))


###RETRIEVE SAMPLE GO-TERMS ANCESTORS###

capture.output(for(i in 1:length(go_ech_file))
{
  #Try, in order to avoid errors if GO-term is not a CC or dont have any ancestors
  aspect=1
  #Try, in order to avoid errors if GO-term is not a CC or dont have any ancestors
  try(print(aspect<-get(go_ech_file[i],GOCCANCESTOR)),TRUE)
  options(warn=-1)
  if(aspect!=1) #if aspect!=1 aspect is an GOCC
  {
    print(go_ech_file[i]) #print first GO-term if is its a CC
  }
  options(warn=0)
},file=(paste(compvalue,"/gocc_ech.txt",sep="")))

#Open file and keep GO terms only (update file and erase old version)
data=scan(paste(compvalue,"/gocc_ech.txt",sep=""),what="character"())#opened with fonction scan (+as character) in order to grep efficiently with go_only

#Save results which only contains GO Id's
capture.output(print.go_only(grep(pattern ="GO:" , data, value = TRUE, fixed = TRUE)),file=(paste(compvalue,"/gocc_ech.txt",sep="")))

################### ASPECT 2: BP ################################

###RETRIEVE UNIVERSE GO-TERMS ANCESTORS###

capture.output(for(i in 1:length(go_file))
{
  aspect=1
  #Try, in order to avoid errors if GO-term is not a CC or dont have any ancestors
  try(print(aspect<-get(go_file[i],GOBPANCESTOR)),TRUE)
  options(warn=-1)
  if(aspect!=1) #if aspect!=1 aspect is an GOCC
  {
    print(go_file[i]) #print first GO-term if is its a CC
  }
  options(warn=0)
},file=(paste(compvalue,"/gobp_univ.txt",sep="")))

#Open file and keep GO terms only (update file and erase old version)
data=scan(paste(compvalue,"/gobp_univ.txt",sep=""),what="character"()) 
capture.output(print.go_only(grep(pattern = "GO:" , data, value = TRUE, fixed = TRUE)),file=(paste(compvalue,"/gobp_univ.txt",sep="")))

###RETRIEVE SAMPLE GO-TERMS ANCESTORS###

capture.output(for(i in 1:length(go_ech_file))
{
  #Try, in order to avoid errors if GO-term is not a CC or dont have any ancestors
  aspect=1
  #Try, in order to avoid errors if GO-term is not a CC or dont have any ancestors
  try(print(aspect<-get(go_ech_file[i],GOBPANCESTOR)),TRUE)
  options(warn=-1)
  if(aspect!=1) #if aspect!=1 aspect is an GOCC
  {
    print(go_ech_file[i]) #print first GO-term if is its a CC
  }
  options(warn=0)
},file=(paste(compvalue,"/gobp_ech.txt",sep="")))

#Open file and keep GO terms only (update file and erase old version)
data=scan(paste(compvalue,"/gobp_ech.txt",sep=""),what="character"())#opened with fonction scan (+as character) in order to grep efficiently with go_only
#Save results which only contains GO Id's
capture.output(print.go_only(grep(pattern ="GO:" , data, value = TRUE, fixed = TRUE)),file=(paste(compvalue,"/gobp_ech.txt",sep="")))


################### ASPECT 3: MF ################################

###RETRIEVE UNIVERSE GO-TERMS ANCESTORS###

capture.output(for(i in 1:length(go_file))
{
  #Try, in order to avoid errors if GOterm is not a MF or dont have any ancestors
  aspect=1
  #Try, in order to avoid errors if GO-term is not a CC or dont have any ancestors
  try(print(aspect<-get(go_file[i],GOMFANCESTOR)),TRUE)
  options(warn=-1)
  if(aspect!=1) #if aspect!=1 aspect is an GOCC
  {
    print(go_file[i]) #print first GO-term if is its a CC
  }
  options(warn=0)
},file=(paste(compvalue,"/gomf_univ.txt",sep="")))

#Open file and keep GO terms only (update file and erase old version)
data=scan(paste(compvalue,"/gomf_univ.txt",sep=""),what="character"())
capture.output(print.go_only(grep(pattern = "GO:" , data, value = TRUE, fixed = TRUE)),file=(paste(compvalue,"/gomf_univ.txt",sep="")))

###RETRIEVE SAMPLE GO-TERMS ANCESTORS###

capture.output(for(i in 1:length(go_ech_file))
{
  #Try, in order to avoid errors if GO-term is not a CC or dont have any ancestors
  aspect=1
  #Try, in order to avoid errors if GO-term is not a CC or dont have any ancestors
  try(print(aspect<-get(go_ech_file[i],GOMFANCESTOR)),TRUE)
  options(warn=-1)
  if(aspect!=1) #if aspect!=1 aspect is an GOCC
  {
    print(go_ech_file[i]) #print first GO-term if is its a CC
  }
  options(warn=0)
},file=(paste(compvalue,"/gomf_ech.txt",sep="")))

#Open file and keep GO terms only (update file and erase old version)
data=scan(paste(compvalue,"/gomf_ech.txt",sep=""),what="character"())#opened with fonction scan (+as character) in order to grep efficiently with go_only
#Save results which only contains GO Id's
capture.output(print.go_only(grep(pattern ="GO:" , data, value = TRUE, fixed = TRUE)),file=(paste(compvalue,"/gomf_ech.txt",sep="")))


######################################################################################################################
############# GO-THREE WALKING AND RELATED STATISTICAL TESTS 
######################################################################################################################


############################################
#HYPERGEOMETRIC TEST
############################################
#phyper(a,b,c,d,lower.tail = TRUE)
#AVEC
#a : GO-term hits in sample
#b : GO-term hits in universe
#c : universe of GO-terms length
#d : GO-terms sample length
#H0: overrepresented GO-term
#H1: not overrepresented GO-term
#Lower.tail = TRUE : invert HO and H1.
#########################################################
#INITIALIZE VALUES FOR UNIVERSE AND DATASETS 
#########################################################
univers_mf=read.table(paste(compvalue,"/gomf_univ.txt",sep=""))
echantillon_mf=read.table(paste(compvalue,"/gomf_ech.txt",sep=""))

univers_cc=read.table(paste(compvalue,"/gocc_univ.txt",sep=""))
echantillon_cc=read.table(paste(compvalue,"/gocc_ech.txt",sep=""))

univers_bp=read.table(paste(compvalue,"/gobp_univ.txt",sep=""))
echantillon_bp=read.table(paste(compvalue,"/gobp_ech.txt",sep=""))
#######################################################

#Special function in order to do not keep undesired characters
onlythis<- function(m)
{
  write.table(format(m, justify="right"),
              row.names=F, col.names=F, quote=F)
}

########################################################
#R SETTINGS AND SOME VALUES SETTINGS
########################################################

Go_univ=univers_mf #Universe
Go_ech=echantillon_mf #Node
options(max.print=99999999) #Raise print capacity
Go_uniq=Go_univ[!duplicated(Go_univ),] #Go_uniq used for loop in order to dont retrieve a goterm multiple times if its duplicated
parent="all" #Root node can be considered as "all" in Go.db

#########################################################
#COMPUTING AND WRITE RESULTS IN FILE FOR EACH ASPECT:
#########################################################

#################### MOLECULAR FUNCTION #################

#Bro-tip: parameters allready set for MF analysis (see behind. But CC and BP need to resetting parameters)

#####PHYPER TEST WITH BONFERRONI CORRECTION#####
pvals=""
for(i in 1:length(Go_uniq))
{
  targeted_goterm=toString(Go_uniq[i]) #tostring in order to request value
  #Bro-tip= lower.tail=TRUE because (lower.tail=TRUE)=FALSE in next loop, for obscure reasons
  pvals[i]<-phyper(length(which(Go_ech==targeted_goterm)),length(which(Go_univ==targeted_goterm)),length(Go_univ[,1])-length(which(Go_univ==targeted_goterm)),length(Go_ech[,1]),lower.tail = FALSE) 
}
pvals2<-as.vector(pvals)
pvals_adjusted<-p.adjust(pvals2, method="bonferroni", n=length(pvals))
a=1

######PHYPER OK, NOW ENHANCE PHYPER RESULTS#####
capture.output(
  #FILE Header
  cat("GO:ID","Go term","Number of hits","Expected number of hits","Go level","P-value","Corrected p-value",sep=";"),
  cat("\n"),
  
  for(i in 1:length(Go_uniq))
  {
    targeted_goterm=toString(Go_uniq[i]) #tostring in order to request value
    #Targeted_goterm: GOterm currently processed##Number of hits##Expected number of hits##phyper(count of this GO in the batch,count of this go in the universe, universe length,batch length)
    #With:number of hits: count of this goterm in the batch
    #expected number of hits: count of the same goterm in the universe
    expectednumberofhits=(((length(which(Go_univ==targeted_goterm)))/(length(Go_univ[,1])))*length(Go_ech[,1]))
    trm=Term(targeted_goterm)
    ##########################################################################
    #RETRIEVE GO-TERM LEVEL : by parents "walking" method (is-a , part-of)
    ##########################################################################
    #First request
    parents=get(targeted_goterm,GOMFPARENTS) 
    #If parents founded-->next DAG level exists.So repeat request with the parents of the next DAG level
    if(parents[1]!=parent)
    {
      level=1 #level in the DAG
      tryCatch({
        for(i in 1:1000) #Arbitrary.
        {
          parents=get(parents[1],GOMFPARENTS) #[1] because prioritize for "is-a"
          level=level+1
          if(parents[1]==parent) stop()#If node ="all" , all go three processed,no more DAG levels.Stop the requests loop
        }
      }, error=function(e){cat()})#Nothing in message error in order to dont print msgerros in results file
    }
    #If no parents founded-->term is on highest level. This is Aspect term-->lvl
    else
    {
      level=1
    }
    #Print results foreach go-term
    if(length(which(Go_ech==targeted_goterm))!=0) #if go-term is present in sample
    {
	    col3=as.character(length(which(Go_ech==targeted_goterm)))
	    col6=as.character(phyper(length(which(Go_ech==targeted_goterm)),length(which(Go_univ==targeted_goterm)),length(Go_univ[,1])-length(which(Go_univ==targeted_goterm)),length(Go_ech[,1]),lower.tail = FALSE))
	    cat(targeted_goterm,trm,col3,expectednumberofhits,level,col6,pvals_adjusted[a],sep=";")
	    cat("\n")
    }
    rm(targeted_goterm)
    a=a+1
  }
  ,file=paste(compvalue,"/hyperesults_mf.txt",sep=""))

#################### CELLULAR COMPOPENT #################

Go_univ=univers_cc
Go_ech=echantillon_cc
Go_uniq=Go_univ[!duplicated(Go_univ),]

#####PHYPER TEST WITH BONFERRONI CORRECTION#####
pvals=""
for(i in 1:length(Go_uniq))
{
  targeted_goterm=toString(Go_uniq[i]) #tostring in order to request value
  #Bro-tip= lower.tail=TRUE because (lower.tail=TRUE)=FALSE in next loop, for obscure reasons
  pvals[i]<-phyper(length(which(Go_ech==targeted_goterm)),length(which(Go_univ==targeted_goterm)),length(Go_univ[,1])-length(which(Go_univ==targeted_goterm)),length(Go_ech[,1]),lower.tail = FALSE) 
}
pvals2<-as.vector(pvals)
pvals_adjusted<-p.adjust(pvals2, method="bonferroni", n=length(pvals))
a=1
######PHYPER OK, NOW ENHANCE PHYPER RESULTS#####
capture.output(
  #FILE Header
  cat("GO:ID","Go term","Number of hits","Expected number of hits","Go level","P-value","Corrected p-value",sep=";"),
  cat("\n"),
  
  for(i in 1:length(Go_uniq))
  {
    targeted_goterm=toString(Go_uniq[i]) #tostring in order to request value
    #Targeted_goterm: GOterm currently processed##Number of hits##Expected number of hits##phyper(count of this GO in the batch,count of this go in the universe, universe length,batch length)
    #With:number of hits: count of this goterm in the batch
    #expected number of hits: count of the same goterm in the universe
    expectednumberofhits=(((length(which(Go_univ==targeted_goterm)))/(length(Go_univ[,1])))*length(Go_ech[,1]))
    trm=Term(targeted_goterm)
    ##########################################################################
    #RETRIEVE GO-TERM LEVEL : by parents "walking" method (is-a , part-of)
    ##########################################################################
    #First request
    parents=get(targeted_goterm,GOCCPARENTS) 
    #If parents founded-->next DAG level exists.So repeat request with the parents of the next DAG level
    if(parents[1]!=parent)
    {
      level=1 #level in the DAG
      tryCatch({
        for(i in 1:1000) #Arbitrary.
        {
          parents=get(parents[1],GOCCPARENTS) #[1] because prioritize for "is-a"
          level=level+1
          if(parents[1]==parent) stop()#If node ="all" , all go three processed,no more DAG levels.Stop the requests loop
        }
      }, error=function(e){cat()})#Nothing in message error in order to dont print msgerros in results file
    }
    #If no parents founded-->term is on highest level. This is Aspect term-->lvl
    else
    {
      level=1
    }
    #Print results foreach go-term
    if(length(which(Go_ech==targeted_goterm))!=0) #if go-term is present in sample
    {
	    col3=as.character(length(which(Go_ech==targeted_goterm)))
	    col6=as.character(phyper(length(which(Go_ech==targeted_goterm)),length(which(Go_univ==targeted_goterm)),length(Go_univ[,1])-length(which(Go_univ==targeted_goterm)),length(Go_ech[,1]),lower.tail = FALSE))
	    cat(targeted_goterm,trm,col3,expectednumberofhits,level,col6,pvals_adjusted[a],sep=";")
	    cat("\n")
    }
    rm(targeted_goterm)
    a=a+1
  }
  ,file=paste(compvalue,"/hyperesults_cc.txt",sep=""))

#################### BIOLOGICAL PROCESS #################

Go_univ=univers_bp
Go_ech=echantillon_bp
Go_uniq=Go_univ[!duplicated(Go_univ),]

#####PHYPER TEST WITH BONFERRONI CORRECTION#####
pvals=""
for(i in 1:length(Go_uniq))
{
  targeted_goterm=toString(Go_uniq[i]) #tostring in order to request value
  #Bro-tip= lower.tail=TRUE because (lower.tail=TRUE)=FALSE in next loop, for obscure reasons
  pvals[i]<-phyper(length(which(Go_ech==targeted_goterm)),length(which(Go_univ==targeted_goterm)),length(Go_univ[,1])-length(which(Go_univ==targeted_goterm)),length(Go_ech[,1]),lower.tail = FALSE) 
}
pvals2<-as.vector(pvals)
pvals_adjusted<-p.adjust(pvals2, method="bonferroni", n=length(pvals))
a=1

######PHYPER OK, NOW ENHANCE PHYPER RESULTS#####
capture.output(
  #FILE Header
  cat("GO:ID","Go term","Number of hits","Expected number of hits","Go level","P-value","Corrected p-value",sep=";"),
  cat("\n"),
  
  for(i in 1:length(Go_uniq))
  {
    targeted_goterm=toString(Go_uniq[i]) #tostring in order to request value
    #Targeted_goterm: GOterm currently processed##Number of hits##Expected number of hits##phyper(count of this GO in the batch,count of this go in the universe, universe length,batch length)
    #With:number of hits: count of this goterm in the batch
    #expected number of hits: count of the same goterm in the universe
    expectednumberofhits=(((length(which(Go_univ==targeted_goterm)))/(length(Go_univ[,1])))*length(Go_ech[,1]))
    trm=Term(targeted_goterm)
    ##########################################################################
    #RETRIEVE GO-TERM LEVEL : by parents "walking" method (is-a , part-of)
    ##########################################################################
    #First request
    parents=get(targeted_goterm,GOBPPARENTS) 
    #If parents founded-->next DAG level exists.So repeat request with the parents of the next DAG level
    if(parents[1]!=parent)
    {
      level=1 #level in the DAG
      tryCatch({
        for(i in 1:1000) #Arbitrary.
        {
          parents=get(parents[1],GOBPPARENTS) #[1] because prioritize for "is-a"
          level=level+1
          if(parents[1]==parent) stop()#If node ="all" , all go three processed,no more DAG levels.Stop the requests loop
        }
      }, error=function(e){cat()})#Nothing in message error in order to dont print msgerros in results file
    }
    #If no parents founded-->term is on highest level. This is Aspect term-->lvl
    else
    {
      level=1
    }
    #Print results foreach go-term
    if(length(which(Go_ech==targeted_goterm))!=0) #if go-term is present in sample
    {
	    col3=as.character(length(which(Go_ech==targeted_goterm)))
	    col6=as.character(phyper(length(which(Go_ech==targeted_goterm)),length(which(Go_univ==targeted_goterm)),length(Go_univ[,1])-length(which(Go_univ==targeted_goterm)),length(Go_ech[,1]),lower.tail = FALSE))
	    cat(targeted_goterm,trm,col3,expectednumberofhits,level,col6,pvals_adjusted[a],sep=";")
	    cat("\n")
	}
    rm(targeted_goterm)
    a=a+1
  }
  ,file=paste(compvalue,"/hyperesults_bp.txt",sep=""))

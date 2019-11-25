args <- commandArgs(trailingOnly=T)
if (length(args)!=1) {
 stop("Requires 1 argument, initial N")
}
N<-as.integer(args[1]) 
steps<-0
while (N !=1) {
 cat (N,"\n")
 if (N%%2==0) {
 N<-N/2
 } else {
 N<-3*N+1
 }
 steps <- steps+1
}
cat("steps=",steps,"\n") 

#Find numbers between 2000 and 3200 which are divisible by 7 and not divisible by 5
val=c()
d=function(x,y)
{
  for(i in (x:y))
  {
    if(i%%7==0 & i%%5!=0)
      val=c(val,i)
  }
  return(val)
}
a=d(2000,3200)
write.csv(a, "output.csv")
getwd()



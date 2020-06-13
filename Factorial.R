#Factorial of given set of numbers

a=vector(length = 3)
n1=as.integer(readline(prompt = "Enter no 1 "))
n2=as.integer(readline(prompt = "Enter no 2 "))
n3=as.integer(readline(prompt = "Enter no 3 "))
a=c(n1,n2,n3)
a
val=c()
for(i in (1:length(a)))
{
  factorial_a= factorial(a[i])
  val=c(val,factorial_a)
}
write.csv(val, "out.csv")



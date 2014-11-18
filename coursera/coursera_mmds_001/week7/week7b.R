N <- 4
beta <- 0.7
iterations <- 1000
M <- matrix(c(0, 1/2, 1/2, 0,
              1,0,0,0,
              0,0,0,1,
              0,0,1,0), ncol=N, byrow=FALSE)

S <- c(1,2)
A <- beta * M
r <- as.matrix(c(1/N, 1/N, 1/N, 1/N))

# Here, pointA, and pointB are the only points that will be teleported to
# also, they specify that the probability to A is twice as high as B.

for (i in 1:iterations){
  r <- A %*% r +  (1-beta) * as.matrix(c(2/3, 1/3, 0, 0))
}

a <- r[1,1]
b <- r[2,1]
c <- r[3,1]
d <- r[4,1]

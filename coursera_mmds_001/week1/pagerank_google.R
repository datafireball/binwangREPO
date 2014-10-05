# Here is the implementation of google page rank formulation 
# Where 
# beta: taxation (avoid spider trap, end node)
# N: number of nodes
# iterations: number of power iterations
# r: page rank
# A: stochastic adjacency matrix 
# M: adjacency matrix

N <- 3
beta <- 0.8
iterations <- 100
M <- matrix(c(0, 1/2, 1/2,
              0,0,1,
              1,0,0), ncol=N, byrow=FALSE)

A <- beta * M + (1-beta) * matrix(rep(1/N, N*N), ncol=N)

r <- as.matrix(c(1/3, 1/3, 1/3))
for (i in 1:iterations){
  r <- A %*% r
}

a <- r[1,1]
b <- r[2,1]
c <- r[3,1]

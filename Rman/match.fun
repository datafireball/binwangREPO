#!/usr/bin/Rscript
source('script.R')

cmd1 <- "match.fun(sum)"
learn(cmd1)

cmd2 <- "match.fun('sum')"
learn(cmd2)

cmd3 <- "match.fun('1')"
learn(cmd3)

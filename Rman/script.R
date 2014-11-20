#!/usr/bin/Rscript

learn <- function(command_string){
    cat('>', command_string, '\n')
    print(eval(parse(text=command_string)))
    cat('\n')
}

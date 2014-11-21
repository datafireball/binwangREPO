#!/usr/bin/Rscript

learn <- function(command_string){
    cat('>', command_string, '\n')
    tryCatch(
        {
            print(eval(parse(text=command_string)))
            cat('\n')
        },
        error=function(e){
            cat(as.character(e))
        }
    )
}

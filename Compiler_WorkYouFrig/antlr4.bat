SET CLASSPATH=.;C:\Users\Sam\git\repository2\Compiler_WorkYouFrig\antlr-4.5.3-complete.jar;%CLASSPATH%
java org.antlr.v4.Tool %*
doskey antlr4=java org.antlr.v4.Tool $*
cmd /k 
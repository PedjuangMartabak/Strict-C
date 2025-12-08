# Generated from CleanCode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CleanCodeParser import CleanCodeParser
else:
    from CleanCodeParser import CleanCodeParser

# This class defines a complete listener for a parse tree produced by CleanCodeParser.
class CleanCodeListener(ParseTreeListener):

    # Enter a parse tree produced by CleanCodeParser#file.
    def enterFile(self, ctx:CleanCodeParser.FileContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#file.
    def exitFile(self, ctx:CleanCodeParser.FileContext):
        pass


    # Enter a parse tree produced by CleanCodeParser#classDef.
    def enterClassDef(self, ctx:CleanCodeParser.ClassDefContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#classDef.
    def exitClassDef(self, ctx:CleanCodeParser.ClassDefContext):
        pass


    # Enter a parse tree produced by CleanCodeParser#function.
    def enterFunction(self, ctx:CleanCodeParser.FunctionContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#function.
    def exitFunction(self, ctx:CleanCodeParser.FunctionContext):
        pass


    # Enter a parse tree produced by CleanCodeParser#paramList.
    def enterParamList(self, ctx:CleanCodeParser.ParamListContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#paramList.
    def exitParamList(self, ctx:CleanCodeParser.ParamListContext):
        pass


    # Enter a parse tree produced by CleanCodeParser#param.
    def enterParam(self, ctx:CleanCodeParser.ParamContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#param.
    def exitParam(self, ctx:CleanCodeParser.ParamContext):
        pass


    # Enter a parse tree produced by CleanCodeParser#lineOfCode.
    def enterLineOfCode(self, ctx:CleanCodeParser.LineOfCodeContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#lineOfCode.
    def exitLineOfCode(self, ctx:CleanCodeParser.LineOfCodeContext):
        pass


    # Enter a parse tree produced by CleanCodeParser#assignment.
    def enterAssignment(self, ctx:CleanCodeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#assignment.
    def exitAssignment(self, ctx:CleanCodeParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CleanCodeParser#funcCall.
    def enterFuncCall(self, ctx:CleanCodeParser.FuncCallContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#funcCall.
    def exitFuncCall(self, ctx:CleanCodeParser.FuncCallContext):
        pass


    # Enter a parse tree produced by CleanCodeParser#returnStmt.
    def enterReturnStmt(self, ctx:CleanCodeParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#returnStmt.
    def exitReturnStmt(self, ctx:CleanCodeParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by CleanCodeParser#type.
    def enterType(self, ctx:CleanCodeParser.TypeContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#type.
    def exitType(self, ctx:CleanCodeParser.TypeContext):
        pass


    # Enter a parse tree produced by CleanCodeParser#args.
    def enterArgs(self, ctx:CleanCodeParser.ArgsContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#args.
    def exitArgs(self, ctx:CleanCodeParser.ArgsContext):
        pass


    # Enter a parse tree produced by CleanCodeParser#expr.
    def enterExpr(self, ctx:CleanCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by CleanCodeParser#expr.
    def exitExpr(self, ctx:CleanCodeParser.ExprContext):
        pass



del CleanCodeParser
# Generated from CleanCode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CleanCodeParser import CleanCodeParser
else:
    from CleanCodeParser import CleanCodeParser

# This class defines a complete generic visitor for a parse tree produced by CleanCodeParser.

class CleanCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CleanCodeParser#file.
    def visitFile(self, ctx:CleanCodeParser.FileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CleanCodeParser#classDef.
    def visitClassDef(self, ctx:CleanCodeParser.ClassDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CleanCodeParser#function.
    def visitFunction(self, ctx:CleanCodeParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CleanCodeParser#paramList.
    def visitParamList(self, ctx:CleanCodeParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CleanCodeParser#param.
    def visitParam(self, ctx:CleanCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CleanCodeParser#lineOfCode.
    def visitLineOfCode(self, ctx:CleanCodeParser.LineOfCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CleanCodeParser#assignment.
    def visitAssignment(self, ctx:CleanCodeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CleanCodeParser#funcCall.
    def visitFuncCall(self, ctx:CleanCodeParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CleanCodeParser#returnStmt.
    def visitReturnStmt(self, ctx:CleanCodeParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CleanCodeParser#type.
    def visitType(self, ctx:CleanCodeParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CleanCodeParser#args.
    def visitArgs(self, ctx:CleanCodeParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CleanCodeParser#expr.
    def visitExpr(self, ctx:CleanCodeParser.ExprContext):
        return self.visitChildren(ctx)



del CleanCodeParser
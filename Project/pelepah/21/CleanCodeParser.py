# Generated from CleanCode.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,97,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,1,1,1,1,2,1,2,1,
        2,1,2,3,2,44,8,2,1,2,1,2,1,2,5,2,49,8,2,10,2,12,2,52,9,2,1,2,1,2,
        1,3,1,3,1,3,5,3,59,8,3,10,3,12,3,62,9,3,1,4,1,4,1,4,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,76,8,6,1,6,1,6,1,6,3,6,81,8,6,3,6,83,
        8,6,1,7,1,7,1,8,1,8,1,8,5,8,90,8,8,10,8,12,8,93,9,8,1,9,1,9,1,9,
        0,0,10,0,2,4,6,8,10,12,14,16,18,0,2,1,0,11,14,1,0,14,16,96,0,23,
        1,0,0,0,2,28,1,0,0,0,4,39,1,0,0,0,6,55,1,0,0,0,8,63,1,0,0,0,10,66,
        1,0,0,0,12,82,1,0,0,0,14,84,1,0,0,0,16,86,1,0,0,0,18,94,1,0,0,0,
        20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,
        0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,
        29,5,1,0,0,29,30,5,14,0,0,30,34,5,2,0,0,31,33,3,4,2,0,32,31,1,0,
        0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,
        1,0,0,0,37,38,5,3,0,0,38,3,1,0,0,0,39,40,5,4,0,0,40,41,5,14,0,0,
        41,43,5,5,0,0,42,44,3,6,3,0,43,42,1,0,0,0,43,44,1,0,0,0,44,45,1,
        0,0,0,45,46,5,6,0,0,46,50,5,2,0,0,47,49,3,10,5,0,48,47,1,0,0,0,49,
        52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,
        0,53,54,5,3,0,0,54,5,1,0,0,0,55,60,3,8,4,0,56,57,5,7,0,0,57,59,3,
        8,4,0,58,56,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,
        7,1,0,0,0,62,60,1,0,0,0,63,64,3,14,7,0,64,65,5,14,0,0,65,9,1,0,0,
        0,66,67,3,12,6,0,67,68,5,8,0,0,68,11,1,0,0,0,69,70,5,14,0,0,70,71,
        5,9,0,0,71,83,3,18,9,0,72,73,5,14,0,0,73,75,5,5,0,0,74,76,3,16,8,
        0,75,74,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,83,5,6,0,0,78,80,
        5,10,0,0,79,81,3,18,9,0,80,79,1,0,0,0,80,81,1,0,0,0,81,83,1,0,0,
        0,82,69,1,0,0,0,82,72,1,0,0,0,82,78,1,0,0,0,83,13,1,0,0,0,84,85,
        7,0,0,0,85,15,1,0,0,0,86,91,3,18,9,0,87,88,5,7,0,0,88,90,3,18,9,
        0,89,87,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,17,
        1,0,0,0,93,91,1,0,0,0,94,95,7,1,0,0,95,19,1,0,0,0,9,23,34,43,50,
        60,75,80,82,91
    ]

class CleanCodeParser ( Parser ):

    grammarFileName = "CleanCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'{'", "'}'", "'def'", "'('", 
                     "')'", "','", "';'", "'='", "'return'", "'int'", "'string'", 
                     "'void'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "STRING", "WS" ]

    RULE_file = 0
    RULE_classDef = 1
    RULE_function = 2
    RULE_paramList = 3
    RULE_param = 4
    RULE_lineOfCode = 5
    RULE_statement = 6
    RULE_type = 7
    RULE_args = 8
    RULE_expr = 9

    ruleNames =  [ "file", "classDef", "function", "paramList", "param", 
                   "lineOfCode", "statement", "type", "args", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    ID=14
    INT=15
    STRING=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CleanCodeParser.EOF, 0)

        def classDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CleanCodeParser.ClassDefContext)
            else:
                return self.getTypedRuleContext(CleanCodeParser.ClassDefContext,i)


        def getRuleIndex(self):
            return CleanCodeParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile" ):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = CleanCodeParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 20
                self.classDef()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(CleanCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CleanCodeParser.ID, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CleanCodeParser.FunctionContext)
            else:
                return self.getTypedRuleContext(CleanCodeParser.FunctionContext,i)


        def getRuleIndex(self):
            return CleanCodeParser.RULE_classDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDef" ):
                listener.enterClassDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDef" ):
                listener.exitClassDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDef" ):
                return visitor.visitClassDef(self)
            else:
                return visitor.visitChildren(self)




    def classDef(self):

        localctx = CleanCodeParser.ClassDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(CleanCodeParser.T__0)
            self.state = 29
            self.match(CleanCodeParser.ID)
            self.state = 30
            self.match(CleanCodeParser.T__1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 31
                self.function()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(CleanCodeParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CleanCodeParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(CleanCodeParser.ParamListContext,0)


        def lineOfCode(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CleanCodeParser.LineOfCodeContext)
            else:
                return self.getTypedRuleContext(CleanCodeParser.LineOfCodeContext,i)


        def getRuleIndex(self):
            return CleanCodeParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = CleanCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(CleanCodeParser.T__3)
            self.state = 40
            self.match(CleanCodeParser.ID)
            self.state = 41
            self.match(CleanCodeParser.T__4)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0):
                self.state = 42
                self.paramList()


            self.state = 45
            self.match(CleanCodeParser.T__5)
            self.state = 46
            self.match(CleanCodeParser.T__1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==14:
                self.state = 47
                self.lineOfCode()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(CleanCodeParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CleanCodeParser.ParamContext)
            else:
                return self.getTypedRuleContext(CleanCodeParser.ParamContext,i)


        def getRuleIndex(self):
            return CleanCodeParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = CleanCodeParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.param()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 56
                self.match(CleanCodeParser.T__6)
                self.state = 57
                self.param()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CleanCodeParser.TypeContext,0)


        def ID(self):
            return self.getToken(CleanCodeParser.ID, 0)

        def getRuleIndex(self):
            return CleanCodeParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = CleanCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.type_()
            self.state = 64
            self.match(CleanCodeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineOfCodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(CleanCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return CleanCodeParser.RULE_lineOfCode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineOfCode" ):
                listener.enterLineOfCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineOfCode" ):
                listener.exitLineOfCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineOfCode" ):
                return visitor.visitLineOfCode(self)
            else:
                return visitor.visitChildren(self)




    def lineOfCode(self):

        localctx = CleanCodeParser.LineOfCodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lineOfCode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.statement()
            self.state = 67
            self.match(CleanCodeParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CleanCodeParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CleanCodeParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CleanCodeParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(CleanCodeParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CleanCodeParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CleanCodeParser.ID, 0)
        def args(self):
            return self.getTypedRuleContext(CleanCodeParser.ArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)


    class ReturnStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CleanCodeParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CleanCodeParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = CleanCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = CleanCodeParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(CleanCodeParser.ID)
                self.state = 70
                self.match(CleanCodeParser.T__8)
                self.state = 71
                self.expr()
                pass

            elif la_ == 2:
                localctx = CleanCodeParser.FuncCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(CleanCodeParser.ID)
                self.state = 73
                self.match(CleanCodeParser.T__4)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                    self.state = 74
                    self.args()


                self.state = 77
                self.match(CleanCodeParser.T__5)
                pass

            elif la_ == 3:
                localctx = CleanCodeParser.ReturnStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.match(CleanCodeParser.T__9)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                    self.state = 79
                    self.expr()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CleanCodeParser.ID, 0)

        def getRuleIndex(self):
            return CleanCodeParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = CleanCodeParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CleanCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(CleanCodeParser.ExprContext,i)


        def getRuleIndex(self):
            return CleanCodeParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = CleanCodeParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.expr()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 87
                self.match(CleanCodeParser.T__6)
                self.state = 88
                self.expr()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CleanCodeParser.ID, 0)

        def INT(self):
            return self.getToken(CleanCodeParser.INT, 0)

        def STRING(self):
            return self.getToken(CleanCodeParser.STRING, 0)

        def getRuleIndex(self):
            return CleanCodeParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CleanCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






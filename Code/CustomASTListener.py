
from Gen.AssignmentStatementListener import AssignmentStatementListener
from Gen.AssignmentStatementParser import AssignmentStatementParser
from default_codes.ast import AST
from default_codes.make_ast_subtree import make_ast_subtree


class ASTListener(AssignmentStatementListener):
    def __init__(self, rule_names):
        self.overridden_rules = ['compoundst', 'declaration', 'assign', 'casedefault', 'ifst', 'ternary']
        self.binary_operator_list = ['term', 'expr', 'cond']
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            if rule_name in self.binary_operator_list and ctx.getChildCount() > 1:
                make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText())
            else:
                make_ast_subtree(self.ast, ctx, rule_name)

    def exitCompoundst(self, ctx:AssignmentStatementParser.CompoundstContext):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "block", True)

    def exitAssign(self, ctx:AssignmentStatementParser.AssignContext):
        make_ast_subtree(self.ast, ctx, "=", True)

    def exitCasedefault(self, ctx:AssignmentStatementParser.CasedefaultContext):
        make_ast_subtree(self.ast, ctx, 'casedefault', True)

    def exitIfst(self, ctx: AssignmentStatementParser.CasedefaultContext):
        make_ast_subtree(self.ast, ctx, 'if', True)

    def exitTernary(self, ctx: AssignmentStatementParser.CasedefaultContext):
        make_ast_subtree(self.ast, ctx, '?', True)


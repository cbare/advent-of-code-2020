"""
Advent of Code 2020 - Day 18
"""

examples = [
    ('1 + 2 * 3 + 4 * 5 + 6', 71),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 26),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
]

class AstNode:
    pass

class OpNode(AstNode):
    def __init__(self, op, a, b):
        self.op = op
        self.a = a
        self.b = b
    def __repr__(self):
        return f'({self.a} {self.op} {self.b})'


def tokenize(s):
    acc = ''
    i = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue
        elif s[i] in '+*()':
            yield s[i]
            i += 1
        elif s[i] in '0123456789':
            acc += s[i]
            i += 1
            while i < len(s) and s[i] in '0123456789':
                acc += s[i]
                i += 1
            yield int(acc)
            acc = ''


def parse_sub(stack):
    b = stack.pop()
    assert isinstance(b,int) or isinstance(b, AstNode), f'expected arg, got {b}'
    if len(stack) == 0 or stack[-1] == '(':
        return b
    op = stack.pop()
    assert op in '+*', f'expected op, got {op}'
    a = stack.pop()
    assert isinstance(a,int) or isinstance(a, AstNode), f'expected arg, got {a}'
    return OpNode(op,a,b)

def parse(expr):
    stack = []
    for tok in tokenize(expr):
        if tok == ')':
            node = parse_sub(stack)
            paren = stack.pop()
            assert paren == '('
            stack.append(node)
        elif tok == '+' or tok == '*':
            node = parse_sub(stack)
            stack.append(node)
            stack.append(tok)
        else:
            stack.append(tok)

    while len(stack) > 1:
        node = parse_sub(stack)
        stack.append(node)
    
    return stack.pop()


def evaluate(x):
    if isinstance(x,int):
        return x
    elif isinstance(x, OpNode):
        if x.op == '+':
            return evaluate(x.a) + evaluate(x.b)
        elif x.op == '*':
            return evaluate(x.a) * evaluate(x.b)
    raise RuntimeError('error!')


def test(examples):
    for expr, expected in examples:
        ast = parse(expr)
        result = evaluate(ast)
        if result == expected:
            print(f'{expr:50} = {result:5}: ok')
        else:
            print(f'{expr:50} = {result:5}: error')


parse('1 + 2 * 3 + 4 * 5 + 6')
parse('1 + (2 * 3) + (4 * (5 + 6))')
test(examples)



# part 1

with open('puzzle-18-input.txt') as f:
    exprs = [line.strip() for line in f]

sum(evaluate(parse(expr)) for expr in exprs)
# Out[254]: 6923486965641


# part 2

# This implements something called Pratt Top-Down operator precedence parsing
# described here: http://effbot.org/zone/simple-top-down-parsing.htm
#       and here: https://eli.thegreenplace.net/2010/01/02/top-down-operator-precedence-parsing/


ops = {
    '(': 0,
    ')': 0,
    '+': 20,
    '*': 10
}

def tokenize(expr):
    for number, operator in re.findall(r'\s*(?:(\d+)|(.))', expr):
        if number:
            yield int(number)
        elif operator in ops:
            yield operator
        else:
            raise SyntaxError(f'unknown operator: {operator}')

def process_stack(stack):
    b = stack.pop()
    if len(stack) == 0 or stack[-1] == '(':
        return b, 0
    op = stack.pop()
    a = stack.pop()
    rbp = ops[stack[-1]] if stack else 0
    return OpNode(op,a,b), rbp

def parse(expr):
    rbp = 0
    stack = []
    ts = tokenize(expr)
    for t in ts:
        if t == '(':
            rbp = ops[t]
            stack.append(t)
        elif t == ')':
            lbp = ops[t]
            while lbp < rbp:
                left, rbp = process_stack(stack)
                stack.append(left)
            left = stack.pop()
            lparen = stack.pop()
            assert lparen == '('
            rbp = ops[stack[-1]] if stack else 0
            stack.append(left)
        elif t in ops:
            lbp = ops[t]
            while lbp <= rbp:
                left, rbp = process_stack(stack)
                stack.append(left)
            rbp = lbp
            stack.append(t)
        else:
            stack.append(t)

    while len(stack) > 1:
        left, rbp = process_stack(stack)
        stack.append(left)

    return stack.pop()

parse('1 + 2 * 3 + 4 * 5 + 6')
# ((1 + 2) * ((3 + 4) * (5 + 6)))

parse('1 + (2 * 3) + (4 * (5 + 6))')

parse('5 + (8 * 3 + 9 + 3 * 4 * 3)')

examples = [
    ('1 + 2 * 3 + 4 * 5 + 6', 231),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 46),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340),
]
test(examples)

# part 2

with open('puzzle-18-input.txt') as f:
    exprs = [line.strip() for line in f]

sum(evaluate(parse(expr)) for expr in exprs)
# Out[323]: 70722650566361


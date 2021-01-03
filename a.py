from itertools import product

seq_num = ['987654321']
op_set = ('-', '+', '*', '')

seq_op = tuple(product(op_set, repeat = 8))
op_first = ('-', '+')
seq_op = [[*tuple(i) + j] for i in op_first for j in seq_op]

# exps = [''.join([''.join(p) for p in list(zip(o, n))]) for o, n in product(seq_op, seq_num)]
exps = [list(zip(o, n)) for o, n in product(seq_op, seq_num)]
exps = [''.join(sum(e, ())) for e in exps]

for e in exps:
  if eval(e) == 2021:
      print(e)

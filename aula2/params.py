from argparse import ArgumentParser

ap = ArgumentParser()

ap.add_argument(
  '--a',
  type=int,
  required=True,
  default=0,
  help="Valor de a é usado para flag"
)

ap.add_argument(
  '--b',
  type=int,
  required=True
)

ap.add_argument(
  '--operacao',
  '--o',
  type=str,
  default="adicao",
  help="Operação",
  choices=['adicao', 'subtracao', 'divisao', 'multiplicacao']
)

args = ap.parse_args()

operacoes = {
  'adicao': lambda a, b: a + b,
  'subtracao': lambda a, b: a - b,
  'adicao': lambda a, b: a + b,
  'multiplicacao': lambda a, b: a * b,
  'divisao': lambda a, b: a / b,
}

fn = operacoes[args.operacao]
print(fn(args.a, args.b))
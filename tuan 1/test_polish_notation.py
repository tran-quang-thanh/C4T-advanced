from polish_notation import PolishNotation

pn = PolishNotation()

assert(pn.calculate("46+") == 10)
assert(pn.calculate("76-") == 1)
assert(pn.calculate("23*") == 6)
assert(pn.calculate("42/") == 2)

assert(pn.calculate("46+7-") == 3)
assert(pn.calculate("46+7-23*-") == -3)
assert(pn.calculate("46+7-23*-343-/+") == 0)
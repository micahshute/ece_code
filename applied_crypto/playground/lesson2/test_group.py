from python_resources.mod_multiplicative_group import *


mg = ModMultiplicativeGroup(11)

print(f"Z*11: {mg.values}")
print([f"Generator: {gen}, Group: {group.values}" for gen, group in mg.generators()])
import time
from IPython.display import display, Math
from sympy import printing

def show_expr(expr, plain_latex=False):
    """Helper function to display Math expressions"""
    if plain_latex:
        return printing.latex(expr)
    return display(Math(printing.latex(expr)))

def evolv(state):
    """Helps determine the childs of a state"""
    finished = False
    goesto = []
    while not finished:
        finished = True
        candidate = list(state)
        for i, c in enumerate(state):
            if c > 0:
                candidate[i] -= 1
                try:
                    candidate[i+1] += 1
                except IndexError:
                    pass
                if [tuple(candidate), i] not in goesto:
                    goesto.append([tuple(candidate), i])
                    finished = False
                    break
                else:
                    candidate = list(state)
    return goesto


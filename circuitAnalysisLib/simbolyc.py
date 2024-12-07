import numpy as np												# Math utilities
from sympy import symbols										# For symbolic resolution of problems
from sympy import cancel, simplify, latex, inverse_laplace_transform
from IPython.display import display, Math						# For prettier display of expresions

class simbolyc:
	S = symbols('s')
	t = symbols('t')
	def __init__(self):
		pass

	@staticmethod
	def Zinductor(L=1):
		return simbolyc.S*L
	@staticmethod
	def Zcapacitor(C=1):
		return 1/(simbolyc.S*C)
	@staticmethod
	def Yinductor(L=1):
		return 1/(simbolyc.S*L)
	@staticmethod
	def Ycapacitor(C=1):
		return simbolyc.S*C
	@staticmethod
	def laplace_to_time(H_s):               #Cuidado con funciones muy complejas acá
		return inverse_laplace_transform(H_s, simbolyc.S, simbolyc.t)

	@staticmethod
	def print_latex(expr):
		expr = simplify(expr)
		num , den = expr.as_numer_denom()
		expr = cancel(num/den)    # Lo transforma en un cociente de polinomios. Eliminar en caso de no buscar eso.
		display(Math(latex(expr)))
		return None

	@staticmethod
	def eficaz(A):
		return np.sqrt(np.mean(A**2))

	@staticmethod
	def paralelo(*Zargs):
		if len(Zargs) == 0:
			raise ValueError("Se requiere al menos un impedancia para calcular el paralelo.")
		return 1/sum(1/arg for arg in Zargs)
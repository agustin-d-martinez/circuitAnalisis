import numpy as np												# Math utilities
import matplotlib.pyplot as plt                                 # For graph and plot of functions
from sympy import Poly											# For symbolic resolution of problems
from scipy import signal                                        # Signals utilities

from .simbolyc import simbolyc

class graphic:
	@staticmethod
	def bodeMagnitude(H , w = None, plot_figure=True ):
		"""
		Imprime el diagrama de bode de amplitud para una transferencia simbolica
		Args:
			H: Función a graficar. Debe estar en funcion a la variable S.
			w (array): vector de frecuencias a utilizar. No es requerido.
			plot_figure (bool): Si es True grafica la salida.

		Returns:
			mag: Módulo del diagrama de bode.
			w: Vector de frecuencias.
		"""
		num = H.num
		den = H.den
		H_EXPRESION = Poly(num, simbolyc.S)/Poly(den, simbolyc.S)
		simbolyc.print_latex(H_EXPRESION)

		w, Hfreq = signal.freqresp( H , w)
		mag = 20 * np.log10(np.abs(Hfreq))

		if plot_figure:
			plt.figure()
			plt.semilogx(w, mag)  # Eje x logarítmico para la frecuencia
			plt.ylabel('Magnitud (dB)')
			plt.grid(True)
			plt.title('Diagrama de Bode')
			plt.show()
		return mag , w

	@staticmethod
	def bodePhase(H , w = None, plot_figure=True):
		num = H.num
		den = H.den
		H_EXPRESION = Poly(num, simbolyc.S)/Poly(den, simbolyc.S)
		simbolyc.print_latex(H_EXPRESION)

		w, Hfreq = signal.freqresp( H , w)

		phase = np.angle(Hfreq, deg=True)

		if plot_figure:
			plt.figure()
			plt.title('Diagrama de Bode')
			plt.semilogx(w, phase)
			plt.ylabel('Fase (grados)')
			plt.xlabel('Frecuencia (rad/s)')
			plt.grid(True)
			plt.show()
		return phase , w

	@staticmethod
	def bode(H , w = None, plot_figure=True):
		num = H.num
		den = H.den
		H_EXPRESION = Poly(num, simbolyc.S)/Poly(den, simbolyc.S)
		simbolyc.print_latex(H_EXPRESION)

		w, Hfreq = signal.freqresp( H , w)

		mag = 20 * np.log10(np.abs(Hfreq))
		phase = np.angle(Hfreq, deg=True)

		if plot_figure:
			plt.figure()
			plt.subplot(1, 2, 1)
			plt.semilogx(w, mag)  # Eje x logarítmico para la frecuencia
			plt.ylabel('Magnitud (dB)')
			plt.grid(True)
			plt.title('Diagrama de Bode')
			plt.subplot(1, 2, 2)
			plt.semilogx(w, phase)
			plt.ylabel('Fase (grados)')
			plt.xlabel('Frecuencia (rad/s)')
			plt.grid(True)
			plt.show()

		return mag , phase , w
	
	@staticmethod
	def plot(x , Y , title=None , xlabel=None , ylabel=None, grid=False ):
		plt.figure()
		plt.plot(x, Y)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.grid(grid)
		plt.title(title)
		plt.show()
		return None
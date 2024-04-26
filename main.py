import matplotlib.pyplot as plt
import numpy as np


def tableModulaire(table, modulo):
	angles = np.linspace(0, 2*np.pi, 1000)
	points = np.linspace(0, 2*np.pi, modulo)

	cosinusAngles = np.cos(angles)
	sinusAngles = np.sin(angles)

	cosinusPoints = np.cos(points + np.pi/2)
	sinusPoints = np.sin(points + np.pi/2)

	plt.figure()
	plt.plot(cosinusAngles, sinusAngles)
	plt.plot(cosinusPoints, sinusPoints, 'o')
	plt.axis('equal')
	plt.show()


if __name__ == "__main__":
	# table = input("Quelle table allons nous tracer ? ")
	# modulo = input("Modulo ? ")
	table = 2
	modulo = 10
	tableModulaire(table, modulo)

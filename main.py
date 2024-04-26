import matplotlib.pyplot as plt
import numpy as np


def tableModulaire(table, modulo):
	angles = np.linspace(2*np.pi, 0, 1000)
	points = np.linspace(2*np.pi, 0, modulo+1)

	cosinusAngles = np.cos(angles)
	sinusAngles = np.sin(angles)

	cosinusPoints = np.cos(points + np.pi/2)
	sinusPoints = np.sin(points + np.pi/2)

	plt.figure()
	plt.plot(cosinusAngles, sinusAngles)
	plt.plot(cosinusPoints, sinusPoints, 'o')
	
	for i in range(0, len(cosinusPoints)-1):
		plt.text(cosinusPoints[i], sinusPoints[i], f"{i}")

	plt.axis('equal')
	plt.show()


if __name__ == "__main__":
	# table = input("Quelle table allons nous tracer ? ")
	# modulo = input("Modulo ? ")
	table = 2
	modulo = 100
	tableModulaire(table, modulo)

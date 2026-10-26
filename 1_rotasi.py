import numpy as np
import matplotlib.pyplot as plt

titik_lama = np.array([[0,0], [1,0], [1,1], [0,1]])
sudut = 90
theta = np.radians(sudut) 

pusat = np.mean(titik_lama, axis=0)

rotasi = np.array([[np.cos(theta), -np.sin(theta)],
                   [np.sin(theta), np.cos(theta)]])

titik_rotasi = (titik_lama - pusat) @ rotasi.T + pusat

print("Titik awal:\n", titik_lama)
print("\nTitik hasil rotasi:\n", titik_rotasi)

# Grafik
plt.figure(figsize=(10,6))
plt.fill(titik_lama[:,0], titik_lama[:,1], fill=False, edgecolor="skyblue", linewidth=10, label="Persegi Awal")
plt.fill(titik_rotasi[:,0], titik_rotasi[:,1], fill=False, edgecolor="red", linewidth=2, linestyle="--", label="Hasil Rotasi 90°")
plt.axis("equal")
plt.grid()
plt.title("Rotasi Persegi")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()


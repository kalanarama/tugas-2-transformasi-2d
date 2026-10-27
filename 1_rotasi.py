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
print("Titik hasil rotasi:\n", np.round(titik_rotasi, 2))

# Grafik
plt.figure(figsize=(10,6))
plt.fill(titik_lama[:,0], titik_lama[:,1], fill=False, edgecolor="skyblue", linewidth=10, label="Persegi Awal")
plt.fill(titik_rotasi[:,0], titik_rotasi[:,1], fill=False, edgecolor="red", linewidth=2, linestyle="--", label="Hasil Rotasi 90°")

# Menampilkan titik koordinat
nama_awal = ["A", "B", "C", "D"]
nama_hasil = ["A'", "B'", "C'", "D'"]

for i in range(4):
    x, y = titik_lama[i]
    plt.annotate(f"{nama_awal[i]}({x:.0f},{y:.0f})",
                 (x, y), xytext=(5, -15), textcoords="offset points",
                 color="skyblue")

for i in range(4):
    x, y = titik_rotasi[i]
    plt.annotate(f"{nama_hasil[i]}({x:.0f},{y:.0f})",
                 (x, y), xytext=(5, 5), textcoords="offset points",
                 color="red")

plt.scatter(pusat[0], pusat[1], color="purple", label="Titik Pusat Rotasi")
plt.text(0.55, 1.15, "Rotasi 90°", color="black")

plt.axis("equal")
plt.grid()
plt.title("Rotasi Persegi")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()


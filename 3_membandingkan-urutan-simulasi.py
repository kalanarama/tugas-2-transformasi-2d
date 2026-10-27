import numpy as np
import matplotlib.pyplot as plt

titik_lama = np.array([[1,1], [4,1], [2,4]])
print("Titik awal:\n", titik_lama)
translasi = np.array([2,1])
scaling = np.array([2,2])
sudut = 90

theta = np.radians(sudut)
rotasi = np.array([[np.cos(theta), -np.sin(theta)],
                   [np.sin(theta), np.cos(theta)]])

# Translasi→Rotasi→Scaling
titik_translasi_1 = translasi + titik_lama
titik_rotasi_1 = titik_translasi_1 @ rotasi.T
titik_scaling_1 = titik_rotasi_1 * scaling

print("\n==============Translasi→Rotasi→Scaling=========")
print("Hasil Translasi: \n", titik_translasi_1)
print("Hasil rotasi:\n", titik_rotasi_1)
print("Hasil scaling:\n", titik_scaling_1)

# Scaling→Rotasi→Translasi 
titik_scaling_2 = titik_lama * scaling
titik_rotasi_2 = titik_scaling_2 @ rotasi.T
titik_translasi_2 = titik_rotasi_2 + translasi

print("\n=========Scaling→Rotasi→Translasi ===========")
print("Hasil scaling:\n", titik_scaling_2)
print("Hasil rotasi:\n", titik_rotasi_2)
print("Hasil Translasi: \n", titik_translasi_2)

# Perbandingan
print("\nTitik awal:", titik_lama)
print("Hasil urutan Translasi→Rotasi→Scaling:\n",np.round(titik_scaling_1,2))
print("Hasil urutan Scaling→Rotasi→Translasi:\n", np.round(titik_translasi_2,2))

# Grafik
plt.figure(figsize=(10,6))
plt.fill(titik_lama[:,0], titik_lama[:,1], fill=False, edgecolor="teal", linewidth=3, label="Segitiga Awal")
plt.fill(titik_scaling_1[:,0], titik_scaling_1[:,1], fill=False, edgecolor="red", linewidth=2, linestyle="--", label="Translasi - Rotasi - Scaling")
plt.fill(titik_translasi_2[:,0], titik_translasi_2[:,1], fill=False, edgecolor="blue", linewidth=2, linestyle="--", label="Scaling - Rotasi - Translasi")

plt.scatter(titik_lama[:,0], titik_lama[:,1], color="teal")
plt.scatter(titik_scaling_1[:,0], titik_scaling_1[:,1], color="red")
plt.scatter(titik_translasi_2[:,0], titik_translasi_2[:,1], color="blue")

# Menampilkan titik koordinat
nama_titik = ["A", "B", "C"]

for i in range(3):
    # Titik segitiga awal
    x, y = np.round(titik_lama[i], 2)
    plt.annotate(f"{nama_titik[i]}({x:g},{y:g})",
                 (x, y), xytext=(5, 7),
                 textcoords="offset points", color="teal", fontsize=9)

    # Titik hasil Translasi - Rotasi - Scaling
    x, y = np.round(titik_scaling_1[i], 2)
    plt.annotate(f"{nama_titik[i]}({x:g},{y:g})",
                 (x, y), xytext=(5, 7),
                 textcoords="offset points", color="red", fontsize=9)

    # Titik hasil Scaling - Rotasi - Translasi
    x, y = np.round(titik_translasi_2[i], 2)
    plt.annotate(f"{nama_titik[i]}({x:g},{y:g})",
                 (x, y), xytext=(5, 7),
                 textcoords="offset points", color="blue", fontsize=9)


plt.title("Perbandingan Urutan Transformasi 2D")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.axis("equal")
plt.grid()
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

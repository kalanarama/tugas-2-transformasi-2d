import numpy as np
import matplotlib.pyplot as plt

total_vertex = int(input("Masukkan jumlah vertex (minimal 5 vertex): "))
while total_vertex < 5:
    print("Jumlah vertex ", total_vertex, ", sehingga kurang dari 5")
    total_vertex = int(input("Masukkan ulang jumlah vertex (min. 5): "))

titik = []
for i in range(total_vertex):
    print(f"Vertex ke-{i+1}")
    x = float(input("Koordinat titik x: "))
    y = float(input("Koordinat titik y: "))
    titik.append([x, y])

titik_lama = np.array(titik)
print("\nTitik yang kamu inputkan:\n", titik_lama)

print("=============Translasi=========")
tx = float(input("Translasi X (tx): "))
ty = float(input("Translasi Y (ty): "))
translasi = np.array([tx,ty])
titik_translasi = translasi + titik_lama
print("Hasil translasi:\n", titik_translasi, "\n")

print("============Rotasi==============")
sudut = float(input("Sudut rotasi (derajat): "))
cx = float(input("Titik pusat x: "))
cy = float(input("Titik pusat y: "))

pusat = np.array([cx,cy])

theta = np.radians(sudut)
rotasi = np.array([[np.cos(theta), -np.sin(theta)],
                   [np.sin(theta), np.cos(theta)]])

titik_rotasi = (titik_lama - pusat) @  rotasi.T + pusat
print("Hasil rotasi: ", titik_rotasi, "\n")

print("============Scaling==============")
sx = float(input("Scaling X (sx): "))
sy = float(input("Scaling Y (sy): "))

scaling = np.array([sx,sy])
titik_scaling = titik_lama * scaling
print("Hasil scaling:\n", titik_scaling, "\n")


# Grafik
plt.fill(titik_lama[:,0], titik_lama[:,1], fill=False, edgecolor="teal", linewidth=3, label="Poligon Awal")
plt.fill(titik_translasi[:,0], titik_translasi[:,1], fill=False, edgecolor="blue", linewidth=2, linestyle="--", label="Hasil Translasi")
plt.fill(titik_rotasi[:,0], titik_rotasi[:,1], fill=False, edgecolor="red", linewidth=2, linestyle="--", label="Hasil Rotasi")
plt.fill(titik_scaling[:,0], titik_scaling[:,1], fill=False, edgecolor="orange", linewidth=2, linestyle="--", label="Hasil Scaling")

plt.scatter(titik_lama[:,0], titik_lama[:,1], color="teal")
plt.scatter(titik_translasi[:,0], titik_translasi[:,1], color="blue")
plt.scatter(titik_rotasi[:,0], titik_rotasi[:,1], color="red")
plt.scatter(titik_scaling[:,0], titik_scaling[:,1], color="orange")
plt.scatter(pusat[0], pusat[1], color="purple", label="Titik Pusat Rotasi")

plt.title("Simulator Transformasi 2D")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.axis("equal")
plt.grid()
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()
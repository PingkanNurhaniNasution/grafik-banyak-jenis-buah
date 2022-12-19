import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# grafik banyak buah

subjects = [ 'mangga', 'apel', 'pisang', 'anggur', 'kiwi']
y = [17, 6, 11, 8, 5]
x = [50, 40, 30, 20, 10]

plt.plot(subjects, y,color = "green", marker='o', label='buah')
plt.title("grafik banyak jenis buah")
plt.xlabel("jenis buah")
plt.ylabel("Jumlah banyak buah")
plt.grid()
plt.show()
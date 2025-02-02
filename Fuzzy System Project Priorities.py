import numpy as np
import matplotlib.pyplot as plt

# Muhammad Fitran Ramadhan 1103220156
# Muhammad Wira Al Fikri 1103223104
# Kelas TK-46-05

def fuzzifikasi_anggaran(x):
    rendah = max(0, min((30 - x) / 20, 1))
    sedang = max(0, min((x - 10) / 20, (90 - x) / 20, 1))
    tinggi = max(0, min((x - 70) / 20, 1))
    return {'rendah': rendah, 'sedang': sedang, 'tinggi': tinggi}

def fuzzifikasi_durasi(x):
    pendek = max(0, min((90 - x) / 60, 1))
    sedang = max(0, min((x - 30) / 60, (360 - x) / 90, 1))
    panjang = max(0, min((x - 270) / 90, 1))
    return {'pendek': pendek, 'sedang': sedang, 'panjang': panjang}

def fuzzifikasi_pengaruh(x):
    kecil = max(0, min((60 - x) / 40, 1))
    besar = max(0, min((x - 20) / 40, 1))
    return {'kecil': kecil, 'besar': besar}

def rule_inferensi(anggaran, durasi, pengaruh):
    rules = [
        ('rendah', 'panjang', 'kecil', 'rendah'),
        ('rendah', 'panjang', 'besar', 'rendah'),
        ('rendah', 'sedang', 'kecil', 'rendah'),
        ('rendah', 'sedang', 'besar', 'sedang'),
        ('rendah', 'pendek', 'kecil', 'sedang'),
        ('rendah', 'pendek', 'besar', 'sedang'),
        ('sedang', 'panjang', 'kecil', 'rendah'),
        ('sedang', 'panjang', 'besar', 'sedang'),
        ('sedang', 'sedang', 'kecil', 'sedang'),
        ('sedang', 'sedang', 'besar', 'sedang'),
        ('sedang', 'pendek', 'kecil', 'sedang'),
        ('sedang', 'pendek', 'besar', 'tinggi'),
        ('tinggi', 'panjang', 'kecil', 'sedang'),
        ('tinggi', 'panjang', 'besar', 'sedang'),
        ('tinggi', 'sedang', 'kecil', 'sedang'),
        ('tinggi', 'sedang', 'besar', 'tinggi'),
        ('tinggi', 'pendek', 'kecil', 'tinggi'),
        ('tinggi', 'pendek', 'besar', 'tinggi'),
    ]

    output = {'rendah': 0, 'sedang': 0, 'tinggi': 0}

    for rule in rules:
        a, b, c, z = rule
        if anggaran[a] and durasi[b] and pengaruh[c]:
            strength = min(anggaran[a], durasi[b], pengaruh[c])
            output[z] = max(output[z], strength)

    return output


def tampilkan_grafik_arsir(output):
    z_values = np.linspace(0, 100, 101)
    rendah = np.maximum(0, np.minimum(1, (40 - z_values) / 20))
    sedang = np.maximum(0, np.minimum((z_values - 20) / 20, np.minimum(1, (80 - z_values) / 20)))
    tinggi = np.maximum(0, np.minimum((z_values - 60) / 20, 1))

    aggregated = (
        np.fmax(np.fmin(output['rendah'], rendah),
        np.fmax(np.fmin(output['sedang'], sedang), np.fmin(output['tinggi'], tinggi)))
    )

    plt.figure(figsize=(10, 6))
    plt.plot(z_values, rendah, 'b', linestyle='--', label='Rendah')
    plt.plot(z_values, sedang, 'g', linestyle='--', label='Sedang')
    plt.plot(z_values, tinggi, 'r', linestyle='--', label='Tinggi')
    plt.fill_between(z_values, 0, aggregated, color='gray', alpha=0.5, label='Aggregated')
    plt.title('Fuzzy Output Aggregation')
    plt.xlabel('Prioritas Proyek')
    plt.ylabel('Derajat Keanggotaan')
    plt.legend()
    plt.grid()
    plt.show()

def defuzzifikasi(output):
    # Definisi domain untuk prioritas (0-100)
    z_values = np.linspace(0, 100, 101)
    rendah = np.maximum(0, np.minimum(1, (40 - z_values) / 20))
    sedang = np.maximum(0, np.minimum((z_values - 20) / 20, np.minimum(1, (80 - z_values) / 20)))
    tinggi = np.maximum(0, np.minimum((z_values - 60) / 20, 1))

    aggregated = (
        np.fmax(np.fmin(output['rendah'], rendah),
        np.fmax(np.fmin(output['sedang'], sedang), np.fmin(output['tinggi'], tinggi)))
    )

    numerator = np.sum(aggregated * z_values)
    denominator = np.sum(aggregated)

    return numerator / denominator if denominator != 0 else 0

# Input
anggaran_input = 95
durasi_input = 45
pengaruh_input = 80

# Output
anggaran = fuzzifikasi_anggaran(anggaran_input)
print("Nilai fuzzy anggaran: ", anggaran)
durasi = fuzzifikasi_durasi(durasi_input)
print("Nilai fuzzy durasi: ", durasi)
pengaruh = fuzzifikasi_pengaruh(pengaruh_input)
print("Nilai fuzzy pengaruh terhadap bisnis: ", pengaruh)

inferensi_output = rule_inferensi(anggaran, durasi, pengaruh)
print("\nInferensi output (nilai fuzzy prioritas proyek): ", inferensi_output)
tampilkan_grafik_arsir(inferensi_output)

hasil_prioritas = defuzzifikasi(inferensi_output)
print("\nNilai prioritas proyek:", hasil_prioritas)

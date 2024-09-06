# Pengecek Password Bcrypt / Bcrypt Password Checker

## Deskripsi / Description

Skrip Python ini dirancang untuk memeriksa kecocokan password dengan hash bcrypt menggunakan daftar password dan hash yang disimpan dalam file teks. Skrip ini menggunakan multithreading untuk meningkatkan efisiensi pencarian, dan output hasil akan disimpan dalam file output.

This Python script is designed to check password matches with bcrypt hashes using a list of passwords and hashes stored in text files. The script uses multithreading to improve search efficiency, and the results are saved in an output file.

## Fitur / Features

- **Multithreading**: Menggunakan `ThreadPoolExecutor` untuk memproses hash secara bersamaan, mempercepat proses pencocokan.
- **Warna Terminal**: Menggunakan `colorama` untuk menampilkan status dan hasil dengan warna yang berbeda di terminal.
- **File Input/Output**: Membaca hash dan password dari file, dan menyimpan hasil ke file output.

- **Multithreading**: Utilizes `ThreadPoolExecutor` to process hashes concurrently, speeding up the matching process.
- **Terminal Colors**: Uses `colorama` to display status and results with different colors in the terminal.
- **File Input/Output**: Reads hashes and passwords from files, and writes results to an output file.

## Persyaratan / Requirements

- Python 3.x
- Modul Python:
  - `bcrypt`
  - `colorama`
  - `numpy` (jika menggunakan fitur numpy) / `numpy` (if using numpy features)

Anda dapat menginstal modul yang diperlukan menggunakan pip:

You can install the required modules using pip:

```bash
pip install bcrypt colorama numpy

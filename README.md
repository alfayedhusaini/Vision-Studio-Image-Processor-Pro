# 📸 VISION STUDIO - Sistem Pemroses Efek Citra Real-Time Digital

Vision Studio adalah aplikasi berbasis web interaktif yang dirancang untuk memproses, memanipulasi, dan memberikan berbagai efek visual pada citra (gambar) digital secara real-time. Aplikasi ini dibangun menggunakan framework **Flask (Python)** di bagian backend dan memanfaatkan **CSS Filter / HTML5 Canvas** di bagian frontend untuk memberikan pengalaman pengguna yang cepat dan responsif.

Aplikasi ini memiliki dua fitur utama:
1. **Pengolahan Gambar File (Upload):** Pengguna dapat mengunggah file gambar dari penyimpanan lokal, melihat preview secara real-time, memilih efek, dan mengunduh hasilnya langsung.
2. **Pengolahan Kamera Instan (Webcam):** Pengguna dapat menangkap gambar langsung dari webcam, menerapkan filter visual secara langsung pada layar, mengambil potret, dan menyimpannya.

---

## 🚀 Fitur Efek Citra Pengolahan Digital
Aplikasi ini menyediakan 10 jenis operasi pemrosesan citra yang dapat dipilih melalui menu drop-down bahasa Indonesia:
* **Normal:** Menampilkan citra asli tanpa manipulasi pixel.
* **Abu-abu (Grayscale):** Mengubah representasi warna RGB menjadi skala intensitas abu-abu (Luminance).
* **Buram (Blur):** Menerapkan algoritma Gaussian Blur untuk menghaluskan detail citra.
* **Cerah (Brightness):** Meningkatkan nilai intensitas komponen pencahayaan pada setiap piksel.
* **Batas Ambang (Threshold):** Segmentasi citra biner murni (hanya pixel hitam dan putih tegas berdasarkan batasan nilai ambang 128).
* **Negatif (Invert):** Membalikkan nilai warna asli citra (operasi citra negatif).
* **Sepia:** Transformasi matriks warna untuk memberikan efek nostalgia kecokelatan klasik (vintage).
* **Kontras Tinggi:** Meningkatkan perbedaan gradasi warna antara area gelap dan terang.
* **Deteksi Tepi (Edge Detection):** Menggunakan filter kernel tingkat tinggi untuk mendeteksi dan menampilkan garis kontur/tepi objek.
* **Pertajam (Sharpen):** Memperjelas dan mempertegas detail transisi warna pada objek yang buram.

---

## 🛠️ Prasyarat Sistem
Sebelum menjalankan aplikasi, pastikan perangkat Anda memenuhi spesifikasi berikut:
* **Python Versi:** `3.10.0` (Sangat direkomendasikan agar versi library sinkron)
* **Kamera/Webcam:** Aktif dan telah diberikan izin akses oleh peramban web (browser).
* **Browser:** Google Chrome, Microsoft Edge, Mozilla Firefox, atau Safari versi terbaru.

---

## 💻 Panduan Instalasi dan Menjalankan Aplikasi di Lokal (Localhost)

Ikuti langkah demi langkah di bawah ini untuk memasang dan menjalankan aplikasi di komputer Anda:

### 1. Unduh Source Code
Download project ini dalam bentuk berkas ZIP lalu ekstrak, atau gunakan perintah Git Clone jika Anda menggunakan Git:
```bash
git clone <url-repository-github-anda>
cd vision-studio
# Technical Training Batch 59 - Odoo Modules

Proyek ini berisi dua modul Odoo yang dikembangkan sebagai bagian dari pelatihan teknis:

## 📚 Daftar Modul

### 1. **ahramadhanimodul** - Manajemen Kursus dan Sesi Pelatihan

Modul lengkap untuk mengelola kursus dan sesi pelatihan dengan fitur-fitur komprehensif.

#### Fitur Utama:
- **Manajemen Kursus**: Membuat dan mengelola kursus dengan deskripsi dan pengguna yang bertanggung jawab
- **Manajemen Sesi**: Mengatur sesi pelatihan dengan tanggal mulai, durasi, dan jumlah kursi
- **Tracking Peserta**: Mencatat peserta yang hadir dalam setiap sesi
- **Instruktur**: Mengelola instruktur dengan tingkat keahlian
- **Status Sesi**: Melacak status sesi (Draft → Progress → Done) dengan tracking otomatis
- **Portal**: Interface khusus untuk peserta dan instruktur
- **Laporan Sesi**: Generate laporan untuk setiap sesi pelatihan
- **Wizard Peserta**: Tool untuk menambahkan peserta secara massal
- **Sequencing**: Otomasi pembuatan kode sesi dan penomoran
- **Scheduled Tasks**: Menggunakan ir.cron untuk tugas-tugas terjadwal

#### Model Data:
- `ahramadhanimodul.course` - Model untuk kursus
- `ahramadhanimodul.session` - Model untuk sesi pelatihan
- `ahramadhanimodul.teacher_level` - Level keahlian instruktur
- Extended `res.partner` - Perluasan kontak untuk instruktur

#### Komponen:
```
controllers/        - Controller untuk UI dan API
data/              - Data sequence dan cron jobs
demo/              - Data demonstrasi
models/            - Model ODM (Odoo Data Model)
report/            - Template laporan
security/          - Aturan akses dan keamanan
views/             - View XML untuk UI
wizard/            - Tool wizard untuk operasi tertentu
```

---

### 2. **ramadhaniperpuslib** - Sistem Manajemen Perpustakaan

Modul untuk mengelola inventaris buku dan transaksi peminjaman di perpustakaan.

#### Fitur Utama:
- **Manajemen Buku**: Mencatat judul buku, stok total, dan deskripsi
- **Tracking Stok**: Menampilkan jumlah buku yang tersedia secara real-time berdasarkan peminjaman aktif
- **Transaksi Peminjaman**: Mencatat setiap peminjaman dan pengembalian buku
- **Status Transaksi**: Melacak status peminjaman (Draft → Progress → Done)
- **Tanggal Peminjaman**: Mencatat tanggal pinjam dan tanggal kembali otomatis
- **Anggota Perpustakaan**: Menghubungkan dengan kontak untuk pencatatan peminjam
- **Validasi Stok**: Mencegah peminjaman buku yang tidak tersedia
- **Auto Sequence**: Nomor transaksi otomatis dengan sequence number

#### Model Data:
- `ramadhaniperpuslib.buku` - Model untuk data buku
- `ramadhaniperpuslib.transaksi` - Model untuk transaksi peminjaman

#### Komponen:
```
controllers/        - Controller untuk operasi
data/              - Data sequence
demo/              - Data demonstrasi
models/            - Model ODM
security/          - Aturan akses
views/             - View XML untuk UI
```

---

## 🚀 Instalasi

1. Copy kedua folder modul ke direktori addons Odoo Anda:
   ```bash
   cp -r ahramadhanimodul /path/to/odoo/addons/
   cp -r ramadhaniperpuslib /path/to/odoo/addons/
   ```

2. Update list modul di Odoo:
   - Buka Odoo dan masuk sebagai administrator
   - Ke menu `Apps` → `Update Apps List`

3. Install modul:
   - Cari `ahramadhanimodul` dan `ramadhaniperpuslib`
   - Klik `Install` pada masing-masing modul

## 📋 Persyaratan

- **Odoo Version**: 15.0+
- **Dependencies**:
  - Base (core Odoo)
  - Contacts (`contacts`)
  - Mail (`mail`)
  - Website (`website`)

## 💡 Penggunaan

### Untuk ahramadhanimodul:
1. Buat kursus baru dari menu Kursus
2. Tambahkan sesi untuk kursus tersebut
3. Tentukan instruktur dan jumlah kursi
4. Tambahkan peserta melalui wizard atau langsung
5. Kelola status sesi melalui workflow

### Untuk ramadhaniperpuslib:
1. Daftar buku baru dengan stok total
2. Catat transaksi peminjaman
3. Ubah status menjadi "Progress" saat buku dipinjam
4. Ubah menjadi "Done" saat buku dikembalikan
5. Pantau stok tersedia secara real-time

## 👤 Author

Dikembangkan sebagai bagian dari **Technical Training Batch 59**

## 📄 Lisensi

Modul-modul ini dikembangkan untuk keperluan pelatihan teknis.

# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech - Prediksi Status Akademik Mahasiswa

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan yang berfokus pada pemanfaatan teknologi (Edutech) untuk meningkatkan kualitas pembelajaran dan layanan kepada mahasiswanya. Seperti banyak institusi pendidikan lainnya, Jaya Jaya Institut menghadapi tantangan dalam memantau progres akademik mahasiswa secara individual dan mengidentifikasi secara dini mahasiswa yang berpotensi mengalami kesulitan, `dropout`, atau sebaliknya, yang memiliki potensi besar untuk lulus dengan baik. Pemahaman mendalam terhadap faktor-faktor yang memengaruhi perjalanan akademik mahasiswa sangat penting untuk merancang strategi intervensi yang efektif, meningkatkan angka kelulusan, dan mengoptimalkan alokasi sumber daya pendukung.

### Permasalahan Bisnis

Permasalahan utama yang dihadapi oleh Jaya Jaya Institut adalah:

1.  **Identifikasi Dini Mahasiswa Berisiko:** Kesulitan dalam mengidentifikasi mahasiswa yang berisiko `Dropout` secara proaktif, sehingga intervensi yang diberikan mungkin terlambat atau kurang tepat sasaran.
2.  **Optimalisasi Tingkat Kelulusan:** Keinginan untuk meningkatkan persentase mahasiswa yang berhasil menyelesaikan studi tepat waktu (status `Graduate`) dan memahami faktor-faktor pendorong keberhasilan tersebut.
3.  **Alokasi Sumber Daya yang Efisien:** Kebutuhan untuk mengalokasikan sumber daya pendukung (seperti konseling akademik, bantuan finansial, program pendampingan) secara lebih efektif kepada mahasiswa yang benar-benar membutuhkan.
4.  **Pengambilan Keputusan Berbasis Data:** Meningkatkan penggunaan analisis data dalam pengambilan keputusan strategis terkait layanan dan kebijakan kemahasiswaan.

Proyek ini bertujuan untuk membangun sebuah sistem prediktif yang dapat membantu Jaya Jaya Institut mengklasifikasikan status akademik masa depan mahasiswa (Dropout, Enrolled, Graduate) berdasarkan data historis mereka.

### Cakupan Proyek

Cakupan proyek ini meliputi tahapan-tahapan berikut:

1. Pemahaman Data (Data Understanding)
2. Persiapan Data (Data Preparation)
3. Pemodelan (Modeling) untuk memprediksi status akademik mahasiswa (Dropout, Enrolled, Graduate)
4. Evaluasi (Evaluation)
5. Interpretasi Model
6. Deployment
7. Pembuatan business dashboard
8. Implementasi aplikasi web interaktif untuk penggunaan model

### Persiapan

**Sumber data:**
Dataset yang digunakan adalah

- [Students Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

**Setup environment:**
Proyek ini dikembangkan menggunakan Python. Untuk menjalankan notebook dan kode terkait, Anda memerlukan environment dengan library-library berikut. Pertama-tama clone repository dengan cara:

```
git clone https://github.com/<username>/solving-educational-institution-problems.git
cd solving-educational-institution-problems
```

Anda dapat membuat environment menggunakan `conda` atau `venv` dan menginstal paket-paket yang dibutuhkan dari file `requirements.txt`.
Untuk menginstal dari file `requirements.txt`, jalankan perintah berikut di terminal Anda:

```
pip install -r requirements.txt
```

Atau jika menggunakan Conda:

```bash
conda create --name <nama-projek> python=3.9 # atau versi python lain yang sesuai
conda activate <nama-projek>
pip install -r requirements.txt
```

Untuk menjalankan aplikasi pakai:

```
streamlit run app.py
```

## Business Dashboard

Dashboard ini menyajikan ringkasan data mahasiswa, mencakup statistik deskriptif, pola distribusi nilai, serta faktor-faktor yang memengaruhi potensi dropout. Tujuan utama dashboard ini adalah membantu para pengambil keputusan untuk mengenali pola dan tren yang muncul dalam data tersebut.

Tampilan dashboard:
![Gambaran Dashboard](Dashboard_Analisa_Siswa_Jaya_Jaya_Institut.png)

> **Note**  
> Link ke dashboard: [Dashboard Analisa Murid Jaya Jaya Institut](https://public.tableau.com/app/profile/felicia.pangestu7204/viz/JayaJayaInstitut_17486987118240/DashboardAnalisaSiswaJayaJayaInstitut?publish=yes)

Berikut adalah beberapa insight yang dapat ditarik dari dashboard "Dashboard Analisa Siswa Jaya Jaya Institut":

1.  **Status Pernikahan dan Implikasinya terhadap Studi:**

    - Status pernikahan menunjukkan potensi hubungan dengan status akhir pendidikan mahasiswa. Individu yang berstatus menikah, bercerai, atau terpisah secara hukum memiliki kecenderungan tingkat _dropout_ yang lebih tinggi dibandingkan dengan mereka yang masih lajang.
    - Sebaliknya, mahasiswa yang berstatus "Single" (lajang) lebih dominan dalam kategori "Graduate". Hal ini mengindikasikan bahwa status lajang mungkin berkorelasi dengan konsistensi dan fokus yang lebih tinggi dalam menyelesaikan studi.
    - _Observasi Tambahan:_ Proporsi _dropout_ pada kategori "Married" tampak paling signifikan, bahkan mungkin melebihi proporsi "Graduate" pada kategori status pernikahan tersebut.

2.  **Distribusi Umum Status Mahasiswa:**

    - Secara keseluruhan, sekitar 49.93% dari populasi mahasiswa berhasil mencapai status "Graduate".
    - Meskipun demikian, angka "Dropout" juga cukup substansial, yaitu sekitar 32.19%, yang menunjukkan adanya area signifikan untuk perbaikan dalam hal retensi mahasiswa.
    - Sekitar 17.88% mahasiswa lainnya masih aktif dalam status "Enrolled".
    - _Potensi Tindakan:_ Menganalisis lebih dalam penyebab utama dari sepertiga mahasiswa yang mengalami _dropout_ harus menjadi prioritas utama institusi.

3.  **Peran Gender dalam Hasil Akademik:**

    - Terdapat indikasi perbedaan performa akademik antara mahasiswa perempuan dan laki-laki. Mahasiswi (Perempuan) cenderung menunjukkan proporsi "Graduate" yang relatif lebih tinggi dibandingkan dengan proporsi "Dropout" mereka.
    - Pada mahasiswa (Laki-Laki), proporsi "Dropout" tampak lebih signifikan dan mungkin sebanding atau bahkan sedikit lebih tinggi dari proporsi "Graduate" mereka.
    - _Potensi Tindakan:_ Investigasi lebih lanjut mengenai faktor-faktor spesifik yang mungkin memengaruhi perbedaan ini diperlukan. Perlu dipertimbangkan apakah program dukungan yang disesuaikan berdasarkan gender dapat memberikan hasil yang lebih baik.

4.  **Dampak Signifikan Program Beasiswa terhadap Keberhasilan Studi:**

    - Mahasiswa yang merupakan penerima beasiswa ("Scholarship holder: Yes") menunjukkan tingkat kelulusan ("Graduate") yang sangat dominan dan tingkat "Dropout" yang sangat rendah.
    - Sebaliknya, mahasiswa yang tidak menerima beasiswa memiliki proporsi "Dropout" yang jauh lebih tinggi dan proporsi "Graduate" yang secara persentase lebih rendah.
    - _Potensi Tindakan:_ Hal ini mengonfirmasi efektivitas program beasiswa, tidak hanya dalam aspek finansial tetapi juga kemungkinan dalam memotivasi atau sebagai indikator seleksi mahasiswa dengan potensi keberhasilan tinggi. Perluasan program beasiswa atau bentuk bantuan finansial lainnya bisa menjadi strategi efektif untuk menekan angka _dropout_.

5.  **Korelasi Usia Saat Pendaftaran dengan Keberhasilan Studi:**

    - Usia saat pendaftaran (`Age at enrollment`) menunjukkan korelasi yang jelas dengan status akhir akademik. Kelompok usia termuda (terlihat paling jelas pada rentang 17-20 tahun di dashboard) memiliki proporsi "Graduate" tertinggi.
    - Seiring bertambahnya usia pendaftaran (terutama pada kelompok usia 26 tahun ke atas, dan sangat signifikan pada kelompok usia di atas 35 tahun), proporsi "Dropout" cenderung meningkat secara signifikan, sementara proporsi "Graduate" menurun.
    - _Potensi Tindakan:_ Mahasiswa yang mendaftar pada usia yang lebih matang mungkin menghadapi tantangan unik (misalnya, komitmen kerja, tanggung jawab keluarga) dan karenanya memerlukan sistem dukungan yang lebih fleksibel, program studi yang disesuaikan, atau layanan konseling yang spesifik.

6.  **Konfirmasi Faktor Kunci dari Model Prediktif (Berdasarkan "Top 5 Faktor Kunci"):**
    - Visualisasi "Top 5 Faktor Kunci Status Akademik Mahasiswa" pada dashboard mengonfirmasi temuan dari model prediktif yang telah dibangun. Faktor-faktor seperti `Tuition fees up to date` (status pembayaran SPP), `Curricular units 1st sem (approved)` (jumlah SKS lulus semester 1), `Curricular units 2nd sem (approved)` (jumlah SKS lulus semester 2), `Age at enrollment` (usia saat pendaftaran), dan `Scholarship holder` (penerima beasiswa) adalah penentu atau indikator paling kuat terhadap status akademik mahasiswa.
    - _Potensi Tindakan:_ Menguatkan fokus pada intervensi yang berkaitan dengan kelancaran pembayaran SPP (bantuan finansial, skema cicilan), memastikan keberhasilan akademik di semester-semester awal (program pendampingan, tutorial), memberikan perhatian khusus pada mahasiswa dewasa, dan terus mengevaluasi serta meningkatkan efektivitas program beasiswa.

## Menjalankan Sistem Machine Learning

Sistem machine learning yang dikembangkan terdiri dari dua bagian utama:

1.  **Notebook Jupyter (`notebook.ipynb`):** Berisi seluruh alur kerja analisis data, pra-pemrosesan, pelatihan model, evaluasi, hingga penyimpanan model terbaik.
2.  **Aplikasi Prediksi Sederhana (`app.py`):** Sebuah aplikasi Streamlit untuk melakukan prediksi status akademik mahasiswa menggunakan model yang telah disimpan.

**Cara Menjalankan:**

**1. Menjalankan Notebook Analisis dan Pelatihan Model:**
a. Pastikan Anda telah menyiapkan environment Python seperti yang dijelaskan di bagian "Persiapan".
b. Pastikan file `data.csv` berada di direktori yang sama dengan `notebook.ipynb`.
c. Buka dan jalankan seluruh sel dalam `notebook.ipynb` menggunakan Jupyter Notebook atau Jupyter Lab.
d. Proses ini akan menghasilkan beberapa file output di direktori kerja Anda, termasuk model terbaik yang disimpan (misalnya `best_model.pkl`), preprocessor (`preprocessor.pkl`), pemetaan target (`target_mapping.pkl`), daftar fitur numerik (`numerical_features.pkl`), daftar fitur kategorikal (`categorical_features.pkl`), dan nama kolom target (`target_column_name.pkl`).

**2. Menjalankan Aplikasi Prediksi Streamlit:**
a. Setelah menjalankan notebook dan semua file (`best_model.pkl`, `preprocessor.pkl`, dll.) berhasil disimpan di direktori yang sama.
b. Jalankan aplikasi Streamlit dari terminal Anda:
`      streamlit run app.py
     `
c. Aplikasi akan terbuka di browser Anda, memungkinkan Anda memasukkan data mahasiswa baru (sesuai fitur yang digunakan model) dan mendapatkan prediksi status akademiknya.

_(Jika Anda mendeploy aplikasi Streamlit atau prototipe lainnya secara online, sertakan linknya di sini)._
Contoh:
`Prototipe aplikasi Streamlit dapat diakses di: [Link ke Aplikasi Streamlit Anda]`

> **Note**  
> Link Aplikasi prediksi: [Prediksi status siswa](https://preditctstudentdropout.streamlit.app/)

## Conclusion

Proyek data science ini telah berhasil mengembangkan sebuah model machine learning, yaitu Random Forest Classifier, yang mampu memprediksi status akademik mahasiswa di Jaya Jaya Institut. Model ini mencapai tingkat akurasi sebesar 76.38% dan F1-Score sebesar 0.7493 pada data uji.

Analisis faktor penting dari model, yang juga terkonfirmasi secara visual melalui dashboard "Analisa Siswa Jaya Jaya Institut", menunjukkan bahwa beberapa faktor kunci yang paling signifikan memengaruhi status kelulusan atau _dropout_ mahasiswa meliputi:

- `Curricular units 2nd sem (approved)` (Jumlah SKS Lulus Semester 2)
- `Curricular units 2nd sem (grade)` (Jumlah SKS Lulus Semester 2)
- `Curricular units 1st sem (approved)` (Jumlah SKS Lulus Semester 1)
- `Curricular units 1st sem (grade)` (Jumlah SKS Lulus Semester 1)
- `Admission grade` (Nilai Saat Pendaftaran)
- `Age at enrollment` (Usia Saat Pendaftaran)
- `Tuition fees up to date` (Status Pembayaran Uang Kuliah)

Selain itu, analisis dashboard juga memberikan _insight_ tambahan mengenai tren pada kelompok mahasiswa berdasarkan:

- **Status Pernikahan:** Mahasiswa lajang cenderung memiliki tingkat kelulusan lebih tinggi, sedangkan yang menikah, bercerai, atau berpisah menunjukkan risiko _dropout_ lebih tinggi.
- **Gender:** Terdapat indikasi perbedaan tingkat kelulusan dan _dropout_ antara mahasiswa laki-laki dan perempuan, di mana mahasiswi cenderung memiliki rasio kelulusan yang lebih baik.
- **Status Beasiswa:** Penerima beasiswa secara signifikan menunjukkan performa akademik yang lebih baik dan risiko _dropout_ yang jauh lebih rendah.
- **Usia Saat Pendaftaran:** Mahasiswa yang mendaftar pada usia lebih muda (17-20 tahun) memiliki tingkat kelulusan tertinggi, dengan risiko _dropout_ yang meningkat seiring bertambahnya usia pendaftaran.

### Rekomendasi Action Items

Berdasarkan kesimpulan dan _insight_ yang diperoleh, berikut adalah beberapa rekomendasi _action items_ yang dapat diimplementasikan oleh Jaya Jaya Institut:

1.  **Pengembangan dan Implementasi Sistem Peringatan Dini (Early Warning System - EWS):**

    - Manfaatkan model prediktif yang telah dibangun sebagai inti dari EWS untuk mengidentifikasi mahasiswa berisiko _dropout_ sejak dini.
    - Integrasikan EWS dengan dashboard pemantauan yang dapat diakses oleh dosen wali, konselor, dan manajemen akademik untuk tindak lanjut yang cepat.

2.  **Penguatan Program Dukungan Akademik di Semester Awal:**

    - Mengingat `Curricular units 1st sem (approved)` dan `Curricular units 2nd sem (approved)` adalah faktor kunci, sediakan program pendampingan akademik (mentoring, tutoring) yang intensif bagi mahasiswa baru, terutama yang menunjukkan kesulitan awal.
    - Kaji ulang kurikulum atau metode pengajaran pada mata kuliah semester awal yang mungkin memiliki tingkat kegagalan tinggi.

3.  **Optimalisasi Program Bantuan Finansial dan Beasiswa:**

    - Perkuat dan perluas program beasiswa (`Scholarship holder` terbukti sangat efektif) dan pastikan prosesnya transparan serta menjangkau mahasiswa yang berhak dan berpotensi.
    - Kembangkan skema bantuan pembayaran SPP yang lebih fleksibel atau program bantuan finansial darurat bagi mahasiswa yang teridentifikasi mengalami kesulitan pembayaran (`Tuition fees up to date` sebagai faktor penting).

4.  **Penyediaan Dukungan Khusus Berdasarkan Profil Mahasiswa:**
    - **Dukungan berbasis Usia:** Rancang program dukungan atau jalur studi yang lebih fleksibel untuk mahasiswa yang mendaftar pada usia lebih dewasa (`Age at enrollment`), mempertimbangkan potensi komitmen kerja atau keluarga mereka.
    - **Dukungan berbasis Status Pernikahan:** Sediakan layanan konseling atau dukungan yang mempertimbangkan tantangan spesifik mahasiswa yang sudah menikah, bercerai, atau berpisah, mengingat tren _dropout_ yang lebih tinggi pada kelompok ini.
    - **Dukungan berbasis Gender:** Lakukan analisis lebih lanjut mengenai perbedaan tren antara gender. Jika terbukti signifikan, pertimbangkan program mentoring atau kelompok dukungan yang mungkin lebih sesuai untuk masing-masing gender.
5.  **Peningkatan Keterlibatan dan Kesejahteraan Mahasiswa:**

    - Selenggarakan program orientasi yang komprehensif untuk membantu mahasiswa baru beradaptasi dengan kehidupan kampus, baik secara akademik maupun sosial.
    - Tingkatkan layanan konseling (psikologis, karir, akademik) dan sosialisasikan ketersediaannya secara luas.

6.  **Pengambilan Keputusan Berbasis Data Secara Berkelanjutan:**

    - Jadikan dashboard analisa siswa sebagai alat monitoring rutin bagi manajemen untuk melacak tren dan efektivitas intervensi.
    - Secara periodik (misalnya, setiap tahun ajaran), lakukan evaluasi dan _retraining_ model prediktif dengan data terbaru untuk menjaga akurasinya. Kumpulkan juga data kualitatif untuk melengkapi temuan kuantitatif.

## Author

Felicia Pangestu [Linkedin](https://www.linkedin.com/in/felicia-pangestu-764905226/)

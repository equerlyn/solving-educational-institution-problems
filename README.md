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
3. Pemodelan (Modeling) untuk memprediksi kemungkinan mahasiswa mengalami dropout
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
Dashboard potensial dapat memvisualisasikan:
* Distribusi status mahasiswa (Dropout, Enrolled, Graduate) secara keseluruhan dan per program studi/angkatan.
* Tren angka dropout/kelulusan dari waktu ke waktu.
* Profil mahasiswa berdasarkan faktor risiko yang teridentifikasi oleh model.
* Efektivitas program intervensi (jika data tersedia).

*(Jika Anda mengembangkan dashboard terpisah, jelaskan di sini dan sertakan linknya).*
Insight:
1. Status pernikahan memiliki potensi hubungan terhadap status pendidikan. Individu yang menikah, bercerai, atau terpisah hukum cenderung memiliki tingkat dropout lebih tinggi dibandingkan yang masih lajang. Sebaliknya, individu yang masih berstatus “Single” lebih banyak ditemukan dalam kategori “Graduate”, yang dapat menunjukkan bahwa status lajang mendukung konsistensi dan keberhasilan dalam menyelesaikan pendidikan.


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
      ```
      streamlit run app.py
      ```
   c. Aplikasi akan terbuka di browser Anda, memungkinkan Anda memasukkan data mahasiswa baru (sesuai fitur yang digunakan model) dan mendapatkan prediksi status akademiknya.

*(Jika Anda mendeploy aplikasi Streamlit atau prototipe lainnya secara online, sertakan linknya di sini).*
Contoh:
`Prototipe aplikasi Streamlit dapat diakses (jika dideploy) di: [Link ke Aplikasi Streamlit Anda]`
`Saat ini, aplikasi hanya dapat dijalankan secara lokal.`

## Conclusion
Proyek data science ini telah berhasil mengembangkan model machine learning, yaitu **[ISI DENGAN NAMA MODEL TERBAIK DARI OUTPUT NOTEBOOK ANDA, contoh: Random Forest Classifier]**, yang fungsional untuk memprediksi status akademik mahasiswa di Jaya Jaya Institut. Model ini mencapai tingkat akurasi sebesar **[ISI DENGAN NILAI AKURASI AKTUAL DARI OUTPUT NOTEBOOK ANDA, contoh: 78.5%]** dan F1-Score (weighted) sebesar **[ISI DENGAN NILAI F1-SCORE AKTUAL DARI OUTPUT NOTEBOOK ANDA, contoh: 0.78]** pada data uji.

Analisis lebih lanjut terhadap model terbaik juga berhasil mengidentifikasi beberapa faktor kunci yang signifikan memengaruhi status kelulusan atau dropout mahasiswa. Fitur-fitur (variabel) paling berpengaruh yang teridentifikasi oleh model antara lain:
* **[ISI DENGAN FITUR PENTING 1 DARI OUTPUT NOTEBOOK ANDA, contoh: Curricular units 2nd sem (grade)]**
* **[ISI DENGAN FITUR PENTING 2 DARI OUTPUT NOTEBOOK ANDA, contoh: Tuition fees up to date]**
* **[ISI DENGAN FITUR PENTING 3 DARI OUTPUT NOTEBOOK ANDA, contoh: Curricular units 1st sem (approved)]**
* **[ISI DENGAN FITUR PENTING 4 DARI OUTPUT NOTEBOOK ANDA, contoh: Age at enrollment]**
* **[ISI DENGAN FITUR PENTING 5 DARI OUTPUT NOTEBOOK ANDA, contoh: Scholarship holder]**
    *(Sesuaikan daftar ini dengan 5-7 fitur teratas dari plot feature importance di notebook Anda).*

Model prediktif yang dikembangkan dalam proyek ini memberikan Jaya Jaya Institut alat yang berharga untuk secara proaktif mengidentifikasi mahasiswa yang berisiko `Dropout` atau memerlukan dukungan tambahan. Wawasan dari fitur-fitur penting dapat menginformasikan desain intervensi yang lebih terarah dan efektif, membantu institut mencapai target peningkatan retensi dan kelulusan mahasiswa.

### Rekomendasi Action Items
Berdasarkan hasil analisis dan model yang dibangun, berikut adalah beberapa rekomendasi action items yang dapat diikuti oleh Jaya Jaya Institut untuk menyelesaikan permasalahan dan mencapai target mereka:

1.  **Implementasi Sistem Peringatan Dini (SPD) Berbasis Model:**
    * **AI-1:** Bentuk tim implementasi lintas fungsi (Akademik, IT, Kemahasiswaan/Konseling) untuk merancang dan menguji coba prototipe sistem peringatan dini berdasarkan model prediktif yang telah dikembangkan. (Target: Q3 tahun berjalan).
    * **AI-2:** Integrasikan output model (daftar mahasiswa berisiko `Dropout` beserta skor risiko dan faktor utamanya) ke dalam dashboard atau alat bantu yang mudah diakses oleh tim konseling dan dosen wali. (Target: Mulai semester depan).

2.  **Fokus Intervensi pada Faktor Kunci yang Teridentifikasi:**
    * **AI-3:** Berdasarkan fitur-fitur paling berpengaruh seperti **[SEBUTKAN 1-2 FITUR KUNCI AKTUAL DARI HASIL ANDA, contoh: nilai semester awal dan status pembayaran SPP]**, selenggarakan pelatihan bagi dosen wali dan staf akademik mengenai strategi identifikasi dini dan pendekatan dukungan yang sesuai. (Target: Dalam 2 bulan ke depan).
    * **AI-4:** Kaji ulang dan sesuaikan kebijakan terkait dukungan finansial, beasiswa, atau fleksibilitas pembayaran SPP jika fitur seperti `Tuition fees up to date` terbukti sangat signifikan dalam memprediksi risiko `Dropout`. (Target: Dalam 3 bulan ke depan).

3.  **Pengembangan Program Intervensi yang Ditargetkan:**
    * **AI-5:** Luncurkan program pendampingan (mentoring) akademik atau program tutorial tambahan yang ditargetkan bagi mahasiswa baru atau mahasiswa semester awal yang teridentifikasi memiliki skor prediksi risiko `Dropout` tertinggi oleh model. (Target: Mulai penerimaan mahasiswa baru/semester berikutnya).
    * **AI-6:** Kembangkan modul intervensi spesifik (misalnya, manajemen waktu, strategi belajar efektif, konseling stres, bantuan penulisan akademik) yang dapat diakses oleh mahasiswa yang teridentifikasi berisiko.

4.  **Pemanfaatan Data untuk Peningkatan Kurikulum dan Proses Pembelajaran:**
    * **AI-7:** Jika fitur terkait unit kurikuler atau nilai mata kuliah tertentu sangat dominan sebagai prediktor kegagalan (misalnya, **[SEBUTKAN FITUR KURIKULER SPESIFIK JIKA ADA DARI HASIL ANDA]**), lakukan evaluasi mendalam terhadap kurikulum, metode pengajaran, beban studi, atau sistem penilaian pada mata kuliah/area tersebut.

5.  **Pengembangan dan Pemeliharaan Model Secara Berkelanjutan:**
    * **AI-8:** Jadwalkan evaluasi dan pelatihan ulang (retraining) model prediktif secara periodik (misalnya, setiap akhir tahun ajaran atau setiap semester) dengan menggunakan data terbaru untuk memastikan akurasi dan relevansinya terhadap dinamika populasi mahasiswa.
    * **AI-9:** Pertimbangkan untuk melakukan eksplorasi pengumpulan data tambahan yang relevan (misalnya, data aktivitas di Learning Management System (LMS), data kehadiran yang lebih detail, hasil survei keterlibatan mahasiswa, frekuensi konsultasi dengan dosen) untuk potensi peningkatan akurasi model di masa mendatang.
    * **AI-10:** Budayakan pengambilan keputusan berbasis data di semua tingkatan yang terkait dengan kemahasiswaan dan akademik, dengan memanfaatkan wawasan dari model ini dan analisis data lainnya.

*(Pastikan untuk menyesuaikan rekomendasi action items ini dengan temuan spesifik dari proyek Anda, terutama fitur-fitur yang paling berpengaruh dan metrik performa model yang aktual).*

import streamlit as st
import pandas as pd
import joblib
import numpy as np

marital_status_options = {
    "Single": 1, "Married": 2, "Widower": 3, "Divorced": 4, "Facto Union": 5, "Legally Separated": 6
}
application_mode_options = {
    "1st phase - general contingent": 1, "Ordinance No. 612/93": 2,
    "1st phase - special contingent (Azores Island)": 5, "Holders of other higher courses": 7,
    "Ordinance No. 854-B/99": 10, "International student (bachelor)": 15,
    "1st phase - special contingent (Madeira Island)": 16, "2nd phase - general contingent": 17,
    "3rd phase - general contingent": 18, "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
    "Ordinance No. 533-A/99, item b3 (Other Institution)": 27, "Over 23 years old": 39,
    "Transfer": 42, "Change of course": 43, "Technological specialization diploma holders": 44,
    "Change of institution/course": 51, "Short cycle diploma holders": 53,
    "Change of institution/course (International)": 57
}
course_options = {
    "Biofuel Production Technologies": 33, "Animation and Multimedia Design": 171,
    "Social Service (evening attendance)": 8014, "Agronomy": 9003,
    "Communication Design": 9070, "Veterinary Nursing": 9085,
    "Informatics Engineering": 9119, "Equinculture": 9130, "Management": 9147,
    "Social Service": 9238, "Tourism": 9254, "Nursing": 9500, "Oral Hygiene": 9556,
    "Advertising and Marketing Management": 9670, "Journalism and Communication": 9773,
    "Basic Education": 9853, "Management (evening attendance)": 9991
}
daytime_evening_options = {"Daytime": 1, "Evening": 0} # Nama fitur di error: Daytime_evening_attendance
previous_qualification_options = {
    "Secondary education": 1, "Higher education - bachelor's degree": 2, "Higher education - degree": 3,
    "Higher education - master's": 4, "Higher education - doctorate": 5, "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9, "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12, "10th year of schooling": 14,
    "10th year of schooling - not completed": 15, "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
    "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38, "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40, "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}
nationality_options = { # Contoh beberapa, LENGKAPI! (Fitur di error: Nacionality)
    "Portuguese": 1, "German": 2, "Spanish": 6, "Italian": 11, "Brazilian": 41,
}
mother_father_qualification_options = { # Fitur di error: Mothers_qualification, Fathers_qualification
    "Secondary Education - 12th Year or Eq.": 1, "Higher Education - Bachelor's": 2,
    "Higher Education - Degree": 3, "Higher Education - Master's": 4, "Higher Education - Doctorate": 5,
    "Unknown": 34, "Can't read or write": 35,
}
occupation_options = { # Fitur di error: Mothers_occupation, Fathers_occupation
    "Student": 0, "Specialists in Intellectual and Scientific Activities": 2,
    "Administrative staff": 4, "Unskilled Workers": 9, "Other Situation": 90, "(blank)": 99,
    "Teachers": 123,
}
yes_no_options = {"Yes": 1, "No": 0}
gender_options = {"Male": 1, "Female": 0} # Fitur di error: Gender

# --- LOAD SAVED ARTIFACTS ---
try:
    model = joblib.load('model/best_model.pkl')
    preprocessor = joblib.load('model/preprocessor.pkl')
    target_mapping = joblib.load('model/target_mapping.pkl')
    target_mapping_inv = {v: k for k, v in target_mapping.items()}
    numerical_features = joblib.load('model/numerical_features.pkl')
    categorical_features = joblib.load('model/categorical_features.pkl')
    print("Model, preprocessor, and feature lists loaded successfully for Streamlit app.")
except FileNotFoundError as e:
    st.error(f"Error: Missing artifact file - {e.filename}. Pastikan semua file .pkl ada di direktori yang sama dengan app.py.")
    print(f"Error: Missing artifact file - {e.filename}.")
    st.stop()
except Exception as e:
    st.error(f"Terjadi error saat memuat artefak: {e}")
    print(f"Terjadi error saat memuat artefak: {e}")
    st.stop()

st.set_page_config(page_title="Prediksi Status Akademik Mahasiswa - Jaya Jaya Institut", layout="wide")
st.title("🎓 Prediksi Status Akademik Mahasiswa")
st.markdown("""
Aplikasi ini memprediksi status akademik mahasiswa (Graduate, Dropout, atau Enrolled)
berdasarkan data yang dimasukkan. Harap isi semua field di samping kiri dengan benar.
""")

input_data = {}
all_expected_features = numerical_features + categorical_features

with st.sidebar.form(key='student_input_form'):
    st.header("Input Data Mahasiswa")

    # Menggunakan nama fitur dari pesan error sebagai kunci untuk input_data
    # Kategori 1: Informasi Pribadi & Aplikasi
    st.subheader("Informasi Pribadi & Aplikasi")
    if 'Marital_status' in all_expected_features: # Sesuai error: Marital_status
        input_data['Marital_status'] = st.selectbox("Status Perkawinan", options=list(marital_status_options.keys()))
    if 'Application_mode' in all_expected_features: # Sesuai error: Application_mode
        input_data['Application_mode'] = st.selectbox("Mode Aplikasi", options=list(application_mode_options.keys()))
    if 'Application_order' in all_expected_features: # Sesuai error: Application_order
        input_data['Application_order'] = st.number_input("Urutan Aplikasi Pilihan", min_value=0, max_value=9, value=1, step=1)
    if 'Course' in all_expected_features:
        input_data['Course'] = st.selectbox("Program Studi", options=list(course_options.keys()))
    if 'Daytime_evening_attendance' in all_expected_features: # Sesuai error
        input_data['Daytime_evening_attendance'] = st.selectbox("Waktu Kuliah (Siang/Malam)", options=list(daytime_evening_options.keys()))
    if 'Nacionality' in all_expected_features: # Sesuai error (Nacionality, bukan Nationality)
        input_data['Nacionality'] = st.selectbox("Kewarganegaraan", options=list(nationality_options.keys())) # LENGKAPI DICTIONARYNYA
    if 'Gender' in all_expected_features: # Sesuai error
        input_data['Gender'] = st.selectbox("Jenis Kelamin", options=list(gender_options.keys()))
    if 'Age_at_enrollment' in all_expected_features: # Sesuai error
        input_data['Age_at_enrollment'] = st.number_input("Usia saat Pendaftaran (Tahun)", min_value=15, max_value=99, value=20, step=1)
    if 'International' in all_expected_features:
        input_data['International'] = st.selectbox("Mahasiswa Internasional?", options=list(yes_no_options.keys()))

    # Kategori 2: Latar Belakang Pendidikan & Keluarga
    st.subheader("Latar Belakang Pendidikan & Keluarga")
    if 'Previous_qualification' in all_expected_features: # Sesuai error
        input_data['Previous_qualification'] = st.selectbox("Kualifikasi Sebelumnya", options=list(previous_qualification_options.keys())) # LENGKAPI DICTIONARY
    if 'Previous_qualification_grade' in all_expected_features: # Sesuai error
        input_data['Previous_qualification_grade'] = st.number_input("Nilai Kualifikasi Sebelumnya (0-200)", min_value=0.0, max_value=200.0, value=150.0, step=0.1)
    if "Mothers_qualification" in all_expected_features: # Sesuai error
        input_data["Mothers_qualification"] = st.selectbox("Kualifikasi Ibu", options=list(mother_father_qualification_options.keys())) # LENGKAPI DICTIONARY
    if "Fathers_qualification" in all_expected_features: # Sesuai error
        input_data["Fathers_qualification"] = st.selectbox("Kualifikasi Ayah", options=list(mother_father_qualification_options.keys())) # LENGKAPI DICTIONARY
    if "Mothers_occupation" in all_expected_features: # Sesuai error
        input_data["Mothers_occupation"] = st.selectbox("Pekerjaan Ibu", options=list(occupation_options.keys())) # LENGKAPI DICTIONARY
    if "Fathers_occupation" in all_expected_features: # Sesuai error
        input_data["Fathers_occupation"] = st.selectbox("Pekerjaan Ayah", options=list(occupation_options.keys())) # LENGKAPI DICTIONARY

    # Kategori 3: Status Akademik & Finansial
    st.subheader("Status Akademik & Finansial")
    if 'Admission_grade' in all_expected_features: # Sesuai error
        input_data['Admission_grade'] = st.number_input("Nilai Seleksi Masuk (0-200)", min_value=0.0, max_value=200.0, value=150.0, step=0.1)
    if 'Displaced' in all_expected_features:
        input_data['Displaced'] = st.selectbox("Mahasiswa Pindahan/Transisi?", options=list(yes_no_options.keys()))
    if 'Educational_special_needs' in all_expected_features: # Sesuai error
        input_data['Educational_special_needs'] = st.selectbox("Kebutuhan Pendidikan Khusus?", options=list(yes_no_options.keys()))
    if 'Debtor' in all_expected_features:
        input_data['Debtor'] = st.selectbox("Memiliki Tunggakan Pembayaran?", options=list(yes_no_options.keys()))
    if 'Tuition_fees_up_to_date' in all_expected_features: # Sesuai error
        input_data['Tuition_fees_up_to_date'] = st.selectbox("Biaya Kuliah Lunas Tepat Waktu?", options=list(yes_no_options.keys()))
    if 'Scholarship_holder' in all_expected_features: # Sesuai error
        input_data['Scholarship_holder'] = st.selectbox("Penerima Beasiswa?", options=list(yes_no_options.keys()))

    # Kategori 4: Unit Kurikuler Semester 1
    st.subheader("Unit Kurikuler Semester 1")
    # Nama fitur dari error: Curricular_units_1st_sem_credited, dll.
    sem1_cols_map = {
        'Curricular_units_1st_sem_credited': "SKS Diakui Sem 1",
        'Curricular_units_1st_sem_enrolled': "SKS Diambil Sem 1",
        'Curricular_units_1st_sem_evaluations': "SKS Dievaluasi Sem 1",
        'Curricular_units_1st_sem_approved': "SKS Lulus Sem 1",
        'Curricular_units_1st_sem_grade': "Rata-rata Nilai Sem 1 (0-20)",
        'Curricular_units_1st_sem_without_evaluations': "SKS Tanpa Evaluasi Sem 1"
    }
    for col_name_actual, user_label in sem1_cols_map.items():
        if col_name_actual in all_expected_features:
            if "grade" in col_name_actual:
                input_data[col_name_actual] = st.number_input(user_label, min_value=0.0, max_value=20.0, value=10.0, step=0.1)
            else:
                input_data[col_name_actual] = st.number_input(user_label, min_value=0, value=0, step=1)

    # Kategori 5: Unit Kurikuler Semester 2
    st.subheader("Unit Kurikuler Semester 2")
    sem2_cols_map = {
        'Curricular_units_2nd_sem_credited': "SKS Diakui Sem 2",
        'Curricular_units_2nd_sem_enrolled': "SKS Diambil Sem 2",
        'Curricular_units_2nd_sem_evaluations': "SKS Dievaluasi Sem 2",
        'Curricular_units_2nd_sem_approved': "SKS Lulus Sem 2",
        'Curricular_units_2nd_sem_grade': "Rata-rata Nilai Sem 2 (0-20)",
        'Curricular_units_2nd_sem_without_evaluations': "SKS Tanpa Evaluasi Sem 2"
    }
    for col_name_actual, user_label in sem2_cols_map.items():
        if col_name_actual in all_expected_features:
            if "grade" in col_name_actual:
                input_data[col_name_actual] = st.number_input(user_label, min_value=0.0, max_value=20.0, value=10.0, step=0.1)
            else:
                input_data[col_name_actual] = st.number_input(user_label, min_value=0, value=0, step=1)

    # Kategori 6: Indikator Ekonomi Makro
    macro_cols_map = {
        'Unemployment_rate': "Tingkat Pengangguran (%)",
        'Inflation_rate': "Tingkat Inflasi (%)",
        'GDP': "GDP"
    }
    has_macro = any(col in all_expected_features for col in macro_cols_map.keys())
    if has_macro:
        st.subheader("Indikator Ekonomi Makro")
        for col_name_actual, user_label in macro_cols_map.items():
            if col_name_actual in all_expected_features:
                 input_data[col_name_actual] = st.number_input(user_label, value=0.0, step=0.01 if col_name_actual == 'GDP' else 0.1)


    # Input untuk fitur yang murni kategorikal (jika ada dan bertipe object di training)
    if categorical_features:
        st.subheader("Data Kategorikal Lain (Teks)")
        for feature in categorical_features: # feature akan memiliki nama kolom yang benar dari .pkl
            input_data[feature] = st.text_input(f"{feature.replace('_', ' ').title()}",
                                                help=f"Masukkan nilai kategori teks untuk {feature}")

    submit_button = st.form_submit_button(label='🔮 Prediksi Status')

if submit_button:
    data_to_process = {}
    for key_from_form, value_from_form in input_data.items():
        # key_from_form sekarang SEHARUSNYA sudah merupakan nama kolom yang benar (e.g., 'Marital_status')
        # Mapping nilai dari selectbox ke kode numerik ASLI
        if key_from_form == 'Marital_status':
            data_to_process[key_from_form] = marital_status_options.get(value_from_form)
        elif key_from_form == 'Application_mode':
            data_to_process[key_from_form] = application_mode_options.get(value_from_form)
        elif key_from_form == 'Course':
            data_to_process[key_from_form] = course_options.get(value_from_form)
        elif key_from_form == 'Daytime_evening_attendance':
            data_to_process[key_from_form] = daytime_evening_options.get(value_from_form)
        elif key_from_form == 'Previous_qualification':
            data_to_process[key_from_form] = previous_qualification_options.get(value_from_form)
        elif key_from_form == 'Nacionality':
            data_to_process[key_from_form] = nationality_options.get(value_from_form)
        elif key_from_form == "Mothers_qualification":
            data_to_process[key_from_form] = mother_father_qualification_options.get(value_from_form)
        elif key_from_form == "Fathers_qualification":
            data_to_process[key_from_form] = mother_father_qualification_options.get(value_from_form)
        elif key_from_form == "Mothers_occupation":
            data_to_process[key_from_form] = occupation_options.get(value_from_form)
        elif key_from_form == "Fathers_occupation":
            data_to_process[key_from_form] = occupation_options.get(value_from_form)
        elif key_from_form == 'Gender':
            data_to_process[key_from_form] = gender_options.get(value_from_form)
        elif key_from_form in ['Displaced', 'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date', 'Scholarship_holder', 'International']:
            data_to_process[key_from_form] = yes_no_options.get(value_from_form)
        else: # Untuk fitur numerik atau yang sudah berupa kode dari number_input
            data_to_process[key_from_form] = value_from_form

    # Validasi apakah semua fitur yang diharapkan ada di data_to_process
    missing_features = []
    for feature_name in all_expected_features:
        if feature_name not in data_to_process:
            missing_features.append(feature_name)
            # Sediakan nilai default yang aman jika fitur tidak ada (misalnya 0 untuk numerik, atau mode untuk kategori)
            # Ini adalah fallback, idealnya semua fitur terisi dari form.
            # if feature_name in numerical_features:
            #     data_to_process[feature_name] = 0 # Atau np.nan jika imputer akan menangani
            # else: # Untuk categorical_features yang mungkin tidak ter-OHE jika tidak ada di form
            #     data_to_process[feature_name] = "Missing" # Atau mode dari training data

    if missing_features:
        st.error(f"Fitur berikut tidak ditemukan dalam input yang diproses: {', '.join(missing_features)}. Harap periksa form input dan mapping.")
        # Hentikan eksekusi jika ada fitur yang hilang, karena akan menyebabkan error di preprocessor
        st.stop()


    try:
        input_df = pd.DataFrame([data_to_process], columns=all_expected_features)

        for col in numerical_features:
            if col in input_df.columns:
                input_df[col] = pd.to_numeric(input_df[col], errors='coerce')
        for col in categorical_features:
            if col in input_df.columns:
                input_df[col] = input_df[col].astype(object)

        if input_df.isnull().values.any():
            st.error("Ada nilai yang hilang atau tidak valid dalam data input setelah diproses. Mohon periksa kembali semua input.")
            # st.write("Data Input (setelah mapping & sebelum preprocessing):")
            # st.dataframe(input_df)
            # st.write("Kolom dengan NaN:")
            # st.write(input_df.columns[input_df.isnull().any()].tolist())
        else:
            input_processed = preprocessor.transform(input_df)
            prediction_encoded = model.predict(input_processed)
            prediction_proba = model.predict_proba(input_processed)
            final_prediction_label = target_mapping_inv[prediction_encoded[0]]

            st.subheader("📈 Hasil Prediksi:")
            if final_prediction_label == "Dropout":
                st.error(f"Prediksi Status Akademik Mahasiswa: **{final_prediction_label}**")
                st.warning("Mahasiswa ini berpotensi **Dropout**. Perlu perhatian dan intervensi khusus.")
            elif final_prediction_label == "Enrolled":
                st.info(f"Prediksi Status Akademik Mahasiswa: **{final_prediction_label}**")
                st.info("Mahasiswa ini diprediksi akan tetap **Terdaftar (Enrolled)**. Pantau progresnya.")
            elif final_prediction_label == "Graduate":
                st.success(f"Prediksi Status Akademik Mahasiswa: **{final_prediction_label}** 🎉")
                st.success("Mahasiswa ini diprediksi akan **Lulus (Graduate)**!")
            else:
                st.write(f"Prediksi Status Akademik Mahasiswa: **{final_prediction_label}**")

            st.subheader("Probabilitas Prediksi per Kelas:")
            proba_class_labels = [target_mapping_inv[i] for i in model.classes_]
            proba_df = pd.DataFrame(prediction_proba, columns=proba_class_labels)
            st.dataframe(proba_df.style.format("{:.2%}"))

    except Exception as e:
        st.error(f"Terjadi error selama proses prediksi: {e}")
        st.error("Pastikan semua input telah diisi dengan benar dan sesuai format yang diharapkan.")

st.markdown("---")
st.markdown("© 2025 Felicia Pangestu · Jaya Jaya Institut. All rights reserved.")
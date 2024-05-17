# Extract, Transform, Load (ETL) Pipeline And Visualization

## About Project
Melakukan proses ETL kepada data Social-Economic Countries yang merupakan kumpulan data dari tahun 1960 hingga saat ini yang mencakup informasi ekonomi dan sosial dari berbagai negara di seluruh dunia. 

## Tech Stacks
Daftar tools dan framework yang digunakan dalam project ini:
- Python
- Library python (pandas etc)
- Vscode
- Github
- Jupyter Notebook
- Firebase
- MySQL
- API World Bank
- XML
- JSON 
- CSV
- DB
- others

## Architecture Diagram
 ![ETL Diagram](https://github.com/ddzikri/mini-project/blob/main/ETL_DIAGRAM.png?raw=true)

## Setup 
### Langkah 1: Persiapan Lingkungan
Pastikan Anda telah menginstal Tools dan Library yang diperlukan:
- Install python dan library sesuai kebutuhan.
- Config Jupyter Notebook.
- Config Firebase Admin.

### Langkah 2: Ekstraksi Data
1. Unduh file data dari [Link Berikut](https://github.com/yudhaislamisulistya/mini-project-de-alta).
2. Kumpulkan data berupa csv, xml, api, db, xml dll dalam satu folder.
3. Buka Jupyter Notebook.
4. Import Library python yang diperlukan.
5. Buat code Python menggunakan pandas, agar dataset yang di extract menjadi dataframe.

### Langkah 3: Transformasi Data
1. Cleaning Data
    - Mengatasi Missing Values
    - Menghapus Duplikasi Data
    - Replace and Regex

2. Penyesuaian Tipe data
3. Drop Kolom yang tidak Diperlukan
4. Imputasi pada gdp_data menggunakan teknik simpleimputer
5. Menghapus Outliers
6. Scaling fitur
7. Buat dummy variabel jika ada dalam dataset
8. Feature Engineering
9. Menggabungkan dataset agar menjadi dataset final.

### Langkah 4: Load Data
1. Google Firebase Admin  
    - Buat Script python untuk menyimpan data final kedalam firebase admin ketika muatan data sangat besar.
2. WorkbenchMySQl
    - Buat Script python untuk menyimpan data final kedalam database workbenchMySQl (local file) ketika muatan data kecil.


### Langkah 5: Visualisasi Data
1. Buat script prompt Implementasi AI untuk analisis visualisasi data (optional).
2. Menggunakan Matplotlib, Seaborn dan plotly express agar tampilan visualisasi menarik.

### Langkah 6: Apache Airflow WSL Ubuntu 
1. Install Apache airflow di WSL ubuntu. 
2. Buat Folder Dags dan masukan file yang diperlukan.
3. Jalankan Airflow with command 'airflow standalone'
4. Liat hasilnya dags di localhost:8080.

### Kata-kata Terakhir
Proyek ini hadir ketika kesepian datang dan rasa penyesalan larut didalam kesepian itu sendiri. terimakasih buat mentor dan teman-teman yang selalu support proyek ini!!.

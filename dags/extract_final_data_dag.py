import pandas as pd
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.utils.dates import days_ago

# Define function to load data from CSV
def load_population_data():
    # Path to your local CSV file (replace with your actual path)
    csv_path = "/home/dzikri/airflow/dags/data_final.csv"

    # Read data from CSV file
    population_df = pd.read_csv(csv_path)

    # Print some information about the loaded data
    print("Data loaded from:", csv_path)
    print("Number of records:", len(population_df))

# Define default arguments for the DAG
default_args = {
    'owner': 'dzikri',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define DAG parameters
dag = DAG(
    'load_final_data',
    default_args=default_args,
    description='A DAG to load final data from local CSV',
    schedule_interval='@daily',  # Run daily
)

# Define task to load data from CSV
load_data_task = PythonOperator(
    task_id='load_final_data',
    python_callable=load_population_data,  # Corrected function name
    dag=dag,
)

# Set task dependencies (no dependencies in this case)
load_data_task
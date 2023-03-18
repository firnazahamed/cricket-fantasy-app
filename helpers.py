import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from google.cloud import storage
from io import BytesIO

# Create API client.
def get_client():
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"]
    )
    client = storage.Client(credentials=credentials)

    return client


@st.cache_data(ttl=600)
def read_file(bucket_name, file_path, format="csv", sheet_name=None):
    client = get_client()
    bucket = client.bucket(bucket_name)
    content = bucket.blob(file_path).download_as_bytes()
    if format == "csv":
        df = pd.read_csv(BytesIO(content))
    elif format == "excel":
        df = pd.read_excel(BytesIO(content), sheet_name=sheet_name)

    return df

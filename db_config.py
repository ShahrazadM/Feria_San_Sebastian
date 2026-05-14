# db_config.py
import os
from supabase import create_client
import streamlit as st

# Cargar desde .env manualmente
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Leer variables de entorno
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Depuración - mostrar si encuentra las variables
if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("No se encontraron las credenciales de Supabase")
    st.write(f"SUPABASE_URL: {'Encontrado' if SUPABASE_URL else 'No encontrado'}")
    st.write(f"SUPABASE_KEY: {'Encontrado' if SUPABASE_KEY else 'No encontrado'}")
    st.write(f"Directorio actual: {os.getcwd()}")
    
    # Verificar si existe el archivo .env
    env_path = os.path.join(os.getcwd(), '.env')
    if os.path.exists(env_path):
        st.success(f"Archivo .env encontrado en: {env_path}")
    else:
        st.error(f"No se encontró el archivo .env en: {env_path}")
    
    st.info("Como crear el archivo .env: 1. Abre el Bloc de notas 2. Escribe: SUPABASE_URL=https://tu-proyecto.supabase.co y SUPABASE_KEY=sb_publishable_tu_clave 3. Guarda como .env en la carpeta del proyecto")
    st.stop()

# Cliente de Supabase
@st.cache_resource
def get_supabase():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def get_connection():
    return get_supabase()
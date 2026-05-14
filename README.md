# 🛒 Frutería San Sebastián

Sistema de ventas para ferias de barrio. Funciona offline, con control de stock y múltiples usuarios.
se usa stremlit para simular como fucnionarian en appshet ya que apshet gratuito no permite conecion a postgre.

## 🔑 Credenciales de Acceso

### 👑 Feriante (Dueño)
| Campo | Valor |
|-------|-------|
| Contraseña | `feriante2026` |
| Email | `prueba@ejemplo.com` |

**Permisos:** Inventario completo, reportes, gestión de ayudantes

### 👥 Ayudantes
| Nombre | Contraseña |
|--------|------------|
| Pedro | `pedro2026` |
| María | `maria2026` |
| José | `jose2026` |

**Permisos:** Solo registrar ventas

## 🛠️ Tecnologías

- **Frontend:** Streamlit
- **Backend:** Supabase (PostgreSQL)
- **Lenguaje:** Python 3.13
  Aquí tienes una versión **corta y sencilla** para tu README:

---

## 🚀 **Despliegue en Streamlit Cloud**

### 📋 **Requisitos previos (entorno local)**

Antes de desplegar, asegúrate de tener estos archivos:

| Archivo | ¿Subir a GitHub? |
|---------|------------------|
| `app.py` | ✅ Sí |
| `requirements.txt` | ✅ Sí |
| `db_config.py` | ✅ Sí |
| `.env` | ❌ **NO** (contiene credenciales) |

### ✅ **Verificación local**

```bash
pip install -r requirements.txt
streamlit run app.py
```

> La app debe funcionar en `localhost` antes de continuar.

### ☁️ **Despliegue en la nube**

1. **Sube a GitHub** solo `app.py`, `requirements.txt` y `db_config.py` (el `.env` NO se sube)

2. **Ve a [share.streamlit.io](https://share.streamlit.io)** y conecta tu repositorio

3. **Configura los Secrets** (Advanced settings → Secrets):

```toml
SUPABASE_URL = "https://tu-proyecto.supabase.co"
SUPABASE_KEY = "sb_publishable_tu_clave"
```

4. **Click en Deploy** 🚀

### ⚠️ **Importante**

- ❌ Nunca subas el archivo `.env` a GitHub
- ✅ Las credenciales van en los Secrets de Streamlit Cloud
- ✅ Prueba localmente antes de desplegar

---

  #:) Para ingresar entrar desde link de la barra de direcciones:
  https://feriasansebastian-prxenyhpywrwh6owpnanjv.streamlit.app/
  

  #feriasansebastian-prxenyhpywrwh6owpnanjv
  

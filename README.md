

## 🔬 **Investigación previa: Funcionamiento en la nube**

El Demo se desarrolló en dos fases:

1. **Neon :** Más ligero, validamos triggers PL/pgSQL y control de stock.Una ves que nos aseguramos que funcionono la conxion y su logica de negocio incluido los trigues  pasamos a Supabase:
2. **Supabase :** Migramos por su facilidad de despliegue (no requiere whitelist IP) y porque no suspende la BD por inactividad (Neon lo hace a los 5 min).
**Conclusión:** Validamos con Neon, elegimos Supabase por robustez y optimo comportamiento en la nube.

---

## 🛒 **Frutería San Sebastián**

Sistema de ventas para ferias de barrio. Funciona offline, con control de stock y múltiples usuarios.

> **Nota:** Usamos Streamlit para simular AppSheet, ya que la versión gratuita de AppSheet no permite conexión a PostgreSQL.
Streamlit es solo para prototipos y demos. En el entorno real de producción  ejemplo con 50 puestos y alta concurrencia, la arquitectura debe ser robusta como la propuesta en el documento (AppSheet + Supabase), donde AppSheet actúa como frontend nativo para dispositivos móviles.

---

## 🔗 **Acceso a la App**

`https://feriasansebastian-prxenyhpywrwh6owpnanjv.streamlit.app/`

---

## 🔑 **Credenciales**

| Rol | Credencial |
|-----|------------|
| **Feriante** | `feriante2026` |
| **Ayudante Pedro** | `pedro2026` |
| **Ayudante María** | `maria2026` |
| **Ayudante José** | `jose2026` |

---

## 🛠️ **Tecnologías**

- **Frontend:** Streamlit
- **Backend:** Supabase (PostgreSQL)
- **Lenguaje:** Python 3.13

---

## 🚀 **Despliegue en Streamlit Cloud**

### Requisitos previos

| Archivo | ¿Subir a GitHub? |
|---------|------------------|
| `app.py` | ✅ Sí |
| `requirements.txt` | ✅ Sí |
| `db_config.py` | ✅ Sí |
| `.env` | ❌ No |

### Verificación local

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Despliegue

1. Sube a GitHub (`app.py`, `requirements.txt`, `db_config.py`)
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Configura Secrets:
```toml
SUPABASE_URL = "https://tu-proyecto.supabase.co"
SUPABASE_KEY = "sb_publishable_tu_clave"
```
4. Deploy 🚀

---

## 📊 **Triggers: Neon vs Supabase**

### ¿Python descuenta stock?

**NO.** Los triggers están en la Base de Datos, no en Python.

```sql
-- Trigger en BD (Neon y Supabase)
CREATE OR REPLACE FUNCTION descontar_stock()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE productos SET stock_kg = stock_kg - NEW.cantidad_kg
    WHERE id = NEW.producto_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

| Pregunta | Respuesta |
|----------|-----------|
| ¿Triggers desde Python? | ❌ No |
| ¿Dónde están? | ✅ En la BD |
| ¿Python solo inserta? | ✅ Sí |
| ¿Trigger descuenta stock? | ✅ Sí |

---

## 📊 **Comparativa Neon vs Supabase**

| Aspecto | Neon | Supabase |
|---------|------|----------|
| **Biblioteca** | `psycopg2-binary` | `supabase` |
| **Conexión** | Cadena PostgreSQL | URL + anon key |
| **Trigger** | ✅ En BD | ✅ En BD |
| **Despliegue** | Requiere whitelist IP | Sin configuración extra |
| **Inactividad** | ⏱️ Suspende a los 5 min | 🔄 Activo siempre |
| **Reactivación** | 🐢 Lenta (2-5 seg) | ⚡ Instantánea |
| **Desactivacion**|💰 Plan pago para desactivar | 💰 Gratuito sin suspensión |

> **Conclusión:** Ambos funcionan igual. La diferencia está en la facilidad de despliegue.



  

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


## ✅ **Respuesta correcta:**

**NO, los triggers NO se usaron desde Python en tu versión de Neon.**

## 📊 **Análisis de tu código Neon:**

```python
# Tu código SOLO inserta datos - NO maneja triggers en Python
def registrar_venta_completa(feriante_email, items_carrito, tipo_pago, total):
    # 1. Insertar venta
    cur.execute("INSERT INTO ventas...")
    
    # 2. Insertar detalles
    cur.execute("INSERT INTO venta_detalles...")
    
    # ❌ NO hay código para descontar stock aquí
    # ✅ El trigger en la BD lo hace automáticamente
```

## 🔄 **Comparativa clara:**

| Aspecto | 🔷 **Neon** | 🔶 **Supabase** |
|---------|-------------|-----------------|
| **Trigger está en** | Base de datos (PostgreSQL) | Base de datos (PostgreSQL) |
| **Código Python** | Solo inserta en tablas | Solo inserta en tablas |
| **¿Python descuenta stock?** | ❌ No | ❌ No |
| **¿Quién descuenta stock?** | ✅ Trigger en BD | ✅ Trigger en BD |
| **Diferencia real** | Conexión con `psycopg2` | Conexión con `supabase-py` |

## 📝 **El trigger (IDÉNTICO en ambos):**

```sql
-- Este trigger vive en la BASE DE DATOS, NO en Python
CREATE OR REPLACE FUNCTION descontar_stock()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE productos SET stock_kg = stock_kg - NEW.cantidad_kg
    WHERE id = NEW.producto_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

## 🎯 **Conclusión:**

| Pregunta | Respuesta |
|----------|-----------|
| ¿Los triggers se usaron desde Python? | ❌ **No** |
| ¿Dónde están los triggers? | ✅ En la **base de datos** (Neon y Supabase) |
| ¿Python solo inserta datos? | ✅ **Sí** |
| ¿El trigger descuenta stock? | ✅ **Sí**, automáticamente |


## 📊 Comparativa Técnica: Neon vs Supabase

| Aspecto | 🔷 Neon | 🔶 Supabase |
|---------|---------|-------------|
| **Biblioteca Python** | `psycopg2-binary` | `supabase` |
| **Cadena de conexión** | `postgresql://user:pass@host/db` | URL + anon key |
| **Trigger** | ✅ En BD (PL/pgSQL) | ✅ En BD (PL/pgSQL) |
| **Descuento de stock** | ✅ Automático (trigger) | ✅ Automático (trigger) |
| **Configuración en Cloud** | Requiere whitelist IP | Sin configuración extra |
| **Dificultad** | Media | Baja |

> **Conclusión:** Ambos funcionan igual. La diferencia está en la facilidad de despliegue.
### 📊 **Comparativa 

| Neon | Supabase |
|------|----------|
| ⏱️ Se suspende a los 5 minutos | 🔄 Permanece activo siempre |
| 🐢 Reactivación lenta (2-5 seg) | ⚡ Respuesta instantánea |
| 💰 Plan pago para desactivar | 💰 Gratuito sin suspensión |


  #:) Para ingresar entrar desde link de la barra de direcciones:
  https://feriasansebastian-prxenyhpywrwh6owpnanjv.streamlit.app/
  

  #feriasansebastian-prxenyhpywrwh6owpnanjv
  

# 🚀 Sprint 2: DevDiary (Seguridad y Usuarios)

¡Tu base de datos está viva! Pero ahora mismo, cualquiera puede entrar y ver los secretos de todo el mundo. En este Sprint, vamos a implementar un sistema de **Autenticación (Login) y Registro**, y asegurarnos de que cada quien solo vea su propio diario.

## ⚠️ PASO CERO: Limpieza de Base de Datos
Como hemos modificado nuestra estructura para incluir un `user_email` y una tabla de `User`, necesitamos reiniciar nuestra base de datos local.
1. Abre tu panel de explorador de archivos a la izquierda.
2. Abre la carpeta `instance`.
3. Haz clic derecho sobre `diary.db` y dale a **Eliminar (Delete)**.
*Tranquilo, tu código de inicialización creará una nueva DB limpia y actualizada cuando corras la app.*

## 📋 Backlog del Sprint (Tus Tareas)

Busca los comentarios `TICKET #...` en tus archivos:

- [ ] **TICKET #1: Crear la tabla de Usuarios (`main.py`)**
  - Configura la clase `User` agregando las columnas necesarias (`id`, `email`, `password`) para que el sistema sepa qué guardar.
- [ ] **TICKET #2: Campos de Inicio de Sesión (`login.html`)**
  - El formulario está incompleto. Observa cómo está hecho el campo de "email" y crea la etiqueta HTML correspondiente para la "password".
- [ ] **TICKET #3: Implementar Registro (`main.py`)**
  - En la ruta `/reg`, usa SQLAlchemy para tomar el email y contraseña enviados por el formulario y guardarlos en la tabla `User`.
- [ ] **TICKET #4: Implementar Login y Seguridad (`main.py`)**
  - Esta es la parte de los verdaderos hackers:
    1. En la ruta `/login`, verifica si el usuario existe en la DB. Si existe, lo guardamos en la `session` (la memoria del navegador).
    2. En `/index`, asegúrate de filtrar las tarjetas (`.filter_by`) para que el usuario logueado solo vea las suyas.
    3. En `/form_create`, asegúrate de enviar el `session['email']` al crear una tarjeta nueva.

¡Éxitos con este nuevo desafío de seguridad Backend! Corre `python main.py` cuando estés listo.
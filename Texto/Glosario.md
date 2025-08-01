# Registro de cambios

Este archivo documenta los cambios importantes que se han hecho en el proyecto.  
Cada entrada indica la fecha, quien hizo el cambio y que se modifico.  

**Instrucciones para logear:**

- Anade un nuevo bloque con la fecha del dia cuando hagas cambios.  
- Describe brevemente que hiciste y quien lo hizo.  
- Usa vinetas para separar cada cambio dentro de la fecha.  
- Manten el formato simple y claro para que cualquiera pueda seguir el historial.

---

## 📘 Glosario de Sintaxis Markdown

Este glosario explica como aplicar formato basico en Markdown para mantener el `changelog.md` claro, ordenado y consistente.

---

### 🔤 Estilos de texto

- **Negrita:**  
  Escribe el texto entre `**dobles asteriscos**`.  
  Ejemplo: `**Importante**` → **Importante**

- *Cursiva:*  
  Escribe el texto entre `*asteriscos simples*`.  
  Ejemplo: `*Nota*` → *Nota*

- ~~Tachado~~:  
  Usa `~~doble virgulilla~~`.  
  Ejemplo: `~~Eliminado~~` → ~~Eliminado~~

---

### 🔠 Encabezados (tamanos de titulo)

Se usan signos `#` para definir titulos:

```markdown
# Titulo nivel 1
## Titulo nivel 2
### Titulo nivel 3
#### Titulo nivel 4
```

Entre mas `#`, mas pequeno el tamano del titulo.  
Usa encabezados para organizar secciones si el archivo crece.

---

### 🔢 Listas

- **Vinetas (sin orden):**  
  Puedes usar `-`, `*` o `+`.  
  Ejemplo:
  ```markdown
  - Cambio 1
  - Cambio 2
  ```

- **Listas numeradas:**  
  Usa numeros seguidos de punto:  
  ```markdown
  1. Primer cambio
  2. Segundo cambio
  ```

---

### 💬 Citas (comentarios o notas)

Usa el simbolo `>` al inicio de la linea:
```markdown
> Este es un comentario para contexto.
```

---

### 💻 Codigo

- **En linea:**  
  Usa una comilla invertida (backtick) \`codigo\`  
  Ejemplo:  
  `Este es un comando: \`npm install\``

- **Bloques de codigo:**  
  Usa tres comillas invertidas antes y despues:
  ````markdown
  \`\`\`
  def ejemplo():
      return True
  \`\`\`
  ````

---

### 🔗 Enlaces

Para poner un link:  
```markdown
[texto del enlace](https://ejemplo.com)
```

Ejemplo:  
[OpenAI](https://openai.com)

---

### 🖼️ Imagenes (poco comun en changelogs)

```markdown
![Texto alternativo](https://ejemplo.com/imagen.png)
```

---

### ✅ Tareas o checklists

Util si quieres hacer seguimiento a cambios pendientes:

```markdown
- [x] Tarea completada
- [ ] Tarea pendiente
```

Resultado:

- [x] Tarea completada  
- [ ] Tarea pendiente

---

Este glosario es solo una guia de formato.  
No hace falta usar todo: enfocate en mantener claro, ordenado y legible el changelog.

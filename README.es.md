# Fable 5.1 — prompt del sistema (proyecto de referencia)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## 📖 Guía de uso

Guía completa (landing + paso a paso): **https://inematds.github.io/fable51-system-prompt/guia/es/**

Material de referencia sobre el **prompt del sistema de Claude Fable 5.1**: qué publica Anthropic, qué aparece en la extracción pública del runtime de Claude.ai, qué cambió respecto a Fable 5 y las fichas prácticas derivadas de ello. Este es el **proyecto**; el **curso** que enseña este contenido está separado (ver al final).

## Dos fuentes, dos niveles de confianza

| Fuente | Qué es | Confianza |
|---|---|---|
| [Prompt central oficial](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1) (Anthropic) | Lo que Anthropic publica y firma, con historial de versiones | Única fuente autenticada |
| Dump del runtime (repositorio [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S/tree/main/ANTHROPIC), carpeta ANTHROPIC) | Runtime ensamblado: prompt central + memoria + búsqueda + artefactos + enrutamiento + esquemas de herramientas. Congelado el 2026-09-02. | Extracción **no autenticada** por Anthropic |
| Field Guide (Mark Kashef, 2026-09-02; traducción PT-BR) | Comparación Fable 5 × 5.1 con el mismo método de conteo | Reproducible; compara dos dumps no autenticados |

Marco para todo en este repositorio: **oficial × extraído** y **modelo × producto que lo rodea**. Fable 5.1 obtiene una puntuación más alta *y* el sistema que lo rodea creció 2,3x; nada demuestra que una cosa haya causado la otra.

## Qué hay aquí

```
fable51-system-prompt/
  README.md               este archivo
  ANALISE.md              los tres números, las 28 herramientas en 6 grupos, reglas de comportamiento, la paradoja
  INDICE-DO-DUMP.md       mapa generado del dump: 40 secciones con líneas y tamaño, herramientas y skills encontradas
  fichas/
    01-ficha-dos-5-testes.md       ficha de registro + las 5 pruebas del comprador (memoria, conversaciones, visuales, skills, control)
    02-escrever-para-o-fable.md    quitar el andamiaje, indicar el cuándo, formato > fórmula, esfuerzo, esqueleto set/2026
    03-custo-e-esforco.md          tabla de precios, niveles de esfuerzo, "ejecuta barato y vuelve a intentarlo", dónde gana lo barato
  build/indice.py         genera el índice a partir del dump
  guia/index.html         landing + guía (GitHub Pages) · capa/capa.png portada del catálogo
  doc/                    material fuente LOCAL (ignorado por git — ver abajo)
```

### `doc/` no se publica

La carpeta `doc/` guarda el dump (`Claude-Fable-5.1.md`, 275.723 bytes, md5 `be4cb3a5103be5c1c581afac2a04b1d0`) y los dos PDF del Field Guide (EN, escrito por Mark Kashef; PT-BR). Son material de terceros / extracción no autenticada; permanecen solo en la máquina, como ya ocurría en el repositorio del curso. El dump original es público en el repositorio CL4R1T4S enlazado arriba. Para regenerar el índice: `python3 build/indice.py` en la raíz.

## Los tres números (resumen)

- Prompt capturado: **17.501 → 40.046 palabras (2,3x)**.
- **+28 herramientas** (46 en total, ninguna eliminada).
- **75% del crecimiento** = memoria + esquemas de herramientas. Solo `memory_filesystem` ocupa el 38% del dump actual.

Detalle en [ANALISE.md](ANALISE.md).

## Cómo usar

1. ¿Quieres saber **qué hay** en el prompt y dónde? [INDICE-DO-DUMP.md](INDICE-DO-DUMP.md) (orden de lectura sugerido al final).
2. ¿Quieres **probar en tu cuenta** si aparecen las novedades? [fichas/01-ficha-dos-5-testes.md](fichas/01-ficha-dos-5-testes.md).
3. ¿Quieres **reescribir tus prompts** para la nueva generación? [fichas/02-escrever-para-o-fable.md](fichas/02-escrever-para-o-fable.md).
4. ¿Quieres **gastar menos**? [fichas/03-custo-e-esforco.md](fichas/03-custo-e-esforco.md).

Todo está fechado: dump del 2026-09-02, análisis del 2026-09-05. El producto cambia; vuelve a auditarlo en cada generación.

## Curso

- **Fable 5.1 en la práctica — qué cambió, cómo usarlo, cómo gastar menos** (3 rutas, 9 módulos): repositorio [`inematds/fable51-system`](https://github.com/inematds/fable51-system) · página https://inematds.github.io/fable51-system/
- Relacionado: **Arquitectura de Intención — Día 4, El Giro** (modelos que operan según la intención): https://inematds.github.io/arquitetura-de-intencao/dia-4.html

---
INEMA.CLUB · 2026

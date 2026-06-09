# 🏓 Como tu quieras — Proyecto: Pong (WIP)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Development Status](https://img.shields.io/badge/Estado-En%20Desarrollo%20%2F%20Incompleto-orange.svg)](#-estado-actual-del-proyecto)
[![GitHub stars](https://img.shields.io/github/stars/Arepan31243/Como-tu-quieras.svg?style=social)](https://github.com/Arepan31243/Como-tu-quieras/stargazers)

Un clon clásico del legendario juego **Pong**. Este proyecto se encuentra actualmente en estado **WIP (Work In Progress)**. Es un desarrollo base funcional pero incompleto, ideal para aprender mecánicas de colisiones, bucles de juego (*game loops*) y físicas básicas bidimensionales.

---

## 📌 Índice

- [🎯 Estado Actual del Proyecto](#-estado-actual-del-proyecto)
- [🛠️ Tecnologías e Implementación](#%EF%B8%8F-tecnologías-e-implementación)
- [⚙️ Instalación y Ejecución](#%EF%B8%8F-instalación-y-ejecución)
- [🎮 Controles Actuales](#-controles-actuales)
- [📋 Roadmap / Tareas Pendientes](#-roadmap--tareas-pendientes)
- [🐛 Bugs Conocidos](#-bugs-conocidos)
- [🤝 Cómo Contribuir o Completarlo](#-cómo-contribuir-o-completarlo)

---

## 🎯 Estado Actual del Proyecto

El juego cuenta con la estructura básica inicializada. A día de hoy, el motor gráfico básico renderiza los componentes en pantalla, pero carece de un sistema completo de condiciones de victoria y de inteligencia artificial.

### Lo que ya funciona (Hecho):
* [x] Creación de la ventana de juego y lienzo (*canvas*) de dibujo.
* [x] Renderizado y movimiento vertical fluido de la pala del Jugador 1 y 2 (Izquierda y derecha).
* [x] Movimiento automatizado lineal de la pelota.
* [x] Sistema básico de colisiones con los bordes superior e inferior de la pantalla.

---

## 🛠️ Tecnologías e Implementación

* **Lenguaje:** [Por ejemplo: Python con Pygame / JavaScript con HTML5 Canvas]
* **Paradigma:** Programación Orientada a Objetos (POO) dividida en entidades (`Pelota`, `Pala`, `Marcador`).
* **Físicas:** Vectores simples para determinar la velocidad e inversión de ejes en colisiones rígidas (`dx`, `dy`).

---

## ⚙️ Instalación y Ejecución

Sigue estos pasos para probar la versión actual en tu máquina local:

### Requisitos Previos
* Tener instalado [Python 3.x / Node.js] según el lenguaje final de tu código.

### Pasos
1. **Clonar este repositorio:**
   ```bash
   git clone [https://github.com/Arepan31243/Como-tu-quieras.git](https://github.com/Arepan31243/Como-tu-quieras.git)
   cd Como-tu-quieras

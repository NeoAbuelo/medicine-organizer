# 📅 API de Administración de Pastillas con Integración a Google Calendar

Esta API en Python permite generar un calendario de administración de medicamentos. Solo necesitas proporcionar los días o semanas de duración del tratamiento, y el intervalo entre dosis (en horas). La API se encarga de calcular los horarios y agregarlos automáticamente a tu Google Calendar.

## 🚀 Características

- Cálculo automático de horarios de dosis según duración e intervalo.
- Integración con Google Calendar para crear eventos por cada toma.
- Compatible con múltiples zonas horarias.

## 📦 Requisitos

- Python 3.12 o superior
- Cuenta de Google con acceso a Google Calendar
- Archivo de credenciales OAuth2 de Google (`credentials.json`)

### Librerías necesarias

```bash
pip install -r requirements.txt

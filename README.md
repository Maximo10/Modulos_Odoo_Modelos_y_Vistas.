# Práctica 4: Módulos Odoo - Modelo y Vista
---
## Objetivo
Aplicar conocimientos sobre modelos, relaciones y vistas en Odoo mediante 4 actividades.

## Actividad 01: Lista de Tareas
- Vista Kanban añadida
- Campo `fecha_vencimiento` añadido
- Vista Calendario implementada

## Actividad 02: Biblioteca de Cómics
- Modelo `Socio` (nombre, apellidos, identificador)
- Modelo `Ejemplar` (comic_id, socio_id, fechas)
- Restricciones: fecha préstamo ≤ hoy, fecha devolución ≥ hoy

## Actividad 03: Gestión Hospitalaria
- Modelo `Paciente` (nombre, apellidos, síntomas)
- Modelo `Medico` (nombre, apellidos, num_colegiado)
- Modelo `Consulta` (paciente_id, medico_id, diagnóstico, fecha)

## Actividad 04: Ciclos Formativos
- Modelos: Ciclo, Módulo, Alumno, Profesor
- Relaciones: One2many, Many2one, Many2many
- Seguridad: Director (CRUD todo) | Profesor (solo lectura profesores)

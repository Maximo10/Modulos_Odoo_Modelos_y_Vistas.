# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos modelo Ciclo Formativo
class Cicloformativos(models.Model):
    #Nombre y descripcion del modelo
    _name='ciclo.formativo'
    _description='Ciclo Formativo'
    _rec_name='nombre'

    #Atributos
    nombre = fields.Char('Nombre', required=True)
    modulo_ids=fields.One2many('modulo', 'ciclo_id', string='Módulos')

#Definimos modelo Módulo
class Modulo(models.Model):
    #Nombre y descripcion del modelo
    _name='modulo'
    _description='Módulo del ciclo formativo'
    _rec_name='nombre'

    #Atributos
    nombre=fields.Char('Nombre del módulo',required=True)
    ciclo_id=fields.Many2one('ciclo.formativo',string='Ciclo formativo', required=True)
    profesor_id=fields.Many2one('ciclo.profesor',string='Profesor que imparte')
    alumno_ids=fields.Many2many('ciclo.alumno',string='Alumnos matriculados')


#Definimos modelo Alumno
class Alumno(models.Model):
    #Nombre y descripcion del modelo
    _name='ciclo.alumno'
    _description='Alumno del instituto'
    _rec_name='nombre'

    #Atributos
    nombre=fields.Char('Nombre',required=True)
    modulo_ids=fields.Many2many('modulo',string='Módulos inscritos')


#Definimos modelo Profesor
class Profesor(models.Model):
    #Nombre y descripcion del modelo
    _name='ciclo.profesor'
    _description='Profesor del instituto'
    _rec_name='nombre'

    #Atributos
    nombre=fields.Char('Nombre', required=True)
    modulo_ids = fields.One2many('modulo', 'profesor_id', string='Módulos que imparte')    
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

#Definimos modelo Paciente
class Paciente(models.Model):
    #Nombre y descripcion del modelo
    _name='hospital.paciente'
    _description='Paciente del hospital'
    # Atributo que se mostrará por defecto como nombre del registro
    _rec_name='nombre'

    #Atributos
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    sintomas = fields.Text('Sintomas')

#Definimos modelo Médico
class Medico(models.Model):
    #Nombre y descripcion del modelo
    _name='hospital.medico'
    _description='Médico del hospital'
    _rec_name='nombre'
    
    #Atributos
    nombre = fields.Char('Nombre',required=True)
    apellidos = fields.Char('Apellidos',required=True)
    # Id único del médico
    numero_colegiado=fields.Char('Número de colegiado',required=True,help='Identificador único del médico')

#Definimos modelo Consulta
class Consulta(models.Model):
    _name='hospital.consulta'
    _description='Consulta entre paciente y médico'
    _rec_name='paciente_id'

    # Relación Many2one con Paciente
    paciente_id = fields.Many2one('hospital.paciente',string='Paciente',required=True)
    # Relación Many2one con Médico 
    medico_id = fields.Many2one('hospital.medico',string='Médico',required=True)
    # Diagnóstico de la consulta
    diagnostico = fields.Text('Diagnóstico')
    # Fecha de la consulta
    fecha_consulta = fields.Date('Fecha de la consulta',default=fields.Date.today)

    # Validación para que la fecha no sea anterior a el dia de consulta
    @api.constrains('fecha_consulta')
    def _check_fecha_consulta(self):
        for record in self:
            if record.fecha_consulta and record.fecha_consulta > fields.Date.today():
                raise ValidationError('La fecha de la consulta no puede ser posterior a hoy.')            
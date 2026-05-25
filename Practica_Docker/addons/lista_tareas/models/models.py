# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class ListaTareas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son
    #https://www.odoo.com/documentation/17.0/developer/reference/addons/orm.html
    #fields
    tarea = fields.Char(string="Tarea")
    prioridad = fields.Integer(string="Prioridad")
    urgente = fields.Boolean(compute='_value_urgente', store=True)
    realizada = fields.Boolean(string="Realizada")
    fecha_vencimiento = fields.Date(string="Fecha de Vencimiento")
    #Este computo depende de la variable prioridad
    @api.depends('prioridad')
    #Funcion para calcular el valor de urgente
    def _value_urgente(self):
        for record in self:
            #Si la prioridad es mayor que 10, se considera urgente, en otro caso no lo es
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False
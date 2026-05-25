# -*- coding: utf-8 -*-
{
    'name': "Gestion Hospitalaria",
    'summary': """Gestion de pacientes, medicos y consultas""",
    'description': """Modulo para la gestion básica de un hospital.""",

    'author': "Birhan Fernández",
    'website': "https://apuntesfpinformatica.es",

    # Indicamos que es una aplicación
    'application': True,

    # Categoría adecuada para este tipo de módulo
    'category': 'Administration',
    'version': '1.0',

    # Dependencias necesarias
    'depends': ['base'],

    # Archivos que se cargan al instalar el módulo
    'data': [
        #Este primero indica la politica de acceso del módulo
        'security/ir.model.access.csv',
        #Cargamos las vistas y las plantillas
        'views/hospital_views.xml',
    ],
    'installable': True,
}

# -*- coding: utf-8 -*-
{
    'name': "ciclos_formativos",
    'summary': "Gestión de ciclos formativos, módulos, alumnos y profesores",
    'description': """Módulo para gestionar los ciclos formativos de un instituto""",

    'author': "Birhan Fernández",
    'website': "https://apuntesfpinformatica.es",

    # Categoría adecuada para este tipo de módulo
    'category': 'Administration',
    'version': '1.0',
    
    # Dependencias necesarias
    'depends': ['base'],

    # Archivos que se cargan al instalar el módulo
    'data': [
        #Este primero indica la politica de acceso del módulo
        'security/groups.xml',
        'security/ir.model.access.csv',
        #Cargamos las vistas y las plantillas
        'views/ciclos_formativos_views.xml',
    ],
    # Indicamos que es una aplicación
    'application': True,
    'installable': True,
}
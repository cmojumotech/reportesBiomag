{
    'name': 'Modulo Reportes y API OAuth',
    'version': '1.0',
    'summary': 'Generación de reportes en Excel y autenticación con API externa vía OAuth',
    'description': 'Módulo para exportar reportes (Ventas, Stock, Stock Picking, Productos y Contactos) en Excel y realizar autenticación OAuth con una API externa.',
    'author': 'Tu Nombre o Empresa',
    'website': 'https://jumotech.com',
    'category': 'Tools',
    'depends': ['base', 'sale', 'stock', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/reports_views.xml',
    ],
    'installable': True,
    'application': True,
}
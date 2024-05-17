{
    'name': 'Student Portal',
    'version': '1.0',
    'summary': 'A portal to display student data',
    'description': 'This module creates a portal to display student data from the student module.',
    'author': 'Tarcin Inc',
    'category': 'website',
    'depends': ['base', 'website', 'student'],
    'data': [
        'views/portal_templates.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}

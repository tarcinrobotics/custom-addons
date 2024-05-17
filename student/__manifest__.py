# student/__manifest__.py
{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Manage Students',
    'description': 'A module to manage student records.',
    'author': 'Tarcin Inc',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
    ],
    'installable': True,
    'application': True,
}

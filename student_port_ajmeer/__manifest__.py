# student/__manifest__.py
{
    'name': 'Student Portal Ajmeer',
    'version': '1.1',
    'summary': 'Ajmeer is working on this Students Portal View inside portal',
    'description': 'A module to manage student records.',
    'author': 'Tarcin Inc',
    'category': 'Portal',
    'depends': ['base', 'portal'],
    'data': [
      #  'security/ir.model.access.csv',
#        'views/student_action_views.xml',
        'views/student_views.xml',
        'views/student_ajmeer.xml',
#        'views/student_education.xml',
    ],
    'installable': True,
    'application': True,
}

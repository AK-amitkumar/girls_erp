# -*- coding: utf-8 -*-
{
    'name': 'Medical Lab',
    'version': '8.0.1.1.0',
    'category': 'medical',
    'depends': ['medical'],
    'data': [
        'security/medical_lab_security.xml',
        'security/ir.model.access.csv',
        'views/medical_test.xml',
   ],
    'author': 'Eman Taha',
    'installable': True,
    'application': True,
    'auto_install': False,
}
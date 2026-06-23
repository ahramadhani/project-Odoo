{
    'name': "ahramadhanimodul",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','mail','website'],
    
     # always loaded
    'data': [
        'data/ir_sequence.xml',
        'data/ir_cron_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/add_attendees.xml',
        'report/session_report.xml',
        'views/course.xml',
        'views/session.xml',
        'views/menu.xml',
        'data/course.xml',
        'views/partner.xml',
        'views/teacher_level.xml',
        'views/portal.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}


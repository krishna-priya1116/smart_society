{
    'name': 'Smart Society',
    'version': '1.0.0',
    'summary': 'Society Management System',
    'depends': ['base','hr','mail','portal','account'],

    'data': [
        'security/society_security.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/portal_templates.xml',
        'views/smart_society_action.xml',
        'views/smart_society_menus.xml',
        'views/society_dashboard_views.xml',
        'views/society_setup_views.xml',
        'views/resident_registrations_views.xml',
        'views/parking_management_views.xml',
        'views/help_desk_views.xml',
        'views/society_alert_views.xml',
        'views/amenity_booking_views.xml',
        'views/society_maintenance_views.xml',
        'data/mail_template_data.xml',
        'data/ir_cron_data.xml',
    ],



    'installable': True,
    'application': True,

}
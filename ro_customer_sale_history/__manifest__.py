{
    'name': "Customer Sale History",

    'summary': """
        User can view the products which the customer have
        purchased just in a View easily.With the help of
        this module you can learn more about your Customers
        and their shopping habits.""",


    'description': """
        This module will help the user to see
        the shopping history of the customer Easily.
    """,

    'author': "Deja-Tech",
    'license': "AGPL-3",

    'category': 'Sales',
    'version': '18.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management','uom'],

    # always loaded
    'data': [
        'views/res_partner_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'currency': 'USD',
    'price': 18.15,
}

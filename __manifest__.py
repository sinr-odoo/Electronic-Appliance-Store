{
    'name': 'Electronic Appliances Store',
    'depends': [
                'base',
                'product',
                'sale',
                'purchase'
        ],
    'data' : [
        'security/ir.model.access.csv',
        'wizard/create_sale_order_view.xml',
        'wizard/create_purchase_order_view.xml',
        'views/product_views.xml',
        # 'views/appliance_property_rent_views.xml',
        'views/electronic_appliances_store_menu.xml',
    ],
    'application': True,
}
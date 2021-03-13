STOCKS = {
    'type': 'object',
    'properties': {
        'stock_name': {'type': 'string'},
        'bought_qty': {'type': 'integer'},
        'bought_qty_value': {'type': 'number'},
        'buying_date': {"type": "string"},
    },
    'required': ['stock_name', 'bought_qty', 'bought_qty_value', 'buying_date']
}
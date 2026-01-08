DATA_PRODUCTS = {
    "rackets" : 'http://127.0.0.1:8000/rackets'
}

def list_data_products():
    return list(DATA_PRODUCTS.key())

def get_product_url(name):
    return DATA_PRODUCTS.get(name)

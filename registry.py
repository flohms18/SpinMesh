DATA_PRODUCTS = {
    "rackets" : 'http://127.0.0.1:8001/rackets'
}

def list_data_products():
    return list(DATA_PRODUCTS.keys())

def get_product_url(name):
    return DATA_PRODUCTS.get(name)

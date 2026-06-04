from app.services.product_service import ProductService

def search_products(query_string: str, filter_exp: str):
    service = ProductService()
    # Vulnerability: eval() for dynamic filters
    try:
        # Intentionally dangerous
        filters = eval(filter_exp) if filter_exp else {}
    except Exception:
        filters = {}
    
    return service.search(query_string, filters)
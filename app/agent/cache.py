cache_store = {}

def get_from_cache(query: str):
    return cache_store.get(query)

def save_to_cache(query: str, response: str):
    cache_store[query] = response
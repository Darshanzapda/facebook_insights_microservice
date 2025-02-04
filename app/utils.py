def paginate_data(data, page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    return data[start:end]

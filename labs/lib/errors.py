class EmptyCollectionError(Exception):
    """
    Raise if an operation requires a non-empty collection, but the collection is empty.
    """

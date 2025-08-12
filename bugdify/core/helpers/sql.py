def dictfetchall(cursor):
    ''' Retorna registros do cursor como uma lista de dicionarios '''
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    
def format_query_for_debugging(query, params=None):
    """
    Formats a parameterized SQL query for direct execution in an SQL console for debugging purposes.
    This function is intended only for debugging and testing, not for constructing queries that will be executed by the application, in order to avoid risks of SQL injection.

    :param query: The SQL query with placeholders.
    :param params: A tuple or dictionary of parameters to be inserted into the query.
    :return: A formatted SQL query string with embedded parameters.
    """
    
    if not params:
        # If params is None, empty or False, return the original query
        return query
    
    if isinstance(params, dict):
        # Ensure the placeholders in the query match the dictionary keys
        assert all(key in query for key in params.keys()), "Parameter keys do not match placeholders in the query."
        formatted_query = query
        for key, value in params.items():
            if isinstance(value, str):
                formatted_query = formatted_query.replace(f"%({key})s", f"'{value}'")
            else:
                formatted_query = formatted_query.replace(f"%({key})s", str(value))

    elif isinstance(params, tuple):
        # Ensure the number of placeholders matches the number of parameters in the tuple
        assert query.count("%s") == len(params), "The count of parameters does not match the placeholders."
        formatted_query = query
        for param in params:
            if isinstance(param, str):
                formatted_query = formatted_query.replace("%s", f"'{param}'", 1)
            else:
                formatted_query = formatted_query.replace("%s", str(param), 1)
    else:
        raise TypeError("Params must be either a tuple or a dictionary")

    return formatted_query
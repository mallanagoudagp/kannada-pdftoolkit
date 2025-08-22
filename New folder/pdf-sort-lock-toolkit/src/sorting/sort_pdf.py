def sort_pdf(pdf_paths, criteria='name'):
    """
    Sorts a list of PDF file paths based on the specified criteria.

    Parameters:
    pdf_paths (list): A list of PDF file paths to be sorted.
    criteria (str): The criteria for sorting. Can be 'name' or 'date'.

    Returns:
    list: A sorted list of PDF file paths.
    """
    if criteria == 'name':
        return sorted(pdf_paths)
    elif criteria == 'date':
        return sorted(pdf_paths, key=lambda x: os.path.getmtime(x))
    else:
        raise ValueError("Invalid sorting criteria. Use 'name' or 'date'.")
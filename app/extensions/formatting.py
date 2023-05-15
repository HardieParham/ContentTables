def format_folder(root: str) -> tuple:
    """
    Function for formating folder paths, returning the name and level of the lowest folder 
    
    :param root: path string returned from the os.walk function
    :type root: string

    :rtype: tuple
    """
    folder_path = root.split('\\')
    current_dir = folder_path[-1]
    level = len(folder_path)
    return (current_dir, level)
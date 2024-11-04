import logging

# Configure the logger
logging.basicConfig(filename='logfile.txt',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def jsonButtonError(text, footer, id, options):
    if not isinstance(text, str):
        error_message_ = f"The argument 'text' must be a string - {type(text).__name__}"
        error_message = f"The argument 'text' must be a string. You passed a {type(text).__name__} - {text}."
        logging.error(error_message_)
        print(error_message)
        return False

    if not isinstance(footer, str):
        error_message_ = f"The argument 'footer' must be a string - {type(footer).__name__}"
        error_message = f"The argument 'footer' must be a string. You passed a {type(footer).__name__}"
        logging.error(error_message_)
        print(error_message)
        return False

    if not isinstance(id, list) or len(id) > 3:
        error_message_ = f"The 'id' array must contain less than 3 values - {len(id)}"
        error_message = f"The 'id' array must contain less than 3 values. {len(id)} values were given."
        logging.error(error_message_)
        print(error_message)
        return False

    # Validate that all elements in 'id' are strings
    for index, item in enumerate(id):
        if not isinstance(item, str):
            error_message_ = f"The item at index #{index}, '{item}', is not a string - {type(item).__name__}"
            error_message = f"The item at index #{index}, '{item}', is not a string. It is a {type(item).__name__}."
            logging.error(error_message_)
            print(error_message)
            return False
    
    # Check if 'options' is a list and has the same length as 'id'
    if not isinstance(options, list) or len(options) != len(id):
        error_message_ = f"The 'options' array must contain exactly {len(id)} values to match 'id' - {len(options)}"
        error_message = f"The 'options' array must contain exactly {len(id)} values to match 'id' - {len(options)} were given"
        logging.error(error_message_)
        print(error_message)
        return False
 
    return True

f = jsonButtonError("x", "v", ["t",5,"c"], [3,7,4])
print(f)
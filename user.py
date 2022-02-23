import logging
import sys
import operations
from config import configurations

def menu():
    """
    Prints the operations on screen.
    :return: user option
    """
    logging.debug("def menu()")
    try:
        print("\nMenu Options")
        print('-'*20)
        print("1. Insert")
        print("2. Find")
        print("3. Filter")
        print("4. Update")
        print("5. Delete")
        option = int(input("What would you like to do? "))
    except Exception as e:
        logging.error(e)
        sys.exit("Exiting demo. Check log for details.")
    else:
        logging.info(">>>User choice: {}".format(option))
        return option


def get_find_mode():
    """
    Gets user input of query mode. (1) One record, (!=1) for many.
    For many records will be limited as per config.configurations[LIMIT_RECORDS] parameter.
    :return: user choice
    """
    logging.debug("def get_find_mode()")
    choice = 1
    try:
        choice = int(input("Display: (1) One record or (!=1)Many? "))
    except Exception as e:
        logging.error(e)
        logging.warning("Mode = 1 by default.")
    finally:
        logging.info("Choice = {}".format(choice))
        return choice


def get_key_value_pair(op):
    """
    Get the key value pair of fields and values which can be used for filtering, inserting, updating etc.
    :param a verb to be displayed in the message "Enter field and corresponding values for ______"
    :return a dictionary:
    """
    logging.debug("def get_key_value_pair()")
    d = {}
    try:
        print("Enter field and corresponding values for {}: ".format(op))
        while True:
            field = input("Enter field name: ")
            if field in configurations["INT_FIELDS"]:
                value = int(input("Enter value:"))
            else:
                value = input("Enter value: ")
            logging.debug(">>>Key:{}, Value={}".format(field, value))
            d[field] = value
            c = input("Do you want to add more fields?(y/n) ").lower()
            if c[0] != 'y':
                logging.debug(">>>Data:{}".format(d))
                break
    except Exception as e:
        logging.error(e)
        sys.exit("Exiting demo. Check log for details.")
    else:
        return d


def get_update_details():
    """
    Prepares the filtering condition and get the fields and corresponding new values for updation operation.
    :return: a tuple of filters(index 0) and update parameters(index 1) each a dictionary.
    """
    logging.debug("get_update_details()")
    filters = get_key_value_pair("filtering")
    update = get_key_value_pair("updation")
    return filters, update


def init(collection):
    """
    Calls the respective db operations functions as per user choice.
    :param: collection The collection on which db ops will be performed.
    :return: None
    """
    logging.debug("def init(collection)")
    print("\n\n*******MongoDB Implementation Demo*******")
    op = operations.Ops(collection)
    while True:
        choice = menu()
        if choice == 1:
            d = get_key_value_pair("insertion")
            op.insert(d)
        elif choice == 2:
            mode = get_find_mode()
            op.find(mode)
        elif choice == 3:
            op.filter(get_key_value_pair("filtering"))
        elif choice == 4:
            op.update(get_update_details())
        elif choice == 5:
            op.delete(get_key_value_pair("filtering"))
        else:
            print("Wrong option entered!")
        c = input("Do you want to perform more operations?(y/n) ").lower()
        logging.info(">>>Continue?: {}".format(c))
        if c[0] != 'y':
            logging.info(">>>Exiting demo.")
            sys.exit("Exiting demo... Good day!!.")

import logging
import database
import user
import sys
from config import configurations


def intro_task():
    """
    Gives a brief description of the Task
    :return: None
    """
    logging.debug("def introTask()")
    print("Task: MongoDB")
    print("Date: 19 Feb 2022")
    print("""Task Description:
    Upload the dataset https://archive.ics.uci.edu/ml/machine-learning-databases/00448/carbon_nanotubes.csv 
    to MongoDB and perform various operations on it.""")


def intro_owner():
    """
    Gives a brief description of Project owner.
    :return: None
    """
    logging.debug("def introOwner()")
    print("Project Owner: Liji Alex")
    print("Course: FSDS")


def init_logs():
    """
    Initializes the log file and default logging format
    :return: None
    """
    try:
        logging.basicConfig(filename=configurations["LOG_FILE"], level=configurations["DEBUG_LEVEL"],
                            format='%(asctime)s %(levelname)s %(message)s')
        logging.info("\n**********New execution begins************")
        logging.debug("def initLogs()")
    except FileNotFoundError as e:
        print("Error: ", e)
        sys.exit("Exiting demo. Check log for details.")
    except Exception as e:
        print("Error: ", e)
        sys.exit("Exiting demo. Check log for details.")


def initialize():
    """
    Initializes the project parameters and starts the project execution.
    :return: None
    """
    init_logs()
    intro_owner()
    intro_task()
    collection = database.initialize()
    logging.debug(collection)
    user.init(collection)


if __name__ == '__main__':
    initialize()

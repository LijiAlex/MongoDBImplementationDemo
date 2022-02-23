import logging
import pymongo
import pandas as pd
import json
import sys


db = None


def connect_to_db():
    """
    Connect to database named CarbonNanoTubes.
    :return: None
    """
    logging.debug("def connect_to_db()")
    db_name = "CarbonNanoTubes"
    try:
        global db
        client = pymongo.MongoClient(
            "mongodb+srv://mongodb:mongodb@cluster0.ffrz7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client[db_name]
        logging.debug(db)
        if client.get_database(db_name):
            logging.info(">>>Database connection successful.")
        else:
            logging.error(">>>Database connection failed.")
    except Exception as e:
        logging.error(e)
        sys.exit("Exiting demo. Check log for details.")


def get_collection():
    """
    Returns the collection for the data.
    :return: collection
    """
    try:
        logging.debug("def get_collection()")
        col_name = "carbon_nano_tubes"
        if col_name in db.list_collection_names():
            my_col = db.get_collection(col_name)
            logging.debug(">>>Collection already exists.")
        else:
            my_col = db[col_name]
            logging.info(">>>Collection created successfully.")
    except Exception as e:
        logging.error(e)
        sys.exit("Exiting demo. Check log for details.")
    else:
        logging.debug(my_col)
        return my_col


def load_data():
    """
        Reads CSV file and loads data to collection if it doesn't exist
        :return: None
    """
    try:
        logging.debug("def load_data()")
        my_col = get_collection()
        if my_col.count() == 0:
            file_name = "carbon_nanotubes.csv"
            data = pd.read_csv(file_name, sep=';')
            logging.debug(">>>CSV read.")
            payload = json.loads(data.to_json(orient='records'))
            logging.debug(">>>Data converted to json.")
            my_col.insert(payload)
            if my_col.count() > 0:
                logging.info(">>>Data loaded to collection: {} records".format(my_col.count()))
            else:
                logging.error(">>>Data load failed.")
        else:
            logging.info(">>>Data already exists: {} records".format(my_col.count()))
    except Exception as e:
        logging.error(e)
        sys.exit("Exiting demo. Check log for details.")
    else:
        return my_col


def initialize():
    """
    1. Establish database connection.
    2. Loads the data.
    :return:
    """
    logging.debug("def initialize()")
    connect_to_db()
    return load_data()

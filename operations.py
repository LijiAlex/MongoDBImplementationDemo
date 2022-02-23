from pprint import pprint
import logging
from config import configurations

class Ops:
    """
    Handles database operations.
    """
    def __init__(self, c):
        """
        Initializes the collection object.
        :param c: collection
        """
        logging.debug("def __init__(self, c)")
        self.collection = c

    def insert(self, d):
        """
        Insert the value passed to database
        :param d: data to be inserted in form of dictionary
        :return: None
        """
        try:
            logging.debug("def insert(self, d)")
            self.collection.insert_one(d)
            logging.info(">>>Data inserted: {}".format(d))
        except Exception as e:
            logging.error(e)

    def find(self, mode):
        """
        Queries and displays data.
        Many record display will be limited as per the parameter config.configurations["LIMIT_RECORDS"]
        :param mode: 1 for single record, !=1 for many
        :return: None
        """
        try:
            logging.debug("def find(self)")
            if mode == 1:
                pprint(self.collection.find_one())
                logging.debug(self.collection.find_one())
            else:
                for record in self.collection.find().limit(configurations["LIMIT_RECORDS"]):
                    pprint(record)
                    logging.debug(record)
            logging.info(">>>Query Successful")
        except Exception as e:
            logging.error(e)

    def filter(self, d):
        """
        Queries and displays data based on filter condition.
        :param d: a dictionary
        :return: None
        """
        try:
            logging.debug("def filter(self, d)")
            cur = self.collection.find(d)
            if cur.count() == 0:
                print("No record matching the filter condition.")
            else:
                for rec in cur:
                    pprint(rec)
                    logging.debug(rec)
            logging.info(">>>Query Successful.filter={},count={}".format(d, cur.count()))
        except Exception as e:
            logging.error(e)

    def update(self, details):
        """
        Update documents based on some filter conditions
        :param details: index 0: dictionary for filter
        index 1: dictionary of values for updation
        :return:
        """
        try:
            logging.debug("def update(self, d)")
            new_values = {"$set": details[1]}
            count = self.collection.update_many(details[0], new_values).modified_count
            logging.info("{} records updated".format(count))
        except Exception as e:
            logging.error(e)

    def delete(self, d):
        """
        Delete documents based on filter condition
        :param d: filter dictionary
        :return:
        """
        try:
            logging.debug("def delete(self, d)")
            count = self.collection.delete_many(d).deleted_count
            logging.info("{} records deleted".format(count))
        except Exception as e:
            logging.error(e)

import os
import logging
import collections.abc

logging.basicConfig(filename="dictionary_log.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")


class dictionary_functions:
    with open('dictionary_log.log', 'w'):
        pass

    def __init__(self, dict1):
        try:
            logging.info("logging begins here")
            self.dict1 = dict1 if type(dict1) == dict else logging.error("the input isnt a dictionary, please check")
        except Exception as e:
            logging.error(e)


    def all_keys(self, dict1):
        try:
            for key, value in dict1.items():
                yield key
                if isinstance(value, dict):
                    for k in self.all_keys(value):
                        yield k
        except Exception as e:
            logging.error(e)

    def dict_keys(self):
        try:
            logging.info("the keys in the dictionary %s are", self.dict1)
            for key in self.all_keys(self.dict1):
                logging.info(key)
        except Exception as e:
            logging.error(e)


    def all_values(self, dict1):
        try:
            for k, v in dict1.items():
                if isinstance(v, dict):
                    yield from self.all_values(v)
                else:
                    yield v
        except Exception as e:
            logging.error(e)


    def dict_values(self):
        try:
            logging.info("the values in the dictionary %s are", self.dict1)
            for value in self.all_values(self.dict1):
                logging.info(value)
        except Exception as e:
            logging.error(e)


    def dict_update(self, dict_to_update, dict_to_insert):
       try:
            if isinstance(dict_to_insert, dict):
                for k, v in dict_to_insert.items():
                    if isinstance(v, collections.abc.Mapping):
                        dict_to_update[k] = self.dict_update(dict_to_update.get(k, {}), v)
                    else:
                        dict_to_update[k] = v
                self.dict1 = dict_to_update
                logging.info("the updated dictionary is %s", self.dict1)
            else:
                logging.error("the passed values isn't a dictionary")
       except Exception as e:
           logging.exception(e)


    def dict_get(self,key,dict2):
        try:
            for k, v in dict2.items():
                if k == key:
                    logging.info("the value of the given key %s is %s", k, v)
                else:
                    continue
        except Exception as e:
            logging.error("the passed key isnt present in the dictionary, please try again")


    def dict_pop_last_inserted(self, dict3):
        try:
            last_key = sorted(dict3.keys())[-1]
            logging.info("the last inserted key of the dictionary is %s", last_key)
            logging.info("the last inserted key, value pair of the passed dictionary is %s:%s", last_key, dict3[last_key])
        except Exception as e:
            logging.exception(e)



dict1 = {'level1': {'level2': {'levelA': 0, 'levelB': 1}}}
dict2 = {'level1': {'level2': {'levelA': 0, 'levelB': 1}}}
dict3 = { 'a': 5, 'b': 56, 'c': 78}


dict_functions = dictionary_functions(dict1)
dict_functions.dict_keys()
dict_functions.dict_values()
dict_functions.dict_update(dict1, {'level1': {'level2': {'levelB': 10}}})
dict_functions.dict_get('level1', dict2)

dict_functions.dict_update(dict3, {'d': 40})
dict_functions.dict_pop_last_inserted(dict3)

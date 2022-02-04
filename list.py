import logging
import os

os.chdir(r'C:\Users\Admin\iNeuron\packages')
logging.basicConfig(filename='list_log.log', level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")


class list_functions:
    # with open('list_log.log', 'w'):
    #     pass

    def __init__(self, list1):
        logging.info("Logging begins here")
        if type(list1) == list:
            logging.info("entered parameter is a list")
            self.list1 = list1
        else:
            logging.error("entered parameter isnt a list")

    def list_length(self):
        try:
            self.count=-1
            list2 = []
            for i in self.list1:
                list2.append(self.list1[self.count])
                self.count += 1
            logging.info("the length of the list is %s",self.count)
        except Exception as e:
            logging.error(e)

    def list_insert(self,pos,ele):
        try:
            logging.info("the count is %s", self.count)
            self.pos = pos
            self.ele = ele
            if self.pos > self.count:
                logging.error("the position is out of bounds, please enter a new position")
            else:
                self.list1[pos] = self.ele
                logging.info("the new inserted list at position %s is %s", self.pos, self.list1)
        except Exception as e:
            logging.error(e)


    def list_pop(self,index):
        try:
            self.index = index
            if self.index > self.count:
                logging.error("Cant retrieve from that position, out of bounds")
            else:
                logging.info("the element at position %s of the list is %s", self.pos, self.list1[self.pos])
        except Exception as e:
            logging.exception(e)

    def list_max(self):
        try:
            self.max=0
            for i in range(self.count+1):
                if isinstance(self.list1[i], (int, float)):
                    self.max = self.list1[i] if self.list1[i] >= self.max else self.max
            logging.info("the maximum number in the list is %s", self.max)
        except Exception as e:
            logging.error(e)

    def list_min(self):
        try:
            self.min = self.list1[1]
            for i in range(self.count+1):
                if isinstance(self.list1[i], (int, float)):
                    self.min = self.list1[i] if self.list1[i] < self.min else self.min
            logging.info("the minimum number in the list is %s", self.min)
        except Exception as e:
            logging.error(e)


list1 = [9, 5, 109.31, -1, -4, 0]
list_functions = list_functions(list1)
list_functions.list_length()

list_functions.list_insert(2, 100)

list_functions.list_pop(4)

list_functions.list_max()
list_functions.list_min()
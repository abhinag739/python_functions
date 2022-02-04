import logging
import os

os.chdir(r"C:\Users\Admin\iNeuron\packages")
logging.basicConfig(filename='tuple_log.log', level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

class tuple_functions:

    with open('tuple_log.log', 'w'):
        pass

    def __init__(self, tuple1):

        logging.info("logging begins here")
        try:
            if type(tuple1) == tuple:
                logging.info("Entered tuple is a tuple object")
                self.tuple1 = tuple1
            else:
                logging.error("the passed tuple isnt a tuple object, please try again")
        except Exception as e:
            logging.error(e)

    def tuple_length(self):
        try:
            self.count = 0
            # As tuple is immutable we create a temporary list out of the tuple in question
            L2 = list(self.tuple1)
            for i in self.tuple1:
                L2.append(self.tuple1[self.count])
                self.count += 1
            logging.info("the length of the tuple is %s", self.count-1)

        except Exception as e:
             logging.error(e)
        return self.count

    def tuple_insert(self,pos,ele):
        try:
            logging.info("the count is %s", self.count)
            self.pos = pos
            self.ele = ele
            self.tuple2 = ()
            self.L2 = list(self.tuple1)
            if self.pos > self.count:
                logging.error("the position is out of bounds, please enter a new position")
            else:
                self.L2 = self.L2[:self.pos] + [self.ele] + self.L2[self.pos:]
                self.tuple2 = tuple(self.L2)
                logging.info("the new inserted tuple at position %s is %s", self.pos, self.tuple2)
        except Exception as e:
            logging.error(e)


    def tuple_pop(self,pos):
        try:
            self.pos = pos
            if not self.tuple2 and self.pos < self.count:
                logging.info("the element at position %s is %s", self.pos, self.tuple1[pos])
            elif len(self.tuple2) > 0:
                logging.info("the element at position %s is %s", self.pos, self.tuple2[pos])
        except Exception as e:
            logging.error(e)

    def tuple_max(self):
        try:
            self.max = 0
            if not self.tuple2:
                for i in self.tuple1:
                    self.max = i if i > self.max else self.max
                logging.info("the maximum element in the tuple %s is %s", self.tuple1, self.max)
            else:
                for i in self.tuple2:
                    self.max = i if i > self.max else self.max
                logging.info("the maximum element in the tuple %s is %s", self.tuple2, self.max)
        except Exception as e:
            logging.error(e)


    def tuple_min(self):
        try:
            if not self.tuple2:
                self.min = self.tuple1[1]
                for i in self.tuple1:
                    self.min = i if i < self.min else self.min
                logging.info("the minimum element in the tuple %s is %s", self.tuple1, self.min)
            else:
                self.min = self.tuple2[1]
                for i in self.tuple2:
                    self.min = i if i < self.min else self.min
                logging.info("the minimum element in the tuple %s is %s", self.tuple2, self.min)
        except Exception as e:
            logging.error(e)


tuple1 = (-1, 9, 4, 5, 3)
tuple_functions = tuple_functions(tuple1)
tuple_functions.tuple_length()
tuple_functions.tuple_insert(0, 109)

tuple_functions.tuple_pop(1)
tuple_functions.tuple_max()
tuple_functions.tuple_min()



import datetime
import pprint as pp
import json

import telegram_bot
from connect_mongoDB import connect_db

my_db = connect_db("test_1")
my_collection = my_db['dictionary']

class document():

    default_number = 1

    def __init__(self, date=datetime.datetime.now(), year=datetime.datetime.year):
        """constructor class"""

        self.date = date
        self.year = year


def control_time(funk):
    """control time execute"""
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = funk(*args, **kwargs)
        print(datetime.datetime.now() - start)
        return result
    return wrapper

@control_time
def create_dic(line, col):
    """Documentation"""
    return_dic = {f'kinder_{num}': num for num in range(1, line+1)}
    for key in return_dic:
        if key == 'kinder_1':
            return_dic[key] = {f'information{1}': {'N1': {'NN1': 1}, 'N2': {'NN2': 2, 'NN3': 3}, 'N3': 3}}
    return_dic[key] = {f'andere{2}': {'str1': {'col1': 2}, 'str2': {'col1': 2, 'col2': 3}, 'str3': {'col1':1, 'col2': 2, 'col3': 3}}}
    return return_dic






def main():

    # """main"""
    # my_dict = create_dic(2, 10)
    # pp.pprint(my_dict)
    # for key in my_dict:
    #     my_collection.insert_one({key: my_dict[key]})
    #
    #
    # # doc1 = document()
    # doc2 = document()
    # doc1.default_number = 2
    # doc2.default_number = 1
    # print(doc1 == doc2)
    # print(doc2.default_number)
    # print(doc1.default_number)






if __name__ == '__main__':
   main()

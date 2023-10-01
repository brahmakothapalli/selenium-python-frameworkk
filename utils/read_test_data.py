""" This module reads the data from the given json file """

import json


class ReadTestData:

    @staticmethod
    def get_test_data():
        global test_data
        with open("/home/brahma/qababuworks/selenium-python-framework/test_data/loginpage.json", 'r') as file:
            data_dict = json.load(file)
        for key in data_dict.keys():
            if key == 'test_login_positive':
                # print(f"no of data sets of the test case are {len(data_dict[key])}")
                print(data_dict[key])
                if data_dict[0]['run'] == 'Y':
                    data = list(data_dict[0])
        print(data)
        # for key in data_dict.keys():
        #     testdata = data_dict[key]
        #     print(testdata)
        #     if key == 'test_login_negative':
        #         my_list = data_dict[key]
        #         print(my_list)
        #         # print(my_list[0]['username'])
            # for val in data_dict[key]:
            # print(val['username'])


ReadTestData.get_test_data()

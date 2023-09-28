""" This module reads the data from the given json file """

import json


class ReadTestData:
    print("reading test data")

    @staticmethod
    def get_test_data():
        with open("/home/brahma/qababuworks/selenium-python-framework/test_data/loginpage.json", 'r') as file:
            data_dict = json.load(file)
        # print(data_dict)
        # for key in data_dict.keys():
        #     if key == 'test_login_positive':
        #         print(len(data_dict[key]))
        #         print(data_dict[key])
        #         if data_dict[0]['run'] == 'Y':
        #             pass

        for key in data_dict.keys():
            testdata = data_dict[key]
            # print(testdata)
            if key == 'test_login_negative':
                my_list = data_dict[key]
                print(my_list)
                # print(my_list[0]['username'])
            # for val in data_dict[key]:
            # print(val['username'])


ReadTestData.get_test_data()

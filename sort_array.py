"""
Requirements:
    1. unsorted-names-list.txt will be given
    2. Sort by last name then given name
Assumption:
    1. A > a, a> B,
    2. case insensitive

"""
import string


class NameList:
    def __init__(self, array):
        self.trans = ''.join(list(string.maketrans('', '')))
        self.data = array

    def sorting_last_name(self, data):
        # case insensitive with alphabetical order
        return string.split(data)[-1].lower()

    def sort(self):
        new_list = map(
            lambda x: (
                string.translate(self.sorting_last_name(x), self.trans),
                x),
            self.data)
        new_list.sort()
        return map(lambda x: x[-1], new_list)

    @staticmethod
    def read_and_store():
        unsorted_names = []
        # read file
        try:
            file1 = open('unsorted-names-list.txt', 'r')
        except Exception as e:
            print(e)
            return
        lines = file1.readlines()
        for line in lines:
            if line.strip():
                unsorted_names.append(line.strip())
        file1.close()

        # sort by requirement
        new_list = NameList(unsorted_names)
        sorted_names = new_list.sort()

        file2 = open('sorted-names-list.txt', 'w')
        for item in sorted_names:
            print('{}'.format(item))
            file2.writelines('{}\n'.format(item))
        file2.close()


NameList.read_and_store()



class Interest:
    name = "My Interest"

    def __init__(self):
        self.interest = {"오버워치":"게임", "WOW":"게임", "Python":"프로그래밍"}

    def add(self, key, value):
        self.interest[key] = value

    def delete(self, key):
        del self.interest[key]

    def count(self):
        '''
        dict_count = 0
        for _ in self.interest:
            dict_count += 1

        return dict_count
        '''
        return self.interest.__len__()

    def get_keys(self):
        return list(self.interest.keys())

    def get_values(self):
        # return set(self.interest.values())

        list_value = []

        for item in self.interest.values():
            try:
                list_value.index(item)
            except ValueError:
                list_value.append(item)

        return list_value

    def write_dict_in_file(self):
        count = 0
        keys = list(self.interest.keys())
        values = list(self.interest.values())

        with open("D:/dict.txt", "w+") as file:
            while count < self.count():
                # strData = "({0}, {1})".format(keys[count], values[count])
                str_data = "(" + keys[count] + ", " + values[count] + ")\n"
                file.write(str_data)
                count += 1

import logging, math


class Array:
    @staticmethod
    def median(*args):
        x = 0
        array = []
        while x < len(args):
            if isinstance(args[x], list):
                array += args[x]
            else:
                logging.error(f"Unexpected type {type(args[x])}")
                break
            x += 1
        array.sort()
        if len(array) % 2 == 0:
            sum_ = (array[math.ceil(len(array) / 2)] + array[math.ceil(len(array) / 2) - 1])
            return sum_ / 2
        else:
            return array[math.ceil(len(array) / 2) - 1]

    @staticmethod
    def mean(list_of_items):
        # comment
        total_sum = 0
        for x in list_of_items:
            total_sum += x
        return (total_sum / len(list_of_items),
                math.ceil(total_sum / len(list_of_items)),
                math.floor(total_sum / len(list_of_items)))

    @staticmethod
    def get_types(li_):
        types = []
        if isinstance(li_, list):
            for x in li_:
                types.append(str(type(x)))
            return types
        else:
            return str(type(li_))

    @staticmethod
    def remove_element(li_, target=0):
        str_ = ""
        for x in range(len(li_)):
            str_ += str(li_[x])
        data = str_.replace(str(target), "")
        arr = [int(i) for i in data]
        return arr

    @staticmethod
    def search_insert_position(number, target):
        if isinstance(number, list) and isinstance(target, int):
            if target in number:
                return number.index(target)
            else:
                number.append(target)
                number.sort()
                return number.index(target)
        else:
            return []

    @staticmethod
    def flip_image(array):
        for x in range(len(array)):
            if isinstance(array, list):
                array[x].reverse()
            else:
                raise TypeError(f"Expected a 2d array")
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j] == 0:
                    array[i][j] = 1
                elif array[i][j] == 1:
                    array[i][j] = 0
        return array

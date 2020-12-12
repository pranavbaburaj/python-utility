import uuid


class Generate:
    """
    @create a  unique code which is not present in the list
    and have specified maxlength ans contains
    the specified group of characters(strings)
    """
    @staticmethod
    def code(maxlength=8, contain="", list_=[]):
        unique_code = uuid.uuid4()
        if len(str(unique_code)) >= 8:
            unique_code = str(unique_code)[:maxlength]
        else:
            unique_code = unique_code
        unique_code = str(unique_code) + contain
        if unique_code not in list_:
            return unique_code
        else:
            return None


class String:
    @staticmethod
    def remove_duplicates(string_):
        if isinstance(string_, str):
            result = ""
            for x in range(len(string_)):
                """
                Check if the character is present inside 
                of the string and if not add to it the
                final string to return
                """
                if string_[x] in result:
                    pass
                else:
                    result += str(string_[x])
            return result
        else:
            return ""

    @staticmethod
    def isEqual(array, second_array):
        """
            @:param : number[], number[]
            @:returns : bool, None
        """
        if isinstance(array, list) and isinstance(second_array, list):
            str_form_one = ""
            str_form_two = ""

            for x in range(len(array)):
                str_form_one += str(array[x])

            for i in range(len(second_array)):
                str_form_two += str(second_array[x])

            return str_form_two == str_form_one
        else:
            raise TypeError("Unexpected type")

    @staticmethod
    def is_palindrome(str_object):
        if isinstance(str_object, str):
            return str_object[::-1] == str_object
        else:
            return ""

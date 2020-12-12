class Number:
    @staticmethod
    def fibonacci(value=0):
        arr = []
        i = 0

        while i < value + 1:
            if i == 0 or i == 1:
                arr.append(i)
            else:
                arr.append(arr[i - 1] + arr[i - 2])
            i += 1

        return arr, arr[len(arr) - 1]

    @staticmethod
    def factors(value=1):
        arr = []
        i = 1

        while i < (value + 1):
            if value % i == 0:
                arr.append(i)
            i += 1
        return arr

    @staticmethod
    def is_palindrome(number):
        number = str(number).replace(".", "")
        return number[::-1] == number


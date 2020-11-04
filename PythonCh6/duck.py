class Duck:

    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_input_name):
        self.__name = new_input_name

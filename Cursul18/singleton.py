class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)

    # def __init__(self):
    #     if Singleton._instance == None:
    #         Singleton._instance = self
    #     else:
    #         raise Exception("This class is a singleton!")
    #
    # @staticmethod
    # def getInstance():
    #     if Singleton._instance == None:
    #         Singleton()
    #     return Singleton._instance
import sys #for exception handling
from src.logger iport loggn

def error_message_detail(error,error_detail:sys):  #to give an own custom message of the error
    _,_,exc_tb=error_detail.exc_info() #on which file on which line the error has occured 
    file_name=exc_tb.tb_frame.f_code.co_filename #in which file name the error is generated
    error_message="Error occured in pytoon script name [{0}] line number [{1}] error message [{2}]".format()
    file_name,exc_tb.tb_lineno,str(error)

class CustomExeption(Exception):
    def __init__(self,error_message,error_detail:sys)
        super.init__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):   #based on inheritance 
        return self.error_message   #prints the error message

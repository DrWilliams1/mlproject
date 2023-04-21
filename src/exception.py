import sys
import logging
"""The sys module provides various functions and variables that are used to
manipulate different parts of the python runtime environment"""

def error_message_detail(error, error_detail:sys): 
    #<-error present in the sys
#Whenever an error is raised I am pushing my own custom message
    _,_,exc_tb=error_detail.exc_info()
    """This is talking about the execution info:
    exc_tb variable gives info about the file_name,line number, and error message"""
    file_name=exc_tb.tb_frame.f_code.co_filename
    """File name variable will give us the file name:"""
    error_message='Error occured in python script name [{0}] line number [{1}] error message [{2}]'.format(
    file_name, exc_tb.lineno,str(error))
    """When an error is raised this function will be called"""

    return error_message
    

    class CustomException(Exception):
        def __init__(self,error_message, error_detail:sys):
            super().__init__(error_message)
            self.error_message= error_message_detail(error_message, error_detail=error_detail)

        def __str__(self):
            return self. error_message
        

  


    

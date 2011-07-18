#!/usr/bin/env python
import unittest

# the following three lines's purpose is to make the code in the sister 'src' folder available to the tests
import sys
import os
sys.path.append(os.path.join('..', 'src'))

from CommandLineManager import * 

# helper method splitting the command line in a list of parameters/arguments
def getArgs(commandLine):
    list= commandLine.split()
    
    return list


class CommandLineManagementTests(unittest.TestCase):
    def test1(self):
        """The CommandLineManager receives the list of parameters/arguments and, if the specified action is valid, receives
        the corresponding Executor; the Executor contains the validation of the received commandLine"""
        
        
        clm=CommandLineManager()
        executor=clm.getExecutor(getArgs('drop BP -spam'))
        assert isinstance(executor, DropExecutor), 'I was expecting a DropExecutor because the action is \'drop\', but I got something else...'
        
        assert not executor.cl_formally_valid(), '-spam parameter is not supported' 
        
        assert isinstance(clm.getExecutor(getArgs('-drop BP')), DropExecutor), 'I was expecting a DropExecutor but I got something else...'

        assert clm.getExecutor(getArgs('DROP BP'))==None, 'DROP in capital letters should not be a valid action parameter'
        assert clm.getExecutor(getArgs('spam BP'))==None, 'spam is not a supported action'
    
          
if __name__ == "__main__":
    unittest.main()
    
#!/usr/bin/env python
import unittest

# the following three lines's purpose is to make the code in the sister 'src' folder available to the tests
import sys
import os
sys.path.append(os.path.join('..', 'src'))

from ConfigurationManagement import * 


class ConfigurationManagerTests(unittest.TestCase):
    def test1(self):
        cm = ConfigurationDescriptor()
        cm.load('ConfigManagerTest1/revolutioner.properties')
        pd=cm.getProductDescriptor('PRODUCT1')
        assert pd is not None
        
        
        assert pd.getOracleConnectionString()=='OracleConnectionString'
        
        assert pd.getEvolutionFolder() == 'evolutionFolderPath'       
        
        assert pd.hasUser('user1')
        assert  pd.getCredentials('user1')==('pippo','password')
               
        pd=cm.getProductDescriptor('spam')
        assert pd is None
        
        
        

    
          
if __name__ == "__main__":
    unittest.main()
    
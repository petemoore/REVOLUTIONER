#!/usr/bin/env python

class ConfigurationDescriptor():
    
    def __init__(self):
        self.productDescriptors=None
    
    def load(self, abs_file_path):
        self.productDescriptors={}
        propFile= file( abs_file_path, "r" )
        propDict= dict()
        for propLine in propFile:
            propDef= propLine.strip()
            if len(propDef) == 0:
                continue
            if propDef[0] in (  '#' ):
                continue
            punctuation= [ propDef.find(c) for c in ':= ' ] + [ len(propDef) ]
            found= min( [ pos for pos in punctuation if pos != -1 ] )
            name= propDef[:found].rstrip()
            value= propDef[found:].lstrip(":= ").rstrip()
            
            import re
            regex=re.compile('([^.]*)\.(.*)')
            match=regex.match(name)
            if match:
                product=match.group(1)
                if product not in self.productDescriptors:
                     self.productDescriptors[product]=ProductDescriptor()
                self.productDescriptors[product].addProperty(match.group(2),value)
            else:
               raise Exception()
            
            
            propDict[name]= value
        propFile.close()
    
    def getProductDescriptor(self, product):
        assert self.productDescriptors is not None, "Configuration non initialised"
        if product in self.productDescriptors:
            return self.productDescriptors[product]
        else:
            return None
            
    
class ProductDescriptor():
    def __init__(self):
        self.users={}
        self.oracle_connection_string=None
        self.evolution_folder=None
        
    def getOracleConnectionString(self):
        return self.oracle_connection_string
    
    def getEvolutionFolder(self):
        return self.evolution_folder

    def hasUser(self,alias):
        return alias in self.users
    
    def getCredentials(self, alias):
        return self.users[alias].getCredentials()
    
    def addProperty(self, name, value):
        
        if name=='oracle_connection_string':
            self.oracle_connection_string=value
            return
        if name=='evolution_folder':
            self.evolution_folder=value
            return
        
        import re
        regex= re.compile('([^.]*)\.username.*')
        match=regex.match(name)
        if match:
            alias= match.group(1)
            if alias not in self.users:
                self.users[alias]=UserDescriptor()
            self.users[alias].setUsername(value)
            return
        
        regex= re.compile('([^.]*)\.password.*')
        match=regex.match(name)
        if match:
            alias= match.group(1)
            if alias not in self.users:
                self.users[alias]=UserDescriptor()
            self.users[alias].setPassword(value)        
            return
        print 'Invalid property: %s:%s' % (name, value)
           
    
    def __str__(self):
        result=''
        for item in self.users:
            result+= item.__str__()+'\n'
        return result
    
        
        
class UserDescriptor():
    def __init__(self):
        self.username=None
        self.password=None
    
    def setUsername(self, username):
        self.username=username
    
    def setPassword(self, password):
        self.password=password
        
    def getCredentials(self):
        return self.username,self.password
    
    def __str__(self):
        return '%s -> %s' (self.username,self.password)
    
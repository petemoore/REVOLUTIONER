#!/usr/bin/env python

    
def getParametersMap(command_line_args):
      parametersMap={}
    
      action=command_line_args[0]
    
      parametersMap[action]=[]
    
      previousParameter=action
    
      for item in command_line_args[1:]:
        if item.startswith('-'):
            parametersMap[item]=[]
            previousParameter=item
        else:
            parametersMap[previousParameter].append(item)
      return action, parametersMap

class CommandLineManager:
    def getExecutor(self,command_line_args):        
        action,map=getParametersMap(command_line_args)
        
        for cls in Executor.__subclasses__():
            if cls.is_executor_for(action):
                return cls(action, map)
        return None

    
class Executor(object):    
    def __init__(self, action, parametersMap):
        self.action, self.parametersMap=action, parametersMap
    
class DropExecutor(Executor):  
    
  def __init__(self, action, parametersMap):
    super(DropExecutor, self).__init__(action,parametersMap)
    self.supportedParameters=set(['drop','-drop']) 
                   
  @classmethod
  def is_executor_for(self, action):
    if action is None :
        return False
    else:        
        if action in ('drop','-drop'):
            return True    
        
  def cl_formally_valid(self):
    parameters=self.parametersMap.keys()
    for parameter in parameters:
        if parameter is not self.action and parameter not in self.supportedParameters:
            return False
    return True   
    
        
        

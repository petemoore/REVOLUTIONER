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
  _myActions=('drop','-drop')
  
  @classmethod
  def is_executor_for(self, action):
    if action is None :
        return False
    else:        
        if action in DropExecutor._myActions:
            return True 
    
  def __init__(self, action, parametersMap):
    assert action in DropExecutor._myActions, "I don't support %s action!" % action
    super(DropExecutor, self).__init__(action,parametersMap)                  
   
        
  def cl_formally_valid(self):
    actualParameters=self.parametersMap.keys()
    supportedParameters=set(DropExecutor._myActions)
    for parameter in actualParameters:
        if parameter not in supportedParameters:
            return False
    return True   
    
        
        

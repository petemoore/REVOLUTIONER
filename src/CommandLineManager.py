#!/usr/bin/env python

class CommandLineManager:
    def getExecutor(self,command_line_args):
        for cls in Executor.__subclasses__():
            if cls.is_executor_for(command_line_args):
                return cls(command_line_args)
        return None
    
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
      return parametersMap
    
class Executor(object):  
    
    def __init__(self, command_line_args):
        self.parametersMap=self.getParametersMap(command_line_args)
    
class DropExecutor(Executor):
  def __init__(self, command_line_args):
    self.supportedParameters=set(['drop','-drop'])
    self.parametersMap=getParametersMap(command_line_args)
    
  @classmethod
  def is_executor_for(self, command_line_args):
    if len(command_line_args)==0:
        return False
    else:
        command=command_line_args[0]
        if command=='drop' or command=='-drop':
            return True    
        
  def cl_formally_valid(self):
    parameters=self.parametersMap.keys()
    for parameter in parameters:
        if parameter not in self.supportedParameters:
            return False
    return True   
    
        
        

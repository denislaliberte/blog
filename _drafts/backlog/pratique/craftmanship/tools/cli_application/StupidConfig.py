import yaml
config_array={}
config_path=""

def generate_config(name):
  variable_path = name + ".yaml"
  return StupidConfig(variable_path)


class StupidConfig:
  def __init__(self,config_path):
    self.config_path = config_path
    self.config_array = self.import_variables(config_path)

  def import_variables(self,variables_path):
    try:
      stream = open(variables_path, 'r')
      variables =yaml.load(stream)
    except:
      variables ={}
    return variables

  def get_variable(self,key,example=""):
    if key in self.config_array:
      value = self.config_array[key]
    else:
      value = self.promt_for_value(key,example)
      self.config_array[key] = value
    return value

  def set_variable(self,key,value):
    self.config_array[key]=value


  def promt_for_value(self,key,example):
      message_placeholder = "{key} in not in the file {path}, enter the value {example} : "
      message = message_placeholder.format(key=key,path=self.config_path,example=example)
      return raw_input(message)

  def dump_to_file(self):
    stream = open(self.config_path,"w")
    config_string = yaml.dump(self.config_array,default_flow_style=False)
    stream.write(config_string)

#!/usr/bin/env python3

class MyString:
  pass

  def __init__(self, value = ''):
    self.value = value
  
  def set_value(self, value):
    ##check if  the value is a String
    if (type(value) == str):
       ##create instance variable "value"
      self._value = value
    else:
      print("The value must be a string.")
    
  def get_value(self):
    return self._value
    
  value = property(get_value, set_value)
    
  def is_sentence(self):
    return True if self._value.endswith('.') else False

  
  def is_question(self):
    return True if self._value.endswith('?') else False

  
  def is_exclamation(self):
    return True if self._value.endswith('!') else False
  
  def count_sentences(self):
    i = 0
    for val in self._value.split():
      if val.endswith('.') or val.endswith('!') or val.endswith('?'):
        i += 1
    return i
    
  
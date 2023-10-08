class Currency:

  currencies =  {'CHF': 0.930023, #swiss franc 
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar
      
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def changeTo(self, new_unit):
    """
      An Currency object is transformed from the unit "self.unit" to "new_unit"
    """
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit
  
  #add magic methods here
  def __repr__(self):
    return f"{round(self.value, 2)} {self.unit}"
  # This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
   
  
  def __str__(self):
    #This method returns the same value as __repr__(self).
    return Currency.__repr__(self)
    # return f"{round(self.value, 2)} {self.unit}"
  
  def __add__(self,other):
    #Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value.
    if type(other) == int or type(other) == float:
      other_value = (other * Currency.currencies[self.unit])
    else:
      other_value = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
    return Currency(other_value + self.value, self.unit)

  def __iadd__(self, other):
    return Currency.__add__(self,other)

  def __radd__(self,other):
    res = self + other
    if self.unit != 'USD':
      res.changeTo('USD')
    return res

  def __sub__(self,other):
      if type(other) == int or type(other) == float:
        other_value = other * Currency.currencies[self.unit]
      else:
        other_value = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
      return Currency(self.value - other_value, self.unit)

  def __isub__(self,other):
    return Currency.__sub__(self,other)

  def __rsub__(self,other):
    result = other - self.value
    result = Currency(result, self.unit)
    if self.unit != 'USD':
      result.changeTo('USD')
    return result
                
      
  

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
v3 = Currency(50000, "JPY")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 

print(v3 + v1)

>>> from sunpy.sun import constants
>>> print(constants.mass)
  Name   = Solar mass
  Value  = 1.9891e+30
  Error  = 5e+25
  Units  = kg
  Reference = Allen's Astrophysical Quantities 4th Ed.
# Verify the average density of the Sun and convert to cgs
>>> (constants.mass/constants.volume).cgs
<Quantity 1.40851154227 g / (cm3)>
# Search for the age of the Sun
>>> constants.find("age")
['age', 'average angular size', 'average density', 'average intensity']
>>> constants.value('age'), constants.unit('age')
(4600000000.0, Unit("yr"))
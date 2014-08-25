from sunpy.sun import constants
print(constants.mass)
# Verify the average density of the Sun and convert to cgs
(constants.mass/constants.volume).cgs
# Search for the age of the Sun
constants.find("age")
constants.value('age'), constants.unit('age')

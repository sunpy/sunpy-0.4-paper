>>> from sunpy import lightcurve
>>> from sunpy.time import TimeRange
>>> goes = lightcurve.GOESLightCurve.create(TimeRange("2011-06-07 06:00",
...                                         "2011-06-07 08:00"))
>>> goes.peek()
>>> print goes.data["B_FLUX"].max()
2.55542e-05
>>> print goes.data["B_FLUX"].idxmax()
2011-06-07 06:41:26
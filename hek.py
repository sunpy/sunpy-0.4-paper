>>> from sunpy.net import hek
>>> client = hek.HEKClient()
>>> tstart, tend = "2011/08/09 00:00:00", "2011/08/10 00:00:00"
>>> result = client.query(hek.attrs.Time(tstart, tend), 
...                       hek.attrs.EventType("FL")) # flares
>>> len(result)
52
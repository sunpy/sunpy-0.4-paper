>>> result = client.query(hek.attrs.Time(tstart, tend), 
...                       hek.attrs.EventType("FL"),
...                       hek.attrs.FRM.Name=="SSW Latest Events")
>>> len(result)
9
from sunpy.net import vso
client = vso.VSOClient()
tstart, tend = "2011/6/7 05:30", "2011/6/7 10:30"
lasco_query = client.query(vso.attrs.Time(tstart, tend),
                           vso.attrs.Instrument('lasco'))
lasco_query.num_records()
lasco_query.show() 
pathformat = "/data/{instrument}/{detector}/{file}.fits"
results = client.get(coronagraphs, path = pathformat)
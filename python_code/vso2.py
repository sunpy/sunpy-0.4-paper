condition = (vso.attrs.Detector("cor1") |
             vso.attrs.Wave(125, 135) |
             vso.attrs.Wave(165, 175) ) # in angstroms
advanced = client.query(vso.attrs.Time(tstart, tend), condition)
advanced.num_records()
advanced.show()
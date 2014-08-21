from sunpy.net import vso
from sunpy.database import Database
database = Database("sqlite:///")
database.download(
     vso.attrs.Time("2012-08-05", "2012-08-05 00:00:05"),
     vso.attrs.Instrument('AIA'))
len(database)
from sunpy.database.tables import display_entries
print display_entries(
     database,
     ["id", "observation_time_start", "wavemin", "wavemax"])
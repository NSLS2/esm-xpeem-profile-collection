import nslsii
from ophyd.signal import EpicsSignalBase


EpicsSignalBase.set_defaults(connection_timeout=10)
nslsii.configure_base(
    get_ipython().user_ns, 
    'xpeem',
    publish_documents_with_kafka=True,
    redis_url="xf21id1-xpeem-redis1.nsls2.bnl.gov",
    redis_port=6380,
    redis_ssl=True,
)

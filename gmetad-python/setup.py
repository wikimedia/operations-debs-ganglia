from distutils.core import setup
from glob import glob

setup(name='gmetad-python',
      version='3.5.0',
      description='Ganglia Meta daemon in Python',
      maintainer='Ganglia Development Team',
      maintainer_email='ganglia-developers@lists.sourceforge.net',
      url='http://ganglia.info',
      license='BSD',
      long_description=
'''Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This gmetad daemon aggregates monitoring data from several clusters
to form a monitoring grid. It also keeps metric history using rrdtool.

gmetad-python is a re-write of the original gmetad code (written in C)
with pluggable interface.  The RRD files, both the metric RRDs and summary
RRDs are being written by RRD plugins rather than directly from gmetad.
This provides the ability to plug in new metric storage modules to support
other types of storage mechanisms other than RRD and also the ability to
plug in any type of gmetad-level analysis.''',
      platforms='Many',
      packages=['Gmetad'],
      scripts=['gmetad.py'],
      data_files=[('/usr/local/etc', ['gmetad-python.conf']),
                  ('/usr/local/lib64/ganglia/python_modules/gmetad', glob('plugins/*.py'))] 
     )

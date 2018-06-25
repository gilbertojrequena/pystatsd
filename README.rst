======================
A Python statsd client
======================

statsd_ is a friendly front-end to Graphite_. This is a Python client
for the statsd daemon with influx tag support.

:Code:          https://github.com/gilbertojrequena/pystatsd-influx-tags
:License:       MIT; see LICENSE file
:Issues:        https://github.com/gilbertojrequena/pystatsd-influx-tags/issues

Quickly, to use:

.. code-block:: python

    >>> import statsd
    >>> c = statsd.StatsClient('localhost', 8125)
    >>> c.incr('foo', tags={'color': 'gray'})  # Increment the 'foo' counter.
    >>> c.timing('stats.timed', 320, tags={'player': 'two'})  # Record a 320ms 'stats.timed'.

You can also add a prefix to all your stats:

.. code-block:: python

    >>> import statsd
    >>> c = statsd.StatsClient('localhost', 8125, prefix='foo')
    >>> c.incr('bar', tags={'color': 'blue'})  # Will be 'foo.bar' in statsd/graphite.


Installing
==========

The easiest way to install statsd is with pip!

You can install from PyPI::

    $ pip install pystatsd-influx-tags

Or GitHub::

    $ pip install -e git+https://github.com/gilbertojrequena/pystatsd-influx-tags

Or from source::

    $ git clone https://github.com/gilbertojrequena/pystatsd-influx-tags
    $ cd pystatsd-influx-tags
    $ python setup.py install


Docs
====

There are lots of docs in the ``docs/`` directory and on ReadTheDocs_.


.. _statsd: https://github.com/etsy/statsd
.. _Graphite: https://graphite.readthedocs.io/
.. _ReadTheDocs: https://statsd.readthedocs.io/en/latest/index.html

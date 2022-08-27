import logging

logger = logging.getLogger('django')

def dump(obj):
  for attr in dir(obj):
    if not attr.startswith('__'):
      logger.info("%s: %r" % (attr, getattr(obj, attr)))


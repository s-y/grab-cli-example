
import csv
import logging
import urllib

from grab import Grab
from grab.spider import Spider, Task
#from grab.tools.logs import default_logging

#from database import db
import settings

from mongolog.handlers import MongoHandler
class project(Spider):

    def __init__(self, **kwargs):
        super(BaseSpider, self).__init__(**kwargs)
        grab_log = logging.getLogger('grab')
        grab_log.addHandler(MongoHandler.to(db=settings.MONGO_DB, collection='logs'))

    def task_generator(self):
        yield Task('initial', url='')

    def task_initial(self, grab, task):
        pass

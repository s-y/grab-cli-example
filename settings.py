# coding: utf-8

GRAB_SPIDER_MODULES = ['spider']
MONGO_DB = 'spider'
# GRAB_PROXY_LIST = {
#    'source': '/web/proxy.txt',
#    'source_type': 'text_file',
# }

GRAB_CACHE = {
        'backend': 'mongo',
        'database': '_cache',
#        'user': '',
#        'passwd': '',
}



GRAB_THREAD_NUMBER = 15

#GRAB_QUEUE = {
#    'backend': 'redis',
#     'database': '_queue',
#}

# GRAB_TASK_REFRESH_CACHE = {
# 'foo': True,
# }

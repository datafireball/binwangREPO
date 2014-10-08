# -*- coding: utf-8 -*-

BOT_NAME = 'projectgeturl'

SPIDER_MODULES = ['projectgeturl.spiders']
NEWSPIDER_MODULE = 'projectgeturl.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36'
LOG_LEVEL='INFO'
DOWNLOAD_DELAY = 0.5
ITEM_PIPELINES = {
    'projectgeturl.pipelines.JsonFilePipeline': 300,
}

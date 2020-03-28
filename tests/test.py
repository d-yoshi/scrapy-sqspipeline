from unittest import TestCase

from scrapy.settings import BaseSettings

from sqspipeline.pipelines import SQSPipeline


class TestPipelines(TestCase):
    def setUp(self):
        self.settings = BaseSettings({
            'SQSPIPELINE_QUEUE_URL': 'https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue',
        })

    def test_settings(self):
        pipeline = SQSPipeline(self.settings, None)
        self.assertEqual(pipeline.queue_url, 'https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue')

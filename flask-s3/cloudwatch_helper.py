import boto3
from botocore.config import Config
from config import S3_BUCKET, S3_KEY, S3_SECRET
def cloudwatch_metric(metric_name, unit):
    my_config = Config(
                            region_name = 'us-east-1'
                    )
    cw = boto3.client('cloudwatch', config=my_config)
    cw_response = response = cw.put_metric_data(
                                        Namespace='Parultest',
                                        MetricData=[
                                            {
                                                'MetricName': metric_name,
                                                'Value': 0.5,
                                                'Unit': unit
                                            }
                                        ]
                                    )
    return (cw_response)
from elasticapm.contrib.flask import ElasticAPM, LoggingHandler


def init_logger(app):
    ############ Elastic APM ###############
    app.config['ELASTIC_APM'] = {
        "SECRET_TOKEN": app.config["SECRET_TOKEN"],
        'SERVER_URL': app.config["SERVER_URL"],
        # # Set the service environment
        #'SECRET_TOKEN': 'gDqXAX3SJVGt5ttZrC',
        #'SERVER_URL': 'https://da7ae9774d3349a38d407d67cadd5706.apm.ap-south-1.aws.elastic-cloud.com:443',
        'ENVIRONMENT': app.config["APP_ENV"],
        'DEBUG': True,
        "SERVICE_NAME": "Movies-App"
    }

    apm = ElasticAPM(app=app, logging=True)

    handler = LoggingHandler(client=apm.client)
    app.logger.addHandler(handler)
    app.logger.info("Setting Elastic APM", exc_info=1)

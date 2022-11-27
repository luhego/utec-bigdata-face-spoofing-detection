from kafka.kafka_consumer import KafkaConsumer

LOGIN_ATTEMPT_TOPIC = "loginattempt"

kafka_consumer = KafkaConsumer()
kafka_consumer.consume(LOGIN_ATTEMPT_TOPIC)

from kafka.kafka_consumer import KafkaConsumer

FILTERED_TOPIC = "filtered"

kafka_consumer = KafkaConsumer()
kafka_consumer.consume(FILTERED_TOPIC)

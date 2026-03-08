---
name: rabbitmq-broker-get-guideline
description: Get the general best practices for deploying RabbitMQ on Amazon MQ.

            - guideline_name: It can take the following value:
                - rabbimq_broker_sizing_guide : this guide tells the customer what instance size to pick for production workload
                - rabbitmq_broker_setup_best_practices_guide: this guide tells the customer what are the best practices in setting up the RabbitMQ broker
                - rabbitmq_quorum_queue_migration_guide: this guide tells the customer how to migrate from classic mirror queue to quorum queue
                - rabbitmq_client_performance_optimization_guide: this guide tells the customer how to optimize their application to get peformance gain of using RabbitMQ
                - rabbitmq_check_broker_follow_best_practice_instructions: this contains instruction to check if a given RabbitMQ broker is following best practices
            
---

# Rabbitmq Broker Get Guideline

Get the general best practices for deploying RabbitMQ on Amazon MQ.

            - guideline_name: It can take the following value:
                - rabbimq_broker_sizing_guide : this guide tells the customer what instance size to pick for production workload
                - rabbitmq_broker_setup_best_practices_guide: this guide tells the customer what are the best practices in setting up the RabbitMQ broker
                - rabbitmq_quorum_queue_migration_guide: this guide tells the customer how to migrate from classic mirror queue to quorum queue
                - rabbitmq_client_performance_optimization_guide: this guide tells the customer how to optimize their application to get peformance gain of using RabbitMQ
                - rabbitmq_check_broker_follow_best_practice_instructions: this contains instruction to check if a given RabbitMQ broker is following best practices
            

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `guideline_name` | string | Yes |  |


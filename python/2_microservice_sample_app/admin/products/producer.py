import pika, json

params = pika.URLParameters('amqps://iovdhsjc:0unZ-1SMxPZBSFPR5VA1BM2ZlUb-dDmG@puffin.rmq2.cloudamqp.com/iovdhsjc')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
import pika, json
from main import Product, db

params = pika.URLParameters('amqps://iovdhsjc:0unZ-1SMxPZBSFPR5VA1BM2ZlUb-dDmG@puffin.rmq2.cloudamqp.com/iovdhsjc')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product Created')
    
    elif properties.content_type == 'product updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Product Updated')

    elif properties.content_type == 'product deleted':
        product = Product.query.get(data)
        product.title = data['title']
        product.image = data['image']
        db.session.delete()
        db.session.commit()
        print('Product Deleted')

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()
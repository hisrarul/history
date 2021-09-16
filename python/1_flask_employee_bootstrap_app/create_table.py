from App import db
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logging.info('##Logging Process Started')
db.create_all()
logging.info('Table created successfully!'
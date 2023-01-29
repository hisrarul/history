def s3_thumbnail_generator(event, context):
    data = "This was triggered by s3 bucket event!"
    print(data)
    return data
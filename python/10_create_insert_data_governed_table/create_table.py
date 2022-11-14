import awswrangler as wr
import boto3
 
my_session = boto3.Session(region_name="us-east-1", profile_name='dl')

wr.catalog.create_parquet_table(
    database = 'animals',
    table = 'animal_locations_governed',
    path = 's3://test-nov22-s3/animals/',
    columns_types = {'id' : 'int',
                      'animal' : 'string',
                      'longitude' : 'double',
                      'latitude' : 'double',
                      'date' : 'string'
    },
    compression = 'snappy',
    description = 'animal location table',
    columns_comments = {
        'id' : 'unique id of a animal',
        'animal' : 'Animal Name',
        'longitude' : 'x coordinate',
        'latitude' : 'y coordinate',
        'date' : 'date animal was located'
    },
    boto3_session = my_session,
    table_type = 'GOVERNED')

df = wr.s3.read_csv(path='s3://test-nov22-s3/data.csv', boto3_session = my_session)
filtered_data = df[df.date.isin(['2021-12-09'])]
transaction_1 = wr.lakeformation.start_transaction(read_only=False, boto3_session = my_session)

ds = wr.s3.to_parquet(
    df=filtered_data,
    path="s3://test-nov22-s3/animals/",
    dataset = True,
    compression = 'snappy',
    database = 'animals',
    table = 'animal_locations_governed',
    parameters = {"num_cols": str(len(df.columns)), "num_rows": str(len(df.index))},
    mode = 'overwrite',
    table_type = 'GOVERNED',
    transaction_id = transaction_1,
    boto3_session = my_session
)

## Commit Lake Formation Transaction
wr.lakeformation.commit_transaction(transaction_1, boto3_session = my_session)
transaction = wr.lakeformation.describe_transaction(transaction_1, boto3_session = my_session)
print(transaction)


## Insert additional data into a governed table
filtered_df2 = df[df.date.isin(['2021-12-10'])]
transaction_2 = wr.lakeformation.start_transaction(read_only=False, boto3_session = my_session)
ds = wr.s3.to_parquet(
    df=filtered_df2,
    path="s3://test-nov22-s3/animals/",
    dataset = True,
    compression = 'snappy',
    database = 'animals',
    table = 'animal_locations_governed',
    parameters = {"num_cols": str(len(df.columns)), "num_rows": str(len(df.index))},
    mode = 'append',
    table_type = 'GOVERNED',
    transaction_id = transaction_2,
    boto3_session = my_session
)
wr.lakeformation.commit_transaction(transaction_2, boto3_session = my_session)
transaction = wr.lakeformation.describe_transaction(transaction_2, boto3_session = my_session)


## Read from governed table
# export AWS_PROFILE="dl"
# export AWS_DEFAULT_REGION="us-east-1"

df3 = wr.lakeformation.read_sql_query(
    sql="SELECT * from animal_locations_governed;",
    database='animals'
)

df4 = wr.lakeformation.read_sql_query(
    sql=f"SELECT * from {'animal_locations_governed'};",
    database='animals',
    transaction_id = transaction_2
)
print(df4.shape[0])

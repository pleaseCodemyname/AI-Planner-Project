import boto3

# DynamoDB 연결
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')

# Table 생성
table = dynamodb.create_table(
    TableName='event',   # 테이블 이름을 문자열로 제공합니다.
    KeySchema=[
        {
            'AttributeName': 'title',   # 기본 키로 사용할 속성 이름을 지정합니다.
            'KeyType': 'HASH'           # 기본 키 유형을 지정합니다. 'HASH'는 해시 키를 의미합니다.
        },
        {
            'AttributeName': 'year',    # 두 번째 기본 키로 사용할 속성 이름을 지정합니다.
            'KeyType': 'RANGE'          # 두 번째 기본 키의 유형을 지정합니다. 'RANGE'는 범위 키를 의미합니다.
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'title',   # 속성 이름을 지정합니다.
            'AttributeType': 'S'        # 속성 유형을 지정합니다. 'S'는 문자열을 의미합니다.
        },
        {
            'AttributeName': 'year',
            'AttributeType': 'N'        # 'N'은 숫자를 의미합니다.
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,       # 읽기 용량 단위를 지정합니다.
        'WriteCapacityUnits': 5       # 쓰기 용량 단위를 지정합니다.
    }
)

# 테이블이 생성되기를 기다립니다.
table.meta.client.get_waiter('table_exists').wait(TableName='event')

# 데이터 삽입
table.put_item(
    Item={
        'title': '7월여행',
        'year': 2023,
        'month': 7,
        'start_day': 19,
        'end_day': 26,
        'goal': '태국여행',
        'place': '방콕&치앙마이',
        'content': '방콕을 간 후 치앙마이로 갈꺼에요'
    }
)

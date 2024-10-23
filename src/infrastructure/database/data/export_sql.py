import json

# JSONファイルを読み込む
with open('route_guide_db.json', 'r') as file:
    data = json.load(file)

# SQLインサート文を生成
sql_statements = []
for item in data:
    latitude = item['location']['latitude']
    longitude = item['location']['longitude']
    name = item['name'].replace("'", "''")  # シングルクォートをエスケープ
    sql = f"INSERT INTO route (latitude, longitude, name, created_at, updated_at) VALUES ({latitude}, {longitude}, '{name}', NOW(), NOW());"
    sql_statements.append(sql)

# SQLファイルに書き込む
with open('route_inserts.sql', 'w') as file:
    for statement in sql_statements:
        file.write(statement + '\n')
# ddd-and-grpc-sample-in-python
# Dev tips
## Update auto generated grpc files([Buf CLI](https://buf.build/docs/installation/) is required.)
```
buf generate
```
# Docker Settings
## Start up grpc server
```
docker compose down && docker compose up --build -d
```
## Run pytest
```
docker compose build && docker compose run pytest
```
## Run the ruby client for test
### One-time test(API execution)
```
docker compose build ruby_client && docker compose run ruby_client ruby -r "./route_guide_client.rb" -e "main '../../src/infrastructure/database/data/route_guide_db.json'"
```
### One-time test(File upload)
```
docker compose build ruby_client && docker compose run ruby_client ruby -r "./file_uploader_client.rb" -e "main '../../src/infrastructure/database/data/route_guide_db.json', '../../src/infrastructure/database/data/route_guide_db.json', '../../src/infrastructure/database/data/route_guide_db.json', '../../src/infrastructure/database/data/route_guide_db.json', '../../src/infrastructure/database/data/route_guide_db.json', '../../src/infrastructure/database/data/route_guide_db.json'"
```

### Load test
```
docker compose build ruby_client && docker compose run ruby_client ruby load_test_route_guide.rb
```
Outputs
```
    user     system      total        real
...
...
...
 20.859072  12.053508  32.912580 ( 49.079657)
```

# Local Settings
## Set up the environment
1. Install Python
1. Install Mysql
1. Create database and user on Mysql(Create DB_NAME and ${DB_NAME}_test databases.)
1. Copy .env.sample to .env and set values
1. Run `pip install --no-cache-dir -r requirements/base.txt`
1. Run `alembic upgrade head`

## Start up grpc server
```
export PYTHONPATH=.:src/auto_generated/grpc
python -m src.presentation.grpc.handler.server
```

## Run pytest
```
pip install --no-cache-dir -r requirements/test.txt
export PYTHONPATH=.:src/auto_generated/grpc
pytest
```

## Run the ruby client for test(Ruby 2.7.8 is required.)
### One-time test
```
cd tests/load
bundle install
ruby -r ./route_guide_client.rb -e "main '../../src/infrastructure/database/data/route_guide_db.json'"
```
### Load test
```
cd tests/load
bundle install
ruby load_test_route_guide.rb
```

Outputs
```
    user     system      total        real
...
...
...
 5.504243  10.177457  15.681700 ( 32.631951)
```

## The fllowing files are licensed under Apache-2.0
auth_sample.proto  
hellostreamingworld.proto  
helloworld.proto  
keyvaluestore.proto  
route_guide.proto  
route_guide_resources.py  
route_guide_server.py  
route_guide_db.json  
route_guide_client.rb  
route_guide_pb.rb  
route_guide_services_pb.rb

Impoted from [grpc/grpc](https://github.com/grpc/grpc) repository.
# ddd-and-grpc-sample-in-python

## Set up the environment
1. Install Python
1. Install Mysql
1. Create database on Mysql
1. Copy .env.sample to .env and set values
1. Run `pip install --no-cache-dir -r requirements/base.txt`
1. Run `alembic upgrade head`

## Start up the server
```
export PYTHONPATH=.
python -m src.presentation.grpc.handler.route_guide_server
```

## Run pytest
```
pip install --no-cache-dir -r requirements/test.txt
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
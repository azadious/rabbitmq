## How to start

### simple flow 
1. docker-compose up -d
2. docker exec -it producer python simple.py
3. docker attach consumer
4. docker exec producer python simple.py

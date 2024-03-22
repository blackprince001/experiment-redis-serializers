# setup redis with docker (redis-stack [contains redis and redinsights for visualizations])
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
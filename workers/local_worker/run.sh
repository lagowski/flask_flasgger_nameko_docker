#!/bin/bash

# Check if rabbit is up and running before starting the service.

is_ready() {
    eval "curl -I http://user:pass@rabbit:15672/api/vhosts"
}

i=0
while ! is_ready; do
    i=`expr $i + 1`
    if [ $i -ge 10 ]; then
        echo "$(date) - rabbit still not ready, giving up"
        exit 1
    fi
    echo "$(date) - waiting for rabbit to be ready"
    sleep 3
done

# Run Migrations

# alembic upgrade head

# Run Service

nameko run --config config.yml local_worker.service --backdoor 3000
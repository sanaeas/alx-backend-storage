#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient


def log_stats():
    """ Provide some stats about Nginx logs stored in MongoDB """
    logs_collection = MongoClient().logs.nginx

    logs = logs_collection.count_documents({})
    methods_count = {
            method: logs_collection.count_documents({"method": method})
            for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]
    }

    status_check = logs_collection.count_documents(
            {"method": "GET", "path": "/status"}
    )

    print(f"{logs} logs")
    print("Methods:")
    for method, count in methods_count.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()

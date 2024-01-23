#!/usr/bin/env python3
""" Script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def log_stats():
    """ Add the top 10 of the most present IPs in the collection nginx """
    logs_collection = MongoClient().logs.nginx

    logs = logs_collection.count_documents({})
    methods_count = {
            method: logs_collection.count_documents({"method": method})
            for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]
    }

    status_check = logs_collection.count_documents(
            {"method": "GET", "path": "/status"}
    )

    ips_count = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    top_ips = logs_collection.aggregate(ips_count)

    print(f"{logs} logs")
    print("Methods:")
    for method, count in methods_count.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")

    print("IPs:")
    for ip_info in top_ips:
        print(f"\t{ip_info['_id']}: {ip_info['count']}")


if __name__ == "__main__":
    log_stats()

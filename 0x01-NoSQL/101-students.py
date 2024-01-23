#!/usr/bin/env python3
""" top_students function """


def top_students(mongo_collection):
    """ Return all students sorted by average score """
    aggregation = [
        {
            '$project': {
                'name': 1,
                'topics': 1,
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]

    sorted_students = mongo_collection.aggregate(aggregation)

    return sorted_students

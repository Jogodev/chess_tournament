"""function to have datetime to string"""
from datetime import datetime


def get_datetime():
    """Get the date and the hour"""
    return str(datetime.now())[:18]

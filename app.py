
import json
import numpy as np
import logging
from datetime import datetime

from flask import Flask, Response
from flask import request

#use logger to debug
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

application = Flask(__name__)

def log_and_extract_input(method, path_params=None):

    path = request.path
    args = dict(request.args)
    data = None
    headers = dict(request.headers)
    method = request.method

    try:
        if request.data is not None:
            data = request.json
        else:
            data = None
    except Exception as e:
        data = "You sent something but I could not get JSON out of it."

    log_message = str(datetime.now()) + ": Method " + method

    inputs =  {
        "path": path,
        "method": method,
        "path_params": path_params,
        "query_params": args,
        "headers": headers,
        "body": data
        }

    log_message += " received: \n" + json.dumps(inputs, indent=2)
    logger.debug(log_message)

    return inputs

def log_response(method, status, data, txt):

    msg = {
        "method": method,
        "status": status,
        "txt": txt,
        "data": data
    }

    logger.debug(str(datetime.now()) + ": \n" + json.dumps(msg, indent=2, default=str))

logger.debug("__name__ = " + str(__name__))


# the following is the math APIs
@application.route("/min", methods=["POST"])
def get_min():

    req_info = log_and_extract_input("/min")

    try:
        if req_info["method"] == "POST":
            if "nums" not in req_info["body"] or "quant" not in req_info["body"]:
                return Response("Invalid Input", status=404, content_type="text/plain")

            nums = req_info["body"]["nums"]
            quant = req_info["body"]["quant"]

            if quant != len(nums) or len(nums) == 0:
                return Response("Invalid Input", status=404, content_type="text/plain")

            Min = float("INF")
            for i in nums:
                Min = min(Min, i)
            res = "The min number is " + str(Min)
            rsp = Response(json.dumps(res), status=200, content_type="application/json")

        else:
            rsp = Response("NOT IMPLEMENTED", status=501, content_type="text/plain")

    except Exception as e:
        rsp = Response("Bad Request", status=418, content_type="text/plain")
        logger.error("Exception=" + e)

    return rsp


@application.route("/max", methods=["POST"])
def get_max():
    req_info = log_and_extract_input("/min")

    try:
        if req_info["method"] == "POST":
            if "nums" not in req_info["body"] or "quant" not in req_info["body"]:
                return Response("Invalid Input", status=404, content_type="text/plain")

            nums = req_info["body"]["nums"]
            quant = req_info["body"]["quant"]

            if quant != len(nums) or len(nums) == 0:
                return Response("Invalid Input", status=404, content_type="text/plain")

            Max = float("-INF")
            for i in nums:
                Max = max(Max, i)
            res = "The max number is " + str(Max)
            rsp = Response(json.dumps(res), status=200, content_type="application/json")

        else:
            rsp = Response("NOT IMPLEMENTED", status=501, content_type="text/plain")

    except Exception as e:
        rsp = Response("Bad Request", status=418, content_type="text/plain")
        logger.error("Exception=" + e)

    return rsp


@application.route("/avg", methods=["POST"])
def get_avg():
    req_info = log_and_extract_input("/avg")

    try:
        if req_info["method"] == "POST":

            if req_info["body"]["nums"] is None:
                return Response("Invalid Input", status=404, content_type="text/plain")

            nums = req_info["body"]["nums"]

            cnt = len(nums)
            sum = 0
            for i in nums:
                sum += i

            res = "The average is " + str(sum / cnt)
            rsp = Response(json.dumps(res), status=200, content_type="application/json")

        else:
            rsp = Response("NOT IMPLEMENTED", status=501, content_type="text/plain")

    except Exception as e:
        rsp = Response("Bad Request", status=418, content_type="text/plain")
        logger.error("Exception=" + e)

    return rsp


@application.route("/median", methods=["POST"])
def get_median():
    req_info = log_and_extract_input("/median")

    try:
        if req_info["method"] == "POST":
            if req_info["body"]["nums"] is None:
                return Response("Invalid Input", status=404, content_type="text/plain")

            nums = req_info["body"]["nums"]

            if len(nums) == 0:
                return Response("Invalid Input", status=404, content_type="text/plain")

            n = len(nums)
            nums.sort()

            if n % 2 == 0:
                median1 = nums[n // 2]
                median2 = nums[n // 2 - 1]
                median = (median1 + median2) / 2
            else:
                median = nums[n // 2]

            res = "The median is " + str(median)
            rsp = Response(json.dumps(res), status=200, content_type="application/json")

        else:
            rsp = Response("NOT IMPLEMENTED", status=501, content_type="text/plain")

    except Exception as e:
        rsp = Response("Bad Request", status=418, content_type="text/plain")
        logger.error("Exception=" + e)

    return rsp


@application.route("/percentile", methods=["POST"])
def get_percentile():
    req_info = log_and_extract_input("/percentile")

    try:
        if req_info["method"] == "POST":
            if "nums" not in req_info["body"] or "quant" not in req_info["body"]:
                return Response("Invalid Input", status=404, content_type="text/plain")

            nums = req_info["body"]["nums"]
            quant = req_info["body"]["quant"]

            if len(nums) == 0:
                return Response("Invalid Input", status=404, content_type="text/plain")

            nums.sort()
            per = np.percentile(nums, quant)

            res = "The " + str(quant) + " percentile is " + str(per)

            rsp = Response(json.dumps(res), status=200, content_type="application/json")

        else:
            rsp = Response("NOT IMPLEMENTED", status=501, content_type="text/plain")

    except Exception as e:
        rsp = Response("Bad Request", status=418, content_type="text/plain")
        logger.error("Exception=" + e)

    return rsp


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run("localhost", port=8010)

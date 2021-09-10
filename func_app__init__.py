import logging

import azure.functions as func
from datetime import datetime
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
            if req_body.get('function'):
                function = req_body.get('function')
                if function == 'datetime':
                    return func.HttpResponse(
                        json.dumps({"function": function, "result": datetime.now().strftime("%Y-%m-%d %H:%M")}),
                        mimetype="application/json",
                        status_code=200
                    )
                elif function == 'date':
                    return func.HttpResponse(
                        json.dumps({"function": function, "result": datetime.now().strftime("%Y-%m-%d")}),
                        mimetype="application/json",
                        status_code=200
                    )
            else:
                return func.HttpResponse(
                    status_code=404
                )
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

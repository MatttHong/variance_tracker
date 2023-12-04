import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        if req.method == "GET":
            # Handle GET request
            message = "This is a GET request."
        elif req.method == "POST":
            # Handle POST request
            req_body = req.get_json()
            message = f"This is a POST request with data: {req_body}"
        else:
            return func.HttpResponse(
                "Method not allowed",
                status_code=405
            )

        return func.HttpResponse(
            message,
            mimetype="text/plain",
            status_code=200
        )
    except Exception as e:
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

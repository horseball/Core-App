import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name') or req.get_json().get('name')
    country = req.params.get('country') or req.get_json().get('country')

    if name:
        # Insert to Dataverse DB
        # league = orm.entity("leagues")
        # league.create({"name": name, "country": country})

        return func.HttpResponse(f"League successfully created. Name : {name}, country : {country}.")
    else:
        return func.HttpResponse(
             "Params are missing. Please include at least a 'name' to create a league.",
             status_code=422
        )

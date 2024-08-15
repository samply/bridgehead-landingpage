from flask import Flask, render_template, url_for
from os import environ
from importlib import import_module
from common import ServiceType

app = Flask(__name__)


def prepare_vars(required_vars):
    missing_vars = [var for var in required_vars if not environ.get(var)]
    if missing_vars:
        raise Exception(f"Please define variables: {', '.join(missing_vars)}")

    for var in required_vars:
        globals()[var] = environ.get(var)


prepare_vars(["PROJECT", "SITE_NAME", "HOST", "ENVIRONMENT"])
project = import_module(f"projects.{PROJECT.lower()}")


@app.route("/")
def page():
    return render_template('page.template',
                           site_name=SITE_NAME,
                           ENVIRONMENT=environ.get("ENVIRONMENT"),
                           thishostname=HOST,
                           project=PROJECT,
                           projectname=project.projectname_friendly,
                           logo=url_for("static", filename="%s.svg" % (PROJECT)),
                           centralservices=[service for service in project.services if
                                            service.type == ServiceType.CENTRAL],
                           localservices=[service for service in project.services if
                                          service.type == ServiceType.BRIDGEHEAD])


if __name__ == '__main__':
    app.run()

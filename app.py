from os import environ
from flask import Flask, render_template, url_for
from os import environ
from importlib import import_module
from common import ServiceType

app = Flask(__name__)

def prepare_vars(vars):
    missingvars = []
    for var in vars:
        env = environ.get(var)
        if env == None:
            missingvars.append(var)
        globals()[var] = environ.get(var)

    if(len(missingvars) > 0):
        raise Exception("Please define variables: %s" % (", ".join(missingvars)) )

@app.route("/")
def page():
    return render_template('page.template',
        site_name=SITE_NAME,
        thishostname=HOST,
        project=PROJECT,
        projectname=project.projectname_friendly,
        logo=url_for("static", filename="%s.svg" % (PROJECT)),
        centralservices=[service for service in project.services if service.type==ServiceType.CENTRAL],
        localservices=[service for service in project.services if service.type==ServiceType.BRIDGEHEAD])

prepare_vars(["PROJECT", "SITE_NAME", "HOST"])

project = import_module("projects.%s" % (PROJECT.lower()) )

if __name__ == '__main__':
    app.run()
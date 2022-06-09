from common import Service, ServiceGroup, ServiceType

projectname_friendly = "Clinical Communication Platform"

services = [
    Service(ServiceGroup.PSEUDONYMIZATION, "Zentraler Kontrollnummernerzeuger", "https://dktk-kne.kgu.de", ServiceType.CENTRAL),
    Service(ServiceGroup.PSEUDONYMIZATION, "Zentrale Patientenliste", "https://patientlist.ccp-it.dktk.dkfz.de", ServiceType.CENTRAL),
    Service(ServiceGroup.SEARCH, "Zentrale Suche", "https://centralsearch.ccp-it.dktk.dkfz.de", ServiceType.CENTRAL),
    Service(ServiceGroup.SEARCH, "Dezentrale Suche", "https://decentralsearch.ccp-it.dktk.dkfz.de", ServiceType.CENTRAL),
    Service(ServiceGroup.OPERATIONS, "Deployment-Server", "https://deployment.ccp-it.dktk.dkfz.de", ServiceType.CENTRAL),
    Service(ServiceGroup.OPERATIONS, "Zentrales Monitoring", "https://monitor.vmitro.de/icingaweb2/", ServiceType.CENTRAL),
    Service(ServiceGroup.OPERATIONS, "Reverse Proxy (Traefik)", "https://<THISHOST>/dashboard/", ServiceType.BRIDGEHEAD),
    Service(ServiceGroup.SEARCH, "Connector(Teiler)", "https://<THISHOST>/ccp-connector", ServiceType.BRIDGEHEAD),
    Service(ServiceGroup.PERSISTENCE, "Samply Store", "https://<THISHOST>/ccp-localdatamanagement", ServiceType.BRIDGEHEAD),
    Service(ServiceGroup.SEARCH, "ID-Manager", "https://<THISHOST>/idmanager", ServiceType.BRIDGEHEAD)
]

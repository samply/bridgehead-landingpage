from common import Service, ServiceGroup, ServiceType

projectname_friendly = "nNGM"

services = [
    Service(ServiceGroup.OPERATIONS, "Zentrales Monitoring", "https://monitoring.verbis.dkfz.de/icingaweb2/dashboard", ServiceType.CENTRAL),
    Service(ServiceGroup.OPERATIONS, "Reverse Proxy (Traefik)", "https://<THISHOST>/dashboard/", ServiceType.BRIDGEHEAD),
    Service(ServiceGroup.PERSISTENCE, "FHIR-Server (Blaze)", "https://<THISHOST>/nngm-localdatamanagement/fhir", ServiceType.BRIDGEHEAD)
]

from common import Service, ServiceGroup, ServiceType

projectname_friendly = "Innovative Therapies for Children with Cancer"

services = [
    # Service(ServiceGroup.SEARCH, "Explorer", "https://explorer.hector.dkfz.de", ServiceType.CENTRAL),
    # Service(ServiceGroup.OPERATIONS, "Zentrales Monitoring", "https://monitoring.verbis.dkfz.de/icingaweb2/dashboard", ServiceType.CENTRAL),
    Service(ServiceGroup.OPERATIONS, "Reverse Proxy (Traefik)", "https://<THISHOST>/dashboard/", ServiceType.BRIDGEHEAD),
    Service(ServiceGroup.PERSISTENCE, "FHIR-Server (Blaze)", "https://<THISHOST>/itcc-localdatamanagement/fhir", ServiceType.BRIDGEHEAD)
]

from common import Service, ServiceGroup, ServiceType

projectname_friendly = "BBMRI-ERIC/GBN"

services = [
    Service(ServiceGroup.SEARCH, "Sample Locator (bbmri.de)", "https://samplelocator.bbmri.de", ServiceType.CENTRAL),
    Service(ServiceGroup.SEARCH, "Sample Locator (BBMRI-ERIC)", "https://locator.bbmri-eric.eu", ServiceType.CENTRAL),
    Service(ServiceGroup.NEGOTIATION, "Negotiator", "https://negotiator.bbmri-eric.eu", ServiceType.CENTRAL),
    Service(ServiceGroup.OPERATIONS, "Zentrales Monitoring", "https://monitoring.verbis.dkfz.de/icingaweb2/dashboard", ServiceType.CENTRAL),
    Service(ServiceGroup.OPERATIONS, "Reverse Proxy (Traefik)", "https://<THISHOST>/dashboard/", ServiceType.BRIDGEHEAD),
    Service(ServiceGroup.PERSISTENCE, "FHIR-Server (Blaze)", "https://<THISHOST>/bbmri-localdatamanagement/fhir", ServiceType.BRIDGEHEAD),
]

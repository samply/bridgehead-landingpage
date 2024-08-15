from common import Service, ServiceGroup, ServiceType

projectname_friendly = "Minimal"

services = [
    Service(ServiceGroup.OPERATIONS, "Reverse Proxy (Traefik)", "https://<THISHOST>/dashboard/",
            ServiceType.BRIDGEHEAD),
]

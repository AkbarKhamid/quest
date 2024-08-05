k8s_yaml(['k8s/gateway.yaml', 'k8s/user-auth-service.yaml', 'k8s/quest-catalog-service.yaml', 'k8s/quest-processing-service.yaml'])

docker_build('user-auth-service', './users')
docker_build('quest-catalog-service', './quest_catalog')
docker_build('quest-processing-service', './quest_processing')
docker_build('gateway', './gateway')

k8s_resource('user-auth-service', port_forwards='8000')
k8s_resource('quest-catalog-service', port_forwards='8001')
k8s_resource('quest-processing-service', port_forwards='8002')
k8s_resource('gateway', port_forwards='8080')

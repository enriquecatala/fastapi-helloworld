<div>
    <a href="https://github.com/sponsors/enriquecatala"><img src="https://img.shields.io/badge/GitHub_Sponsors--_.svg?style=flat-square&logo=github&logoColor=EA4AAA" alt="GitHub Sponsors"></a>
    <a href="https://enriquecatala.com"><img src="https://img.shields.io/website?down_color=red&down_message=down&label=enriquecatala.com&up_color=46C018&url=https%3A%2F%2Fenriquecatala.com&style=flat-square" alt="Data Engineering with Enrique Catalá"></a>
    <a href="https://www.linkedin.com/in/enriquecatala"><img src="https://img.shields.io/badge/LinkedIn--_.svg?style=flat-square&logo=linkedin" alt="LinkedIn Enrique Catalá Bañuls"></a>
    <a href="https://twitter.com/enriquecatala"><img src="https://img.shields.io/twitter/follow/enriquecatala?color=blue&label=twitter&style=flat-square" alt="Twitter @enriquecatala"></a>
    <a href="https://youtube.com/enriquecatala"><img src="https://raw.githubusercontent.com/enriquecatala/enriquecatala/master/img/youtube.png" alt="Data Engineering: Canal youtube de Enrique Catalá" height=20></a>
</div>

<a href="https://mvp.microsoft.com/es-es/PublicProfile/5000312?fullName=Enrique%20Catala"><img src="https://raw.githubusercontent.com/enriquecatala/enriquecatala/master/img/MVP_Logo_horizontal.png" alt="Microsoft DataPlatform MVP Enrique Catalá"></a>
# fastapi-helloworld
Very basic API rest for kubernetes demo purposes

>NOTE: This image **has been pushed to https://hub.docker.com/r/enriquecatala/fastapi-helloworld**

## Test

Check your api documentation
1. Go to http://localhost:5000/docs

Test your methods: 
Navigate to IP:PORT(/one/hello | /two/hello)
For example: 
1. Go to http://localhost:5000/one/hello



## Setup the container

No special setup required, but the container will return the _HELLOWORLD_ENV_ in the output call. You can edit that variable to check values

### Kubernetes
If you wanto to deploy, [here](kubernetes-deployment.yaml) you have a deployment example. Please change this accordingly:

```yaml
    env:
        - name: HELLOWORLD_ENV
          value: "Pon aqui lo que te de la gana :)"
```

### Docker
In case you are using docker-compose.yml

```yaml
    environment:
      - HELLOWORLD_ENV=Pon aqui lo que te de la gana :)
```

## Create your own container
### Build container

`docker-compose build`

### Run the container locally

`docker-compose up`

## CI/CD with GitHub Actions

Just push :)

### Setup

First of all, you need to create a new repository in GitHub. Then you need to create a service principal in Azure. For example:

```bash
az ad sp create-for-rbac --name "github-actions-financeai-dev" --role contributor --scopes "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>" --sdk-auth
```

With the output, just create this Azure credential for GitHub Actions:
```json
{
  "clientId": "<client id>",
  "clientSecret": "<client secret>",
  "subscriptionId": "<subscription id>",
  "tenantId": "<tenant id>",
  "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
  "resourceManagerEndpointUrl": "https://management.azure.com/",
  "activeDirectoryGraphResourceId": "https://graph.windows.net/",
  "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
  "galleryEndpointUrl": "https://gallery.azure.com/",
  "managementEndpointUrl": "https://management.core.windows.net/"
}

```

>NOTE: For more information please read [this](https://github.com/Azure/aks-set-context/tree/releases/v1) and [this](https://docs.microsoft.com/en-us/azure/aks/kubernetes-action)
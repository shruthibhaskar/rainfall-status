Folder k8:

Contains the kubernetes pod, configmap yaml files specific to rainfall service.
pod.yml - contains instructions to run rainfall status check python application.
configmap.yml - contains the configuration details of location and api_url.

Folder main:
Dockerfile - Application is built on pythin alpine image, dockerfile contains instruction to run python flask application.

app:
main.py - Contains python application to fetch rainfall status.
api_url: https://api.data.gov.sg/v1/environment/rainfall (to check live rainfall status)
location: <any valid location>

Setting environment variable with below commands in Linux/mac system:
export API_URL="https://api.data.gov.sg/v1/environment/rainfall"
export LOCATION="Marina Gardens Drive"

functions.py - Contains definitions to fetch the rainfall status.

test:
api_raining.json - Contains the test data of raining status taken when raining in Upper Changi Road North location.
test_functions.py - Contains all the functions that are used to call and test scenarios.
test.py - Contains scenarios to check the Raining, Not Raining, Station id and Env variable tests.

logs:
tdd_logs - contains the tdd test scenario logs

Folder others:

Contains all the trials tried for api implementation in python.

Assumptions:

Flask : Using python flask to run webservice.
CSV : comma separated values.
Docker registry : using personal public dockerhub to store rainfall status check service docker images.
eg image: 104466/rainfall_flask_env:latest.

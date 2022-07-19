Folder main: <br />
`Dockerfile` - Application is built on pythin alpine image, dockerfile contains instruction to run python flask application. <br />

app: <br />
`main.py` - Contains python application to fetch rainfall status. <br />
api_url: https://api.data.gov.sg/v1/environment/rainfall (to check live rainfall status) <br />
location: "any valid location" <br />

Setting environment variable with below commands in Linux/mac system: <br />
`export API_URL="https://api.data.gov.sg/v1/environment/rainfall"` <br />
`export LOCATION="Marina Gardens Drive"` <br />

`functions.py` - Contains definitions to fetch the rainfall status. <br />

test: <br />
`api_raining.json` - Contains the test data of raining status taken when raining in Upper Changi Road North location. <br />
`test_functions.py` - Contains all the functions that are used to call and test scenarios. <br />
`test.py` - Contains scenarios to check the Raining, Not Raining, Station id and Env variable tests. <br />

logs: <br />
`tdd_logs` - contains the tdd test scenario logs<br />

Folder k8: <br />

Contains the kubernetes pod, configmap yaml files specific to rainfall service. <br />
`pod.yml` - contains instructions to run rainfall status check python application. <br />
`configmap.yml` - contains the configuration details of location and api_url. <br />

Folder others: <br />

Contains all the trials tried for api implementation in python. <br />

Assumptions: <br />

Flask : Using python flask to run webservice.<br />
CSV : comma separated values.<br />
Docker registry : using personal public dockerhub to store rainfall status check service docker images.<br />
eg image: 104466/rainfall_flask_env:latest.<br />

# Hello-world-Python

Command to Run in local : ```Python app/app.py```

Command to build Docker : ```make build```

Command to Run Docker Container: ```make run```

Command to build & Run in docker : ```make app```

Application runs in port 8080 

Paths :

1) /   `#home page`
2) /healthz `#health check page`


3. What other information would you add to health endpoint json object in step 2? Explain what would be the use case
for that extra information?
```
Build/Docker/Commit ID: Devops can use this to identify the unique artifact

SRE Contact: Contact information of the SRE if clients want to contact the Admin: ( this should only be displayed if the status is "down" th implemetion does not cover this scenario)

Environment: Identifies where the application is up.

Java_Opts/Configuration: To check if the heap information or Env variables passed for the environment is proper.
```

5. How would you automate the build/test/deploy process for this application? (a verbal answer is enough. installation of CICD is bonus, not required)
   - What branching strategy would you use for development?
   `Feature-based/Story-based branching Strategy are preferable, but Branching Strategies needs to be decided with consense from Devops and development team for a smooth release process`
   - What CICD tool/service would you use?
   `Since the application is Dockerized, the options are many, from Simple group of servers & Load Balancers to AKS/GKS/EKS/ECS/Kubenetes to using tools like CFT and Terraform to create those infrastructure depending on the apps importance and availablity criteria. For this app and single server with public access is enough` 
   - What stages would you have in the CICD pipeline?
   `Depending on the tools the organizations use the stages will differ, some organizations run code ananlysis in Git and Artifactory by integrating test tools to them. In situation like these the no of stages in pipeline will cut down. but the main stages of a pipeline are Checkout, Build, Test, Authorize(if env is prod) and Deploy.`
   - What would be the purpose of each stage in CICD pipeline.
   ```
   Checkout : to bring the code to build workspace.
   Build : To package the code to a deployable format like jar, war, zip, container, etc
   Test : This can be a single stage or multiple stages depending on the architecture of the pipeline/deployment process. The fucntionality/performance of the application can be tested in this stage through automated test scripts ```
   Authorize: This is a Stage required for the product owner/manager to authorize the deployment to Production. The concerned person can review test reports and code qualityreport and decide to deploy or forefeit.
   Deploy: Deploy the application to Environment. depending on mutable or immutable infrastructure this stage may also have infra creation
   ```
# dockerhub URLs:
## exercises and homeworks:
session-1: https://hub.docker.com/repository/docker/kentregs/exercise-1  
session-2: https://hub.docker.com/repository/docker/kentregs/deploy
- version 12: exer1
- version 15: exer2
## final-project:
- final-train: https://hub.docker.com/repository/docker/kentregs/final-train
- final-deploy: https://hub.docker.com/repository/docker/kentregs/final-deploy
---
# Final Project Quickstart Guide
## Set-up Docker 
Pull the latest version of the final-deploy container from dockerhub.
```
docker pull kentregs/final-deploy
```
Run the container and bind port 5000 to the TCP port 8080 of the host machine. 
```
docker run -p 8080:5000 kentregs/final-deploy
```
Test if the endpoint is working as expected.

![](https://i.imgur.com/GdnlHqW.png)

---

## Set-up Postman 
**Before proceeding to the next steps, the Postman desktop application needs to be installed.**  

Verify the location of your Postman agent's working directory and store the images that you will be using in your request body there. 

![](https://i.imgur.com/seIQCIo.gif)

Upload the images to the working directory and prepare the POST request body that will be sent to the /invocations endpoint.  

**Note: The bee and wasp images are in 'mynt-cadetship-docker-repo/final-project/data/'**

![](https://i.imgur.com/mCQlH2q.png)

Select **form-data** and fill in the keys with **img_1** to **img_10**. Afterwards, set the file type to **File** and upload the images that you stored in the **Postman working directory** in the previous step in the **VALUE** column.  

The end result should look like so:

![](https://i.imgur.com/0Uctzxf.png)

Finally, send the request and wait for the response to be received.  

### Demo:

![](https://i.imgur.com/xHTUeZV.gif)

### Output in terminal once request is received:

![](https://i.imgur.com/VPmo1zO.png)

### Response:
![](https://i.imgur.com/OWdkF4K.png)

---

# Additional notes:
The model training was performed in a GPU-accelerated Kaggle notebook and may be seen in **'mynt-cadetship-docker-repo/final-project/model training files/bee-vs-wasp-ntbk.ipynb'**
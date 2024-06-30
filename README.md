# siwp2005-final-project

## Setup Instructions

### Enable WSL

- Open PowerShell as Administrator
- Enable WSL feature
    ```
      dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

    ```
- Enable Virtual Machine
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

    ```
![image](https://hackmd.io/_uploads/Hkps9rsV0.png)
- Restart your computer. 
    > you need to restart your windows to see the effect whether you can run wsl on your windows
    
- Validate your wsl
    ```
    wsl --version
    ```
![image](https://hackmd.io/_uploads/HkL7oHiVC.png)
- Set WSL 2 as default version
    ```
    wsl --set-default-version 2
    ```
![image](https://hackmd.io/_uploads/SyeviHsVR.png)


### Using Ubuntu on WSL 2

- Check which linux distro are availables on your windows 
```
wsl --list --online
```
![image](https://hackmd.io/_uploads/SkS3aHs40.png)

- Install ubuntu
```
wsl.exe --install -d <DistroName>
```
Please change `<DistroName>` with the ubuntu distro list on your windows, we will use `Ubuntu-22.04`
`wsl.exe --install -d Ubuntu-22.04` then follow the instruction set ubuntu username and password

- Update the list of available package
```
sudo apt-get update
```

- Create a directory for the project and clone the repository
```
mkdir ukkw
cd ukkw/
git clone https://github.com/hendrikTpl/siwp2005-final-project.git
cd siwp2005-final-project/
```

### Enable & Setup Docker

- Validate your docker
```
docker --version
```
![Screenshot 2024-06-30 162417](https://hackmd.io/_uploads/BkuYEj080.png)

- Install docker (if you haven't downloaded it yet)
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

- Validate your docker again
```
docker --version
docker compose --version
```

- Setup environment
```
cp env.example .env
```

![Screenshot 2024-06-30 165048](https://hackmd.io/_uploads/By959s0IC.png)

- Start and build Docker containers
```
sudo docker compose -f docker-compose.yaml up --build -d
```

- List all running Docker containers
```
sudo docker ps
```

![Screenshot 2024-06-30 165211](https://hackmd.io/_uploads/S1r1joRLA.png)

- To check specific container
```
sudo docker ps --filter name="name of the container" 
```

- To stop service
```
sudo docker compose -f docker-compose.yaml down
```


## Project Description
In the context of UKRIDA's Portal System, which includes various sub-systems such as course management, bulletin management, billing management, academin management, softskill management, it is essential to develop each sub-system as independent micro-services. This approach minimizes downtime by ensuring that if one micro-service fails, it does not impact the other subsystems. This final project aims to design a backend micro-service focusing on containerized development. The backend will be built using Flask to implement REST APIs and will use MongoDB as the database. The primary goal is to create a service with well-defined endpoints that can be seamlessly integrated with a user interface (UI). This project will emphasize the importance of developing each sub-system as a micro-service rather than a monolithic service to enhance reliability and maintainability.
## API Documentation

**Version**: 1.0.11
**API Base URL**: http://127.0.0.1:5003/api/v1

This API provides backend services using Flask and MongoDB for managing users, courses, and bulletins in the UKRIDA Portal System.

### Server configuration
- **Protocol**: `http`
- **Server IP**: `127.0.0.1`
- **Port**: `5003`

### Endpoints
- #### User Endpoints
    - **Register User**
        - Method: POST
        - Endpoint: `/user`
        - Description: Registers a new user
    - **Login Endpoint**
        - Method: POST
        - Endpoint: `/login`
        - Description: Authenticates a user and provides a login token.
    
- #### Courses Endpoints
    - **Add Course**
        - Method: POST
        - Endpoint: `/courses`
        - Description: Adds a new course.
    - **Get All Courses**
        - Method: GET
        - Endpoint: `/courses/{course_id}`
        - Description: Retrieves a list of all courses.
    - **Get Course by ID**
        - Method: GET
        - Endpoint: `/courses/{course_id}`
        - Description: Retrieves details of a specific course by its ID.
    - **Delete Course by ID**
        - Method: DELETE
        - Endpoint: `/courses/{course_id}`
        - Description: Deletes a course by its ID.
    - **Edit Course by ID**
        - Method: PUT
        - Endpoint: `/courses/{course_id}`
        - Description: Edits the details of a specific course by its ID.

- #### Bulletin Endpoints
  - **Add Bulletin**
    - Method: POST
    - Endpoint: `/bulletin`
    - Description: Adds a new bulletin.
  - **Get All Bulletins**
    - Method: GET
    - Endpoint: `/bulletin`
    - Description: Retrieves a list of all bulletins.
  - **Get Bulletin by ID**
    - Method: GET
    - Endpoint: `/bulletin/{bulletin_id}`
    - Description: Retrieves details of a specific bulletin by its ID.
  - **Delete Bulletin by ID**
    - Method: DELETE
    - Endpoint: `/bulletin/{bulletin_id}`
    - Description: Deletes a bulletin by its ID.
  - **Edit Bulletin by ID**
    - Method: PUT
    - Endpoint: `/bulletin/{bulletin_id}`
    - Description: Edits the details of a specific bulletin by its ID.

- #### Billing Endpoints
  - **Add Billing**
    - Method: POST
    - Endpoint: `/billing`
    - Description: Adds a new billing.
  - **Get All Billings**
    - Method: GET
    - Endpoint: `/billing`
    - Description: Retrieves a list of all billings.
  - **Get Billing by ID**
    - Method: GET
    - Endpoint: `/billing/{billing_id}`
    - Description: Retrieves details of a specific billing by its ID.
  - **Delete Billing by ID**
    - Method: DELETE
    - Endpoint: `/billing/{billing_id}`
    - Description: Deletes a billing by its ID.
  - **Edit Billing by ID**
    - Method: PUT
    - Endpoint: `/billing/{billing_id}`
    - Description: Edits the details of a specific billing by its ID.


- #### Academic Endpoints
  - **Add Academic**
    - Method: POST
    - Endpoint: `/academic`
    - Description: Adds a new academic.
  - **Get All Academics**
    - Method: GET
    - Endpoint: `/academic`
    - Description: Retrieves a list of all academics.
  - **Get Academic by ID**
    - Method: GET
    - Endpoint: `/academic/{academic_id}`
    - Description: Retrieves details of a specific academic by its ID.
  - **Delete Academic by ID**
    - Method: DELETE
    - Endpoint: `/academic/{academic_id}`
    - Description: Deletes an academic by its ID.
  - **Edit Academic by ID**
    - Method: PUT
    - Endpoint: `/academic/{academic_id}`
    - Description: Edits the details of a specific academic by its ID.


#### Softskill Endpoints
  - **Add Softskill**
    - Method: POST
    - Endpoint: `/softskill`
    - Description: Adds a new softskill.
  - **Get All Softskill**
    - Method: GET
    - Endpoint: `/softskill`
    - Description: Retrieves a list of all softskills.
  - **Get Softskill by ID**
    - Method: GET
    - Endpoint: `/softskill/{softskill_id}`
    - Description: Retrieves details of a specific softskill by its ID.
  - **Delete Softskill by ID**
    - Method: DELETE
    - Endpoint: `/softskill/{softskill_id}`
    - Description: Deletes an softskill by its ID.
  - **Edit Softskill by ID**
    - Method: PUT
    - Endpoint: `/softskill/{softskill_id}`
    - Description: Edits the details of a specific softskill by its ID.

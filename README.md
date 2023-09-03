# THE ARCHITECT By InnovateFusion for A2SV Generative AI Hackaton 


## USING YARN (Recommend)

- yarn install
- yarn dev

## USING NPM

- npm i OR npm i --legacy-peer-deps
- npm run dev

#ENV VARAIBLE FOR BACKEND


Sure, here are one-line descriptions for each environment variable:
- OPENAI_API_KEY: For cha with chat gpt
- CLD_API_KEY: Your Cloud API key for accessing cloud services.
- CLD_API_SECRET: Your Cloud API secret for secure authentication.
- MIRAGE_API_KEY: Your Mirage API key for accessing Mirage services.
- STABILITY_API_KEY: Your Stability API key for authorization to Stability services.
- DBPATH: For Mysql DataBase

#BACKEND FORLDER
- api/crud: For DataBase related issue
- api/route: For endpoints
- api/chat: For chat with open api
- api/common/image: for image generation
Example: endpoint: https://architect-n16u.onrender.com/api/v1/users/d00bfa01-0697-401a-88db-b6a6d9320dbf/homes 

##API Documentation for Home Management
This FastAPI application provides an endpoint for managing residential and business homes.

Create Residential Home for a User
POST /users/{user_id}/homes/residential

Create a residential home for a user.

user_id (path parameter): The ID of the user for whom the home is being created.
home (request body): JSON object containing information about the residential home. See the schemas section for the required structure.
Create Business Home for a User
POST /users/{user_id}/homes/business

Create a business home for a user.

user_id (path parameter): The ID of the user for whom the business home is being created.
home (request body): JSON object containing information about the business home. See the schemas section for the required structure.
Retrieve Home by ID
GET /homes/{home_id}

Retrieve information about a home by its ID.

home_id (path parameter): The ID of the home to retrieve.
Create Chat for a Home
POST /homes/{home_id}/chat

Create a chat for a specific home.

home_id (path parameter): The ID of the home for which the chat is being created.
chat (request body): JSON object containing chat details. See the schemas section for the required structure.
Retrieve Homes for a User
GET /users/{user_id}/homes

Retrieve a list of homes associated with a user.

user_id (path parameter): The ID of the user for whom the homes are being retrieved.
skip (query parameter, optional): Number of records to skip (default is 0).
limit (query parameter, optional): Maximum number of records to retrieve (default is 100).
Update Residential Home
PUT /homes/{home_id}/residential

Update information about a residential home.

home_id (path parameter): The ID of the residential home to update.
home (request body): JSON object containing updated residential home information. See the schemas section for the required structure.
Update Business Home
PUT /homes/{home_id}/business

Update information about a business home.

home_id (path parameter): The ID of the business home to update.
home (request body): JSON object containing updated business home information. See the schemas section for the required structure.
Retrieve Home Image
GET /homes/{home_id}/image

Retrieve the image associated with a home.

home_id (path parameter): The ID of the home for which the image is being retrieved.
Delete Home
DELETE /homes/{home_id}

Delete a home by its ID.

home_id (path parameter): The ID of the home to delete.
Retrieve Home Summary
GET /homes/{home_id}/summary

Retrieve a summary of information about a home.

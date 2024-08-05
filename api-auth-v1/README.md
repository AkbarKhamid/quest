# API Authentication Service

This service handles user authentication and management for the Quest platform.

## API Endpoints

The following table describes the available API endpoints:

| URL                | Method | Description                            | OpenAPI Link                                              |
| ------------------ | ------ | -------------------------------------- | --------------------------------------------------------- |
| `/auth/signup`     | POST   | Register a new user                    | [Link](#operation/create_user_auth_signup_post)           |
| `/auth/login`      | POST   | Authenticate a user and return a token | [Link](#operation/login_for_access_token_auth_login_post) |
| `/auth/logout`     | POST   | Log out a user (invalidate token)      | [Link](#operation/logout_user_auth_logout_post)           |
| `/users/me`        | GET    | Get current user's information         | [Link](#operation/read_users_me_users_me_get)             |
| `/users/me`        | PATCH  | Update current user's information      | [Link](#operation/update_user_me_users_me_patch)          |
| `/users/{user_id}` | GET    | Get a user's information by ID         | [Link](#operation/read_user_users__user_id__get)          |
| `/users/{user_id}` | DELETE | Delete a user by ID                    | [Link](#operation/delete_user_users__user_id__delete)     |

## OpenAPI Documentation

For detailed information about request/response schemas, authentication requirements, and to try out the API, please refer to the auto-generated OpenAPI documentation:

[OpenAPI Documentation](http://localhost:8000/docs)

To access the OpenAPI documentation:

1. Ensure the API server is running.
2. Open a web browser and navigate to `http://localhost:8000/docs`.

This interactive documentation allows you to:

- Read detailed descriptions of each endpoint
- Understand the required parameters and request bodies
- Test the API directly from the browser
- View response schemas and possible status codes

## Authentication

Most endpoints require authentication. To authenticate:

1. Use the `/auth/login` endpoint to obtain a JWT token.
2. Include the token in the `Authorization` header of subsequent requests:

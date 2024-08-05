# TODO: Quest Catalog Service

This service manages quest details and properties for the Quest platform.

## API Endpoints

The following table describes the available API endpoints:

| URL                  | Method | Description                         | OpenAPI Link                                             |
| -------------------- | ------ | ----------------------------------- | -------------------------------------------------------- |
| `/quests`            | GET    | List all quests                     | [Link](#operation/list_quests_quests_get)                |
| `/quests/{quest_id}` | GET    | Get details of a specific quest     | [Link](#operation/get_quest_quests__quest_id__get)       |
| `/quests`            | POST   | Create a new quest                  | [Link](#operation/create_quest_quests_post)              |
| `/quests/{quest_id}` | PUT    | Update an existing quest            | [Link](#operation/update_quest_quests__quest_id__put)    |
| `/quests/{quest_id}` | DELETE | Delete a quest                      | [Link](#operation/delete_quest_quests__quest_id__delete) |
| `/quests/search`     | GET    | Search for quests based on criteria | [Link](#operation/search_quests_quests_search_get)       |

## OpenAPI Documentation

For detailed information about request/response schemas, authentication requirements, and to try out the API, please refer to the auto-generated OpenAPI documentation:

[OpenAPI Documentation](http://localhost:8001/docs)

To access the OpenAPI documentation:

1. Ensure the API server is running.
2. Open a web browser and navigate to `http://localhost:8001/docs`.

This interactive documentation allows you to read detailed descriptions of each endpoint, understand the required parameters and request bodies, test the API directly from the browser, and view response schemas and possible status codes.

## Authentication

Most endpoints require authentication. Please refer to the Authentication Service documentation for details on how to obtain and use authentication tokens.

## Rate Limiting

To prevent abuse, this API implements rate limiting. Please refer to the OpenAPI documentation for specific limits on each endpoint.

## Errors

The API uses standard HTTP status codes to indicate the success or failure of requests. In case of an error, the response body will contain more detailed information about the problem.

For any questions or issues, please contact the dev team.

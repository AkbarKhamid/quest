# TODO: Quest Processing Service

This service tracks user quest progress and manages user quest rewards for the Quest platform.

## API Endpoints

The following table describes the available API endpoints:

| URL                              | Method | Description                                     | OpenAPI Link                                                                |
| -------------------------------- | ------ | ----------------------------------------------- | --------------------------------------------------------------------------- |
| `/progress/{user_id}`            | GET    | Get quest progress for a user                   | [Link](#operation/get_user_progress_progress__user_id__get)                 |
| `/progress/{user_id}/{quest_id}` | POST   | Update quest progress for a user                | [Link](#operation/update_quest_progress_progress__user_id___quest_id__post) |
| `/rewards/{user_id}`             | GET    | Get rewards for a user                          | [Link](#operation/get_user_rewards_rewards__user_id__get)                   |
| `/rewards/{user_id}/{quest_id}`  | POST   | Award a reward to a user for completing a quest | [Link](#operation/award_quest_reward_rewards__user_id___quest_id__post)     |
| `/rewards/{user_id}/{reward_id}` | PATCH  | Update reward status (e.g., claim a reward)     | [Link](#operation/update_reward_status_rewards__user_id___reward_id__patch) |
| `/stats/{user_id}`               | GET    | Get quest completion statistics for a user      | [Link](#operation/get_user_stats_stats__user_id__get)                       |

## OpenAPI Documentation

For detailed information about request/response schemas, authentication requirements, and to try out the API, please refer to the auto-generated OpenAPI documentation:

[OpenAPI Documentation](http://localhost:8002/docs)

To access the OpenAPI documentation:

1. Ensure the API server is running.
2. Open a web browser and navigate to `http://localhost:8002/docs`.

This interactive documentation allows you to read detailed descriptions of each endpoint, understand the required parameters and request bodies, test the API directly from the browser, and view response schemas and possible status codes.

## Authentication

Most endpoints require authentication. Please refer to the Authentication Service documentation for details on how to obtain and use authentication tokens.

## Rate Limiting

To prevent abuse, this API implements rate limiting. Please refer to the OpenAPI documentation for specific limits on each endpoint.

## Errors

The API uses standard HTTP status codes to indicate the success or failure of requests. In case of an error, the response body will contain more detailed information about the problem.

For any questions or issues, please contact the dev team.

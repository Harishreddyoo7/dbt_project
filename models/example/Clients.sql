WITH source_data AS (
    SELECT
        *
    FROM {{ source('src_postgres', 'Clients') }}
)
SELECT
    "ClientId" AS "Client ID",
    "ClientName" AS "Client Name",
    "Description",
    "ClientUri" AS "Client URI",
    "FrontChannelLogoutSessionRequired" AS "Front Channel Logout Session Required",
    "BackChannelLogoutSessionRequired" AS "Back Channel Logout Session Required",
    "Created",
    "Updated",
    "LastAccessed"
FROM
    source_data

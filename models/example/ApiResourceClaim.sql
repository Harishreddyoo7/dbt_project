WITH source_data AS (
    SELECT
        *
    FROM {{ source('src_postgres', 'ApiResourceClaim') }}
)
SELECT
    "Id",
    "Type"
FROM
    source_data
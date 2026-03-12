SELECT
    id,
    username,
    first_name,
    language,
    cv,
    created_at,
    updated_at
FROM users
LIMIT $1
OFFSET $2;
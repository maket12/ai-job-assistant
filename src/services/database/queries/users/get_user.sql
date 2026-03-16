SELECT
    id,
    username,
    first_name,
    language,
    cv,
    created_at,
    updated_at
FROM users
WHERE id = $1;
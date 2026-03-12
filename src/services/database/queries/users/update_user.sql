UPDATE users
SET
     username = $2,
     first_name = $3,
     language = $4,
     cv = $5,
     updated_at = CURRENT_TIMESTAMP
WHERE id = $1;
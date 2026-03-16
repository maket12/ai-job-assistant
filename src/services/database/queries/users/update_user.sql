UPDATE users
SET
     username = COALESCE($2, username),
     first_name = COALESCE($3, first_name),
     language = COALESCE($4, language),
     cv = COALESCE($5, cv),
     updated_at = CURRENT_TIMESTAMP
WHERE id = $1;
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL
);

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM users) THEN
        INSERT INTO users (username, password) VALUES
        ('admin', 'admin123'),
        ('user1', 'password1'),
        ('user2', 'password2');
    END IF;
END $$;

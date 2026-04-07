
-- TASK 2. Inserting and updating
CREATE OR REPLACE PROCEDURE insert_or_update(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    
    IF NOT FOUND THEN
        INSERT INTO phonebook (name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;

-- TASK 3. Inserting many users
CREATE OR REPLACE PROCEDURE insert_many(
    users_data TEXT[][]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
BEGIN
    FOR i IN 1..array_length(users_data, 1)
    LOOP
        INSERT INTO phonebook (name, phone) 
        VALUES (users_data[i][1], users_data[i][2])
        ON CONFLICT (phone) DO NOTHING;
    END LOOP;
END;
$$;

-- TASK 5. To delete by name or phone
CREATE OR REPLACE PROCEDURE delete_by(
    identifier VARCHAR,
    delete_type VARCHAR DEFAULT 'name'
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF delete_type = 'name' THEN
        DELETE FROM phonebook WHERE name = identifier;
    ELSE
        DELETE FROM phonebook WHERE phone = identifier;
    END IF;
END;
$$;
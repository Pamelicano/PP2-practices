-- TASK 1. Search py pattern
CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
RETURNS TABLE(
    id INTEGER,
    name VARCHAR,
    phone VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook 
    WHERE phonebook.name ILIKE '%' || pattern || '%' 
       OR phonebook.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- TASK 4. pagination
CREATE OR REPLACE FUNCTION get_paginated(page_num INTEGER, page_size INTEGER)
RETURNS TABLE(
    id INTEGER,
    name VARCHAR,
    phone VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook 
    ORDER BY id 
    LIMIT page_size 
    OFFSET (page_num - 1) * page_size;
END;
$$ LANGUAGE plpgsql;
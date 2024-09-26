SELECT * FROM tasks WHERE user_id = 1;

SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;

SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

INSERT INTO tasks (title, description, status_id, user_id) 
VALUES ('New Task', 'Description of the new task', 1, 1);

SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');
DELETE FROM tasks WHERE id = 1;

SELECT * FROM users WHERE email LIKE '%@example.com';
UPDATE users SET fullname = 'New Name' WHERE id = 1;

SELECT s.name, COUNT(t.id) 
FROM tasks t 
JOIN status s ON t.status_id = s.id 
GROUP BY s.name;

SELECT t.* 
FROM tasks t 
JOIN users u ON t.user_id = u.id 
WHERE u.email LIKE '%@example.com';
SELECT * FROM tasks WHERE description IS NULL;

SELECT u.fullname, t.title 
FROM tasks t 
JOIN users u ON t.user_id = u.id 
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');

SELECT u.fullname, COUNT(t.id) 
FROM users u 
LEFT JOIN tasks t ON u.id = t.user_id 
GROUP BY u.fullname;

-- Admin 1
INSERT INTO authentication_user (id, email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES (1002,'adminuser@gmail.com', 'John', 'Doe', 'ADMIN', 'Adminuser.2023', true, true, true, NOW());

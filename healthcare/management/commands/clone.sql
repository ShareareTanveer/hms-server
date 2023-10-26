-- Department 1
INSERT INTO healthcare_department (name, description, status) 
VALUES ('Cardiology', 'Specializing in heart health', true);

-- Department 2
INSERT INTO healthcare_department (name, description, status) 
VALUES ('Orthopedics', 'Focusing on musculoskeletal conditions', true);

-- Department 3
INSERT INTO healthcare_department (name, description, status) 
VALUES ('Obstetrics and Gynecology', 'Women health care', true);

-- Department 4
INSERT INTO healthcare_department (name, description, status) 
VALUES ('Oncology', 'Cancer diagnosis and treatment', false);

-- Department 5
INSERT INTO healthcare_department (name, description, status) 
VALUES ('Pediatrics', 'Medical care for children', true);

-- Department 6
INSERT INTO healthcare_department (name, description, status) 
VALUES ('Neurology', 'Treatment for neurological disorders', false);

-- Department 7
INSERT INTO healthcare_department (name, description, status) 
VALUES ('Dermatology', 'Skin and hair care', true);

-- Department 8
INSERT INTO healthcare_department (name, description, status) 
VALUES ('Ophthalmology', 'Eye care and vision services', false);

-- Department 9
INSERT INTO healthcare_department (name, description, status) 
VALUES ('Urology', 'Specializing in urinary tract issues', true);

-- Department 10
INSERT INTO healthcare_department (name, description, status) 
VALUES ('Psychiatry', 'Mental health and psychiatric care', true);


-- Admin 1
INSERT INTO authentication_user (id, email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES (1001,'admin@gmail.com', 'John', 'Doe', 'ADMIN', 'Admin.2023', true, true, true, NOW());

-- User 1
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('patient1@example.com', 'John', 'Doe', 'PATIENT', 'Patient.2023', false, false, true, NOW());

-- User 2
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('patient2@example.com', 'Jane', 'Smith', 'PATIENT', 'Patient.2023', false, false, true, NOW());

-- User 3
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('patient3@example.com', 'David', 'Brown', 'PATIENT', 'Patient.2023', false, false, true, NOW());

-- User 4
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('patient4@example.com', 'Sarah', 'Wilson', 'PATIENT', 'Patient.2023', false, false, true, NOW());

-- User 5
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('patient5@example.com', 'Michael', 'Johnson', 'PATIENT', 'Patient.2023', false, false, true, NOW());

-- User 6
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('patient6@example.com', 'Emily', 'Miller', 'PATIENT', 'Patient.2023', false, false, true, NOW());

-- User 7
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('patient7@example.com', 'Jessica', 'Martinez', 'PATIENT', 'Patient.2023', false, false, true, NOW());

-- User 8
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('patient8@example.com', 'Daniel', 'Davis', 'PATIENT', 'Patient.2023', false, false, true, NOW());

-- User 9
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('patient9@example.com', 'Olivia', 'Garcia', 'PATIENT', 'Patient.2023', false, false, true, NOW());

-- User 10
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('patient10@example.com', 'William', 'Harris', 'PATIENT', 'Patient.2023', false, false, true, NOW());


-- User 1
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('doctor1@example.com', 'John', 'Doe', 'DOCTOR', 'Doctor.2023', false, false, true, NOW());

-- User 2
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('doctor2@example.com', 'Jane', 'Smith', 'DOCTOR', 'Doctor.2023', false, false, true, NOW());

-- User 3
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('doctor3@example.com', 'David', 'Brown', 'DOCTOR', 'Doctor.2023', false, false, true, NOW());

-- User 4
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('doctor4@example.com', 'Sarah', 'Wilson', 'DOCTOR', 'Doctor.2023', false, false, true, NOW());

-- User 5
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('doctor5@example.com', 'Michael', 'Johnson', 'DOCTOR', 'Doctor.2023', false, false, true, NOW());

-- User 6
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('doctor6@example.com', 'Emily', 'Miller', 'DOCTOR', 'Doctor.2023', false, false, true, NOW());

-- User 7
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('doctor7@example.com', 'Jessica', 'Martinez', 'DOCTOR', 'Doctor.2023', false, false, true, NOW());

-- User 8
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('doctor8@example.com', 'Daniel', 'Davis', 'DOCTOR', 'Doctor.2023', false, false, true, NOW());

-- User 9
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('doctor9@example.com', 'Olivia', 'Garcia', 'DOCTOR', 'Doctor.2023', false, false, true, NOW());

-- User 10
INSERT INTO authentication_user (email, first_name, last_name, role, password, is_superuser, is_staff, is_active, date_joined)
VALUES ('doctor10@example.com', 'William', 'Harris', 'DOCTOR', 'Doctor.2023', false, false, true, NOW());




-- UserDetail 1
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (1, '123 Main St, City', '555-123-4567', '1990-01-15', 'M', 'A+');
-- UserDetail 2
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (2, '456 Elm St, Town', '555-987-6543', '1985-03-20', 'F', 'B-');
-- UserDetail 3
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (3, '789 Oak St, Village', '555-777-8888', '1980-12-05', 'M', 'O+');
-- UserDetail 4
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (4, '321 Pine St, Hamlet', '555-234-5678', '1995-07-10', 'F', 'AB+');
-- UserDetail 5
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (5, '567 Maple St, County', '555-345-6789', '1992-09-25', 'M', 'A-');
-- UserDetail 6
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (6, '890 Cedar St, Town', '555-876-5432', '1988-04-03', 'F', 'O-');
-- UserDetail 7
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (7, '753 Birch St, Village', '555-654-3210', '1991-06-12', 'M', 'B+');
-- UserDetail 8
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (8, '654 Redwood St, County', '555-987-6543', '1987-10-01', 'F', 'AB-');
-- UserDetail 9
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (9, '432 Magnolia St, Town', '555-123-9876', '1994-11-15', 'M', 'A+');
-- UserDetail 10
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (10, '876 Chestnut St, Village', '555-234-5678', '1993-08-22', 'F', 'B-');

-- UserDetail 1
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (11, '123 Main St, City', '555-123-4567', '1990-01-15', 'M', 'A+');
-- UserDetail 2
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (12, '456 Elm St, Town', '555-987-6543', '1985-03-20', 'F', 'B-');
-- UserDetail 3
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (13, '789 Oak St, Village', '555-777-8888', '1980-12-05', 'M', 'O+');
-- UserDetail 4
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (14, '321 Pine St, Hamlet', '555-234-5678', '1995-07-10', 'F', 'AB+');
-- UserDetail 5
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (15, '567 Maple St, County', '555-345-6789', '1992-09-25', 'M', 'A-');
-- UserDetail 6
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (16, '890 Cedar St, Town', '555-876-5432', '1988-04-03', 'F', 'O-');
-- UserDetail 7
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (17, '753 Birch St, Village', '555-654-3210', '1991-06-12', 'M', 'B+');
-- UserDetail 8
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (18, '654 Redwood St, County', '555-987-6543', '1987-10-01', 'F', 'AB-');
-- UserDetail 9
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (19, '432 Magnolia St, Town', '555-123-9876', '1994-11-15', 'M', 'A+');
-- UserDetail 10
INSERT INTO core_userdetail (user_id, address, phone, date_of_birth, sex, blood_group)
VALUES (20, '876 Chestnut St, Village', '555-234-5678', '1993-08-22', 'F', 'B')



-- Patient 1
INSERT INTO healthcare_patient (user_details_id, occupation, medical_history, status)
VALUES (1, 'Engineer', 'No major medical history', true);
-- Patient 2
INSERT INTO healthcare_patient (user_details_id, occupation, medical_history, status)
VALUES (2, 'Teacher', 'Allergic to peanuts', true);
-- Patient 3
INSERT INTO healthcare_patient (user_details_id, occupation, medical_history, status)
VALUES (3, 'Accountant', 'Hypertension', true);
-- Patient 4
INSERT INTO healthcare_patient (user_details_id, occupation, medical_history, status)
VALUES (4, 'Student', 'Asthma', true);
-- Patient 5
INSERT INTO healthcare_patient (user_details_id, occupation, medical_history, status)
VALUES (5, 'Nurse', 'Diabetes', true);
-- Patient 6
INSERT INTO healthcare_patient (user_details_id, occupation, medical_history, status)
VALUES (6, 'Librarian', 'No major medical history', true);
-- Patient 7
INSERT INTO healthcare_patient (user_details_id, occupation, medical_history, status)
VALUES (7, 'Engineer', 'Allergic to shellfish', true);
-- Patient 8
INSERT INTO healthcare_patient (user_details_id, occupation, medical_history, status)
VALUES (8, 'Teacher', 'Asthma', true);
-- Patient 9
INSERT INTO healthcare_patient (user_details_id, occupation, medical_history, status)
VALUES (9, 'Student', 'No major medical history', true);
-- Patient 10
INSERT INTO healthcare_patient (user_details_id, occupation, medical_history, status)
VALUES (10, 'Nurse', 'No major medical history', true);



-----Doctor Role ---------


-- Doctor 1
INSERT INTO healthcare_doctor (user_details_id, designation, department_id, short_bio, spacialist, education_degree, status, visiting_fee)
VALUES (11, 'Cardiologist', 1, 'Specializing in heart health', 'Cardiology', 'M.D. in Cardiology', true, 150);

-- Doctor 2
INSERT INTO healthcare_doctor (user_details_id, designation, department_id, short_bio, spacialist, education_degree, status, visiting_fee)
VALUES (12, 'Orthopedic Surgeon', 2, 'Focusing on musculoskeletal conditions', 'Orthopedics', 'M.D. in Orthopedics', true, 180);

-- Doctor 3
INSERT INTO healthcare_doctor (user_details_id, designation, department_id, short_bio, spacialist, education_degree, status, visiting_fee)
VALUES (13, 'OB-GYN Specialist', 3, 'Women health care', 'Obstetrics and Gynecology', 'M.D. in OB-GYN', true, 160);

-- Doctor 4
INSERT INTO healthcare_doctor (user_details_id, designation, department_id, short_bio, spacialist, education_degree, status, visiting_fee)
VALUES (14, 'Oncologist', 4, 'Cancer diagnosis and treatment', 'Oncology', 'M.D. in Oncology', true, 200);

-- Doctor 5
INSERT INTO healthcare_doctor (user_details_id, designation, department_id, short_bio, spacialist, education_degree, status, visiting_fee)
VALUES (15, 'Pediatrician', 5, 'Medical care for children', 'Pediatrics', 'M.D. in Pediatrics', true, 140);

-- Doctor 6
INSERT INTO healthcare_doctor (user_details_id, designation, department_id, short_bio, spacialist, education_degree, status, visiting_fee)
VALUES (16, 'Neurologist', 6, 'Treatment for neurological disorders', 'Neurology', 'M.D. in Neurology', true, 190);

-- Doctor 7
INSERT INTO healthcare_doctor (user_details_id, designation, department_id, short_bio, spacialist, education_degree, status, visiting_fee)
VALUES (17, 'Dermatologist', 7, 'Skin and hair care', 'Dermatology', 'M.D. in Dermatology', true, 170);

-- Doctor 8
INSERT INTO healthcare_doctor (user_details_id, designation, department_id, short_bio, spacialist, education_degree, status, visiting_fee)
VALUES (18, 'Ophthalmologist', 8, 'Eye care and vision services', 'Ophthalmology', 'M.D. in Ophthalmology', true, 210);

-- Doctor 9
INSERT INTO healthcare_doctor (user_details_id, designation, department_id, short_bio, spacialist, education_degree, status, visiting_fee)
VALUES (19, 'Urologist', 9, 'Specializing in urinary tract issues', 'Urology', 'M.D. in Urology', true, 180);

-- Doctor 10
INSERT INTO healthcare_doctor (user_details_id, designation, department_id, short_bio, spacialist, education_degree, status, visiting_fee)
VALUES (20, 'Psychiatrist', 10, 'Mental health and psychiatric care', 'Psychiatry', 'M.D. in Psychiatry', true, 120);



-- Insert values into the "healthcare_day" table
INSERT INTO healthcare_day (name) VALUES ('Monday');
INSERT INTO healthcare_day (name) VALUES ('Tuesday');
INSERT INTO healthcare_day (name) VALUES ('Wednesday');
INSERT INTO healthcare_day (name) VALUES ('Thursday');
INSERT INTO healthcare_day (name) VALUES ('Friday');
INSERT INTO healthcare_day (name) VALUES ('Saturday');
INSERT INTO healthcare_day (name) VALUES ('Sunday');






-- Insert values into the "Schedule" table
INSERT INTO healthcare_schedule (doctor_id, start_time, end_time, per_patient_time, status)
VALUES (1, '09:00:00', '17:00:00', 15, true);

INSERT INTO healthcare_schedule (doctor_id, start_time, end_time, per_patient_time, status)
VALUES (2, '08:30:00', '16:30:00', 20, true);

INSERT INTO healthcare_schedule (doctor_id, start_time, end_time, per_patient_time, status)
VALUES (3, '10:00:00', '18:00:00', 15, true);

INSERT INTO healthcare_schedule (doctor_id, start_time, end_time, per_patient_time, status)
VALUES (4, '08:00:00', '16:00:00', 30, true);

INSERT INTO healthcare_schedule (doctor_id, start_time, end_time, per_patient_time, status)
VALUES (5, '09:30:00', '17:30:00', 20, true);

INSERT INTO healthcare_schedule (doctor_id, start_time, end_time, per_patient_time, status)
VALUES (6, '10:30:00', '18:30:00', 15, true);

INSERT INTO healthcare_schedule (doctor_id, start_time, end_time, per_patient_time, status)
VALUES (7, '09:00:00', '17:00:00', 20, true);

INSERT INTO healthcare_schedule (doctor_id, start_time, end_time, per_patient_time, status)
VALUES (8, '08:30:00', '16:30:00', 30, true);

INSERT INTO healthcare_schedule (doctor_id, start_time, end_time, per_patient_time, status)
VALUES (9, '10:00:00', '18:00:00', 15, true);

INSERT INTO healthcare_schedule (doctor_id, start_time, end_time, per_patient_time, status)
VALUES (10, '08:00:00', '16:00:00', 20, true);

-- Associate available days with schedules
-- Doctor 1 Schedule
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (1, 1);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (1, 2);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (1, 3);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (1, 4);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (1, 5);

-- Doctor 2 Schedule
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (2, 2);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (2, 3);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (2, 4);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (2, 5);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (2, 6);

-- Doctor 3 Schedule
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (3, 1);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (3, 2);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (3, 3);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (3, 4);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (3, 5);

-- Doctor 4 Schedule
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (4, 2);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (4, 3);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (4, 4);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (4, 5);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (4, 6);

-- Doctor 5 Schedule
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (5, 2);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (5, 3);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (5, 4);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (5, 6);

-- Doctor 6 Schedule
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (6, 2);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (6, 5);

-- Doctor 7 Schedule
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (7, 2);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (7, 5);

-- Doctor 8 Schedule
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (8, 2);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (8, 3);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (8, 1);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (8, 5);

-- Doctor 9 Schedule
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (9, 2);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (9, 5);

-- Doctor 10 Schedule
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (10, 2);
INSERT INTO healthcare_schedule_available_days (schedule_id, day_id) VALUES (10, 5);



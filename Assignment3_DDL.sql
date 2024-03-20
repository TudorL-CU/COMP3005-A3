create table students (
	student_id			SERIAL,
	first_name			TEXT	not null,
	last_name			TEXT	not null,
	email				TEXT	unique not null,
	enrollment_date		DATE,
	
	primary key (student_id)
);
create database geeks;
\c geeks;

create schema core;
create schema users;
create schema stats;

drop table if exists users.user_types cascade;
create table users.user_types (
	user_type_id      serial primary key,
	user_type         varchar(100) not null
);


drop table if exists users.users cascade;
create table users.users (
	user_id         serial primary key,
	user_type_id    integer not null references users.user_types(user_type_id),
	email           varchar(500) unique not null
);


drop table if exists core.topics cascade;
create table core.topics (
	topic_id           serial primary key,
	description        varchar(500) not null
);


drop table if exists core.questions cascade;
create table core.questions (
	question_id      serial primary key,
	topic_id         integer not null references core.topics(topic_id),
	text    varchar(500) not null
);


drop table if exists stats.questions_hist_data cascade;
create table stats.questions_hist_data (
	questions_hist_data_id      serial primary key,
	question_id                 integer not null references core.questions(question_id),
	topic_id                    integer not null references core.topics(topic_id),
	user_id                     integer not null references users.users(user_id),
	answered_correctly          boolean,
	date_answered               timestamp without time zone
);

drop table if exists stats.topic_stats cascade;
create table stats.topic_stats (
	topic_stats_id             serial primary key,
	topic_id                   integer not null references core.topics(topic_id),
	percentage_correct         numeric not null
);


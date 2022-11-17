CREATE DATABASE flask_intro;

\connect flask_intro

CREATE TABLE reminders (
    title VARCHAR(255),
    description TEXT
);
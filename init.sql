
CREATE TABLE audit_logs
(
    id serial primary key not null,
    browser text,
    user_agent text,
    referrer text,
    remote_address text,
    path text,
    message text,
    severity text,
    event_type text,
    event_date timestamp default current_timestamp(),
    success boolean,
    source text,
    detail text,
    application_version text
);

CREATE TABLE accounts
(
    id serial primary key not null,
    email text not null,
    credentials text not null,
    token text not null,
    created timestamp default current_timestamp
);



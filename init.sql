
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
    karma integer not null default 0,
    email text not null,
    credentials text not null,
    token text not null,
    created timestamp default current_timestamp(),
    muted_till timestamp,
    banned_till timestamp
);

create table species
(
    id serial primary key not null,
    name text not null
);

create table techniques
(
    id serial primary key not null,
    name text not null
);

create table seasons
(
    id serial primary key not null,
    name text not null
);


create table my_fisheries
(
    id serial primary key not null,
    name text not null,
    default_zoom integer default 16,
    account_id int not null,
    constraint fk_us_fish FOREIGN KEY(account_id) references accounts(id)
);

create table coordinates
(
    id serial primary key not null,
    location point not null
);

create table hotspots
(
    id serial primary key not null,
    species_id int not null,
    fishery_id int not null,
    highlight_color text not null,
    species_id int not null,
    season_id int not null,
    constraint fk_hsp_spec FOREIGN KEY (species_id) references species(id),
    constraint fk_hsp_seas FOREIGN KEY (season_id) references  seasons(id)
);

create table hotspot_techniques
(
   id serial primary key not null,
   hotspot_id int not null,
   technique_id int not null,
   constraint fk_hsptq_hsp FOREIGN KEY (hotspot_id) references hotspots(id),
   constraint fk_hsptq_tq FOREIGN KEY (technique_id) references  techniques(id)
);

create table hotspot_coordinates
(
   id serial primary key not null,
   hotspot_id int not null,
   coordinate_id int not null,
   constraint fk_hspco_hsp FOREIGN KEY (hotspot_id) references hotspots(id),
   constraint fk_hspco_co FOREIGN KEY (coordinate_id) references  coordinates(id)
);

create table my_fishery_coordinates
(
   id serial primary key not null,
   fishery_id int not null,
   coordinate_id int not null,
   constraint fk_mfc_mf FOREIGN KEY (fishery_id) references my_fisheries(id),
   constraint fk_mfc_co FOREIGN KEY (coordinate_id) references  coordinates(id)
);

create table videos
(
    id serial primary key not null,
    url text not null,
    clicks int not null default 0,
    added timestamp default current_timestamp
);

create table technique_videos
(
   id serial primary key not null,
   technique_id int not null,
   video_id int not null,
   constraint fk_tqv_tq FOREIGN KEY (technique_id) references techniques(id),
   constraint fk_tqv_vd FOREIGN KEY (video_id) references  videos(id)
);

create table technique_tackle_links
(
   id serial primary key not null,
   technique_id int not null,
   product_url text not null,
   image_url text not null,
   constraint fk_tqv_tq FOREIGN KEY (technique_id) references techniques(id)
);
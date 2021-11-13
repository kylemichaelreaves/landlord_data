CREATE TABLE jersey_city (
    id serial,
    street_address text,
    owner_name text,
    owners_mailing_address text,
    city_state_zip text,
    full_address text,
    number_properties_owned int,
    list_properties_owned text[],
    latitude numeric(8, 6),
    longitude numeric(8, 6)
);


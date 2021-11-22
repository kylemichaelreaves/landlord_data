CREATE TABLE jersey_city (
    id serial,
    street_address text,
    owner_name text,
    owners_mailing_address text,
    city_state_zip text,
    property_full_address text,
    units int,
    list_properties_owned text[],
    number_properties_owned int,
    g_code text,
    latitude numeric(8, 6),
    longitude numeric(8, 6),
    primary key (id)
);


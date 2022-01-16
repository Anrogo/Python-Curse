-- INSERT INTO persona(nombre, apellido, email) VALUES ('Susana', 'Lara', 'slara@mail.com')
-- SELECT * FROM public.persona ORDER BY id_persona ASC 
-- DELETE FROM persona WHERE id_persona = 3

CREATE TABLE IF NOT EXISTS public.persona
(
    id_persona integer NOT NULL DEFAULT nextval('persona_id_persona_seq'::regclass),
    nombre character varying COLLATE pg_catalog."default",
    apellido character varying COLLATE pg_catalog."default",
    email character varying COLLATE pg_catalog."default",
    CONSTRAINT persona_pkey PRIMARY KEY (id_persona)
)

INSERT INTO public.persona (
nombre, apellido, email) VALUES (
'Juan'::character varying, 'Perez
'::character varying, 'jperez@mail.com
'::character varying), ('Karla
'::character varying, 'Gómez
'::character varying, 'kgomez@mail.com'::character varying)
 returning id_persona;

--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1 (Debian 16.1-1.pgdg120+1)
-- Dumped by pg_dump version 16.1 (Debian 16.1-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: profiles; Type: TABLE; Schema: public; Owner: uwsgi
--

CREATE TABLE public.profiles (
    id integer NOT NULL,
    lastname character varying(100),
    firstname character varying(100),
    email character varying(320),
    activities text
);


ALTER TABLE public.profiles OWNER TO uwsgi;

--
-- Name: profiles_id_seq; Type: SEQUENCE; Schema: public; Owner: uwsgi
--

CREATE SEQUENCE public.profiles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.profiles_id_seq OWNER TO uwsgi;

--
-- Name: profiles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: uwsgi
--

ALTER SEQUENCE public.profiles_id_seq OWNED BY public.profiles.id;


--
-- Name: status; Type: TABLE; Schema: public; Owner: uwsgi
--

CREATE TABLE public.status (
    id integer NOT NULL,
    profile_id integer NOT NULL,
    message text,
    datetime timestamp without time zone
);


ALTER TABLE public.status OWNER TO uwsgi;

--
-- Name: status_id_seq; Type: SEQUENCE; Schema: public; Owner: uwsgi
--

CREATE SEQUENCE public.status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.status_id_seq OWNER TO uwsgi;

--
-- Name: status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: uwsgi
--

ALTER SEQUENCE public.status_id_seq OWNED BY public.status.id;


--
-- Name: status_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: uwsgi
--

CREATE SEQUENCE public.status_profile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.status_profile_id_seq OWNER TO uwsgi;

--
-- Name: status_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: uwsgi
--

ALTER SEQUENCE public.status_profile_id_seq OWNED BY public.status.profile_id;


--
-- Name: profiles id; Type: DEFAULT; Schema: public; Owner: uwsgi
--

ALTER TABLE ONLY public.profiles ALTER COLUMN id SET DEFAULT nextval('public.profiles_id_seq'::regclass);


--
-- Name: status id; Type: DEFAULT; Schema: public; Owner: uwsgi
--

ALTER TABLE ONLY public.status ALTER COLUMN id SET DEFAULT nextval('public.status_id_seq'::regclass);


--
-- Name: status profile_id; Type: DEFAULT; Schema: public; Owner: uwsgi
--

ALTER TABLE ONLY public.status ALTER COLUMN profile_id SET DEFAULT nextval('public.status_profile_id_seq'::regclass);


--
-- Data for Name: profiles; Type: TABLE DATA; Schema: public; Owner: uwsgi
--

COPY public.profiles (id, lastname, firstname, email, activities) FROM stdin;
1	Lewis	Jaden	bruh	gaming
\.


--
-- Data for Name: status; Type: TABLE DATA; Schema: public; Owner: uwsgi
--

COPY public.status (id, profile_id, message, datetime) FROM stdin;
1	1	bruh	2024-03-01 16:39:55
\.


--
-- Name: profiles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: uwsgi
--

SELECT pg_catalog.setval('public.profiles_id_seq', 1, false);


--
-- Name: status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: uwsgi
--

SELECT pg_catalog.setval('public.status_id_seq', 1, true);


--
-- Name: status_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: uwsgi
--

SELECT pg_catalog.setval('public.status_profile_id_seq', 1, false);


--
-- Name: profiles profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: uwsgi
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_pkey PRIMARY KEY (id);


--
-- Name: status status_pkey; Type: CONSTRAINT; Schema: public; Owner: uwsgi
--

ALTER TABLE ONLY public.status
    ADD CONSTRAINT status_pkey PRIMARY KEY (id);


--
-- Name: status status_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: uwsgi
--

ALTER TABLE ONLY public.status
    ADD CONSTRAINT status_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES public.profiles(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--


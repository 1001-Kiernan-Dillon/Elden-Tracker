--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

-- Started on 2024-05-04 17:20:21

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
-- TOC entry 234 (class 1259 OID 17134)
-- Name: bosses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bosses (
    id integer NOT NULL,
    name text,
    image text,
    region text,
    description text,
    location text,
    drops text[],
    "healthPoints" text
);


ALTER TABLE public.bosses OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 17133)
-- Name: bossTest_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."bossTest_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."bossTest_id_seq" OWNER TO postgres;

--
-- TOC entry 4917 (class 0 OID 0)
-- Dependencies: 233
-- Name: bossTest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."bossTest_id_seq" OWNED BY public.bosses.id;


--
-- TOC entry 223 (class 1259 OID 16976)
-- Name: items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.items (
    id integer NOT NULL,
    name text NOT NULL,
    image text,
    description text,
    type text,
    effect text,
    obtainedfrom text
);


ALTER TABLE public.items OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16975)
-- Name: items_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.items_id_seq OWNER TO postgres;

--
-- TOC entry 4918 (class 0 OID 0)
-- Dependencies: 222
-- Name: items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.items_id_seq OWNED BY public.items.id;


--
-- TOC entry 225 (class 1259 OID 16990)
-- Name: talismans; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.talismans (
    id integer NOT NULL,
    name text,
    image text,
    description text,
    effects text
);


ALTER TABLE public.talismans OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16989)
-- Name: talismans_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.talismans_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.talismans_id_seq OWNER TO postgres;

--
-- TOC entry 4919 (class 0 OID 0)
-- Dependencies: 224
-- Name: talismans_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.talismans_id_seq OWNED BY public.talismans.id;


--
-- TOC entry 228 (class 1259 OID 17067)
-- Name: user_bosses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_bosses (
    user_id integer NOT NULL,
    boss_id integer NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.user_bosses OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 17090)
-- Name: user_bosses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_bosses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_bosses_id_seq OWNER TO postgres;

--
-- TOC entry 4920 (class 0 OID 0)
-- Dependencies: 229
-- Name: user_bosses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_bosses_id_seq OWNED BY public.user_bosses.id;


--
-- TOC entry 227 (class 1259 OID 17052)
-- Name: user_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_items (
    user_id integer NOT NULL,
    item_id integer NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.user_items OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 17097)
-- Name: user_items_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_items_id_seq OWNER TO postgres;

--
-- TOC entry 4921 (class 0 OID 0)
-- Dependencies: 230
-- Name: user_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_items_id_seq OWNED BY public.user_items.id;


--
-- TOC entry 226 (class 1259 OID 17037)
-- Name: user_talismans; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_talismans (
    user_id integer NOT NULL,
    talisman_id integer NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.user_talismans OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 17104)
-- Name: user_talismans_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_talismans_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_talismans_id_seq OWNER TO postgres;

--
-- TOC entry 4922 (class 0 OID 0)
-- Dependencies: 231
-- Name: user_talismans_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_talismans_id_seq OWNED BY public.user_talismans.id;


--
-- TOC entry 217 (class 1259 OID 16909)
-- Name: user_weapons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_weapons (
    user_id integer NOT NULL,
    weapon_id integer NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.user_weapons OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 17111)
-- Name: user_weapons_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_weapons_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_weapons_id_seq OWNER TO postgres;

--
-- TOC entry 4923 (class 0 OID 0)
-- Dependencies: 232
-- Name: user_weapons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_weapons_id_seq OWNED BY public.user_weapons.id;


--
-- TOC entry 220 (class 1259 OID 16925)
-- Name: user_weapons_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_weapons_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_weapons_user_id_seq OWNER TO postgres;

--
-- TOC entry 4924 (class 0 OID 0)
-- Dependencies: 220
-- Name: user_weapons_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_weapons_user_id_seq OWNED BY public.user_weapons.user_id;


--
-- TOC entry 221 (class 1259 OID 16930)
-- Name: user_weapons_weapon_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_weapons_weapon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_weapons_weapon_id_seq OWNER TO postgres;

--
-- TOC entry 4925 (class 0 OID 0)
-- Dependencies: 221
-- Name: user_weapons_weapon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_weapons_weapon_id_seq OWNED BY public.user_weapons.weapon_id;


--
-- TOC entry 216 (class 1259 OID 16885)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16884)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_user_id_seq OWNER TO postgres;

--
-- TOC entry 4926 (class 0 OID 0)
-- Dependencies: 215
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- TOC entry 219 (class 1259 OID 16917)
-- Name: weapons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.weapons (
    id integer NOT NULL,
    name character varying,
    image character varying,
    description text,
    attack jsonb,
    defence jsonb,
    "scalesWith" jsonb,
    "requiredAttributes" jsonb,
    category character varying,
    weight double precision
);


ALTER TABLE public.weapons OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16916)
-- Name: weapons_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.weapons_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.weapons_id_seq OWNER TO postgres;

--
-- TOC entry 4927 (class 0 OID 0)
-- Dependencies: 218
-- Name: weapons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.weapons_id_seq OWNED BY public.weapons.id;


--
-- TOC entry 4740 (class 2604 OID 17137)
-- Name: bosses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bosses ALTER COLUMN id SET DEFAULT nextval('public."bossTest_id_seq"'::regclass);


--
-- TOC entry 4735 (class 2604 OID 16979)
-- Name: items id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.items ALTER COLUMN id SET DEFAULT nextval('public.items_id_seq'::regclass);


--
-- TOC entry 4736 (class 2604 OID 16993)
-- Name: talismans id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.talismans ALTER COLUMN id SET DEFAULT nextval('public.talismans_id_seq'::regclass);


--
-- TOC entry 4739 (class 2604 OID 17091)
-- Name: user_bosses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_bosses ALTER COLUMN id SET DEFAULT nextval('public.user_bosses_id_seq'::regclass);


--
-- TOC entry 4738 (class 2604 OID 17098)
-- Name: user_items id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_items ALTER COLUMN id SET DEFAULT nextval('public.user_items_id_seq'::regclass);


--
-- TOC entry 4737 (class 2604 OID 17105)
-- Name: user_talismans id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_talismans ALTER COLUMN id SET DEFAULT nextval('public.user_talismans_id_seq'::regclass);


--
-- TOC entry 4731 (class 2604 OID 16926)
-- Name: user_weapons user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_weapons ALTER COLUMN user_id SET DEFAULT nextval('public.user_weapons_user_id_seq'::regclass);


--
-- TOC entry 4732 (class 2604 OID 16931)
-- Name: user_weapons weapon_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_weapons ALTER COLUMN weapon_id SET DEFAULT nextval('public.user_weapons_weapon_id_seq'::regclass);


--
-- TOC entry 4733 (class 2604 OID 17112)
-- Name: user_weapons id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_weapons ALTER COLUMN id SET DEFAULT nextval('public.user_weapons_id_seq'::regclass);


--
-- TOC entry 4730 (class 2604 OID 16888)
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- TOC entry 4734 (class 2604 OID 16920)
-- Name: weapons id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weapons ALTER COLUMN id SET DEFAULT nextval('public.weapons_id_seq'::regclass);


--
-- TOC entry 4760 (class 2606 OID 17141)
-- Name: bosses bossTest_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bosses
    ADD CONSTRAINT "bossTest_pkey" PRIMARY KEY (id);


--
-- TOC entry 4748 (class 2606 OID 16983)
-- Name: items items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_pkey PRIMARY KEY (id);


--
-- TOC entry 4752 (class 2606 OID 16997)
-- Name: talismans talismans_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.talismans
    ADD CONSTRAINT talismans_pkey PRIMARY KEY (id);


--
-- TOC entry 4750 (class 2606 OID 16985)
-- Name: items unique_name; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT unique_name UNIQUE (name);


--
-- TOC entry 4758 (class 2606 OID 17096)
-- Name: user_bosses user_bosses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_bosses
    ADD CONSTRAINT user_bosses_pkey PRIMARY KEY (id);


--
-- TOC entry 4756 (class 2606 OID 17103)
-- Name: user_items user_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_items
    ADD CONSTRAINT user_items_pkey PRIMARY KEY (id);


--
-- TOC entry 4754 (class 2606 OID 17110)
-- Name: user_talismans user_talismans_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_talismans
    ADD CONSTRAINT user_talismans_pkey PRIMARY KEY (id);


--
-- TOC entry 4744 (class 2606 OID 17117)
-- Name: user_weapons user_weapons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_weapons
    ADD CONSTRAINT user_weapons_pkey PRIMARY KEY (id);


--
-- TOC entry 4742 (class 2606 OID 16892)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- TOC entry 4746 (class 2606 OID 16924)
-- Name: weapons weapons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weapons
    ADD CONSTRAINT weapons_pkey PRIMARY KEY (id);


--
-- TOC entry 4767 (class 2606 OID 17168)
-- Name: user_bosses boss_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_bosses
    ADD CONSTRAINT boss_id FOREIGN KEY (boss_id) REFERENCES public.bosses(id) NOT VALID;


--
-- TOC entry 4765 (class 2606 OID 17062)
-- Name: user_items item_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_items
    ADD CONSTRAINT item_id FOREIGN KEY (item_id) REFERENCES public.items(id);


--
-- TOC entry 4763 (class 2606 OID 17047)
-- Name: user_talismans talisman_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_talismans
    ADD CONSTRAINT talisman_id FOREIGN KEY (talisman_id) REFERENCES public.talismans(id);


--
-- TOC entry 4761 (class 2606 OID 16937)
-- Name: user_weapons user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_weapons
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id) NOT VALID;


--
-- TOC entry 4764 (class 2606 OID 17042)
-- Name: user_talismans user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_talismans
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- TOC entry 4766 (class 2606 OID 17057)
-- Name: user_items user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_items
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- TOC entry 4768 (class 2606 OID 17072)
-- Name: user_bosses user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_bosses
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- TOC entry 4762 (class 2606 OID 16942)
-- Name: user_weapons weapon_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_weapons
    ADD CONSTRAINT weapon_id FOREIGN KEY (weapon_id) REFERENCES public.weapons(id) NOT VALID;


-- Completed on 2024-05-04 17:20:21

--
-- PostgreSQL database dump complete
--


--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0 (Homebrew)
-- Dumped by pg_dump version 16.0 (Homebrew)

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
-- Name: culture; Type: TABLE; Schema: public; Owner: database
--

CREATE TABLE public.culture (
    identifiant_culture smallint NOT NULL,
    no_parcelle smallint,
    code_production smallint,
    date_debut date,
    date_fin date,
    qte_recoltee numeric
);


ALTER TABLE public.culture OWNER TO database;

--
-- Name: culture_identifiant_culture_seq; Type: SEQUENCE; Schema: public; Owner: database
--

ALTER TABLE public.culture ALTER COLUMN identifiant_culture ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.culture_identifiant_culture_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: date; Type: TABLE; Schema: public; Owner: database
--

CREATE TABLE public.date (
    date date NOT NULL
);


ALTER TABLE public.date OWNER TO database;

--
-- Name: elements_chimiques; Type: TABLE; Schema: public; Owner: database
--

CREATE TABLE public.elements_chimiques (
    code_element character varying(5) NOT NULL,
    un character varying(20),
    libelle_element character varying(20)
);


ALTER TABLE public.elements_chimiques OWNER TO database;

--
-- Name: engrais; Type: TABLE; Schema: public; Owner: database
--

CREATE TABLE public.engrais (
    id_engrais smallint NOT NULL,
    un character varying(20),
    nom_engrais character varying(20)
);


ALTER TABLE public.engrais OWNER TO database;

--
-- Name: engrais_id_engrais_seq; Type: SEQUENCE; Schema: public; Owner: database
--

ALTER TABLE public.engrais ALTER COLUMN id_engrais ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.engrais_id_engrais_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: epandre; Type: TABLE; Schema: public; Owner: database
--

CREATE TABLE public.epandre (
    id_engrais smallint,
    no_parcelle smallint,
    date date,
    qte_epandue numeric
);


ALTER TABLE public.epandre OWNER TO database;

--
-- Name: logs; Type: TABLE; Schema: public; Owner: database
--

CREATE TABLE public.logs (
    log_id smallint NOT NULL,
    method character varying(25),
    "table" character varying(25),
    status character varying(25),
    "timestamp" timestamp without time zone
);


ALTER TABLE public.logs OWNER TO database;

--
-- Name: logs_log_id_seq; Type: SEQUENCE; Schema: public; Owner: database
--

ALTER TABLE public.logs ALTER COLUMN log_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.logs_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: parcelle; Type: TABLE; Schema: public; Owner: database
--

CREATE TABLE public.parcelle (
    no_parcelle smallint NOT NULL,
    surface numeric,
    nom_parcelle character varying(20),
    coordonnees character varying(20)
);


ALTER TABLE public.parcelle OWNER TO database;

--
-- Name: parcelle_no_parcelle_seq; Type: SEQUENCE; Schema: public; Owner: database
--

ALTER TABLE public.parcelle ALTER COLUMN no_parcelle ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.parcelle_no_parcelle_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: posseder; Type: TABLE; Schema: public; Owner: database
--

CREATE TABLE public.posseder (
    id_engrais smallint,
    code_element character varying(5),
    valeur integer
);


ALTER TABLE public.posseder OWNER TO database;

--
-- Name: production; Type: TABLE; Schema: public; Owner: database
--

CREATE TABLE public.production (
    code_production smallint NOT NULL,
    un character varying(20),
    nom_production character varying(20)
);


ALTER TABLE public.production OWNER TO database;

--
-- Name: production_code_production_seq; Type: SEQUENCE; Schema: public; Owner: database
--

ALTER TABLE public.production ALTER COLUMN code_production ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.production_code_production_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: un; Type: TABLE; Schema: public; Owner: database
--

CREATE TABLE public.un (
    un character varying(20) NOT NULL
);


ALTER TABLE public.un OWNER TO database;

--
-- Data for Name: culture; Type: TABLE DATA; Schema: public; Owner: database
--

COPY public.culture (identifiant_culture, no_parcelle, code_production, date_debut, date_fin, qte_recoltee) FROM stdin;
9	5	3	2000-10-10	2001-10-10	12343
10	7	4	2001-10-10	2023-10-13	8754
12	6	5	2000-10-10	2001-10-10	1
\.


--
-- Data for Name: date; Type: TABLE DATA; Schema: public; Owner: database
--

COPY public.date (date) FROM stdin;
2023-10-12
2023-11-12
2023-12-10
2000-10-10
2001-10-10
\.


--
-- Data for Name: elements_chimiques; Type: TABLE DATA; Schema: public; Owner: database
--

COPY public.elements_chimiques (code_element, un, libelle_element) FROM stdin;
ee	rtey	ele
ae	rtey	lpezr
Na	111	Naokfoe
\.


--
-- Data for Name: engrais; Type: TABLE DATA; Schema: public; Owner: database
--

COPY public.engrais (id_engrais, un, nom_engrais) FROM stdin;
5	rtey	mpoaz
6	rtey	ge2loukata
7	rtey	ge2loukata
8	rtey	ge2loukata
9	rtey	ge2loukata
10	rtey	ge2loukata
11	rtey	ge2loukata
\.


--
-- Data for Name: epandre; Type: TABLE DATA; Schema: public; Owner: database
--

COPY public.epandre (id_engrais, no_parcelle, date, qte_epandue) FROM stdin;
5	24	2023-10-12	4344351
5	23	2023-10-12	4344351
\.


--
-- Data for Name: logs; Type: TABLE DATA; Schema: public; Owner: database
--

COPY public.logs (log_id, method, "table", status, "timestamp") FROM stdin;
118	GET	culture	success	2023-10-13 10:12:15.478885
119	GET	engrais	success	2023-10-13 10:12:21.705536
120	GET	engrais	success	2023-10-13 10:12:32.129718
121	GET	parcelle	success	2023-10-13 10:12:56.916912
122	GET	parcelle	success	2023-10-13 10:13:05.31883
123	GET	parcelle	success	2023-10-13 10:13:11.991971
124	GET	parcelle	success	2023-10-13 10:13:13.241686
125	GET	parcelle	success	2023-10-13 10:13:17.453748
126	GET	parcelle	success	2023-10-13 10:13:20.640563
127	GET	parcelle	success	2023-10-13 10:13:24.538606
128	GET	date	success	2023-10-13 13:33:02.584041
129	GET	elements_chimiques	success	2023-10-13 13:33:29.707526
130	GET	engrais	success	2023-10-13 13:33:51.24229
131	GET	culture	success	2023-10-13 13:50:08.263152
132	POST	culture	fail	2023-10-13 13:50:18.263538
133	POST	culture	fail	2023-10-13 13:50:19.257759
134	POST	culture	fail	2023-10-13 13:50:20.168298
135	POST	date	success	2023-10-13 13:50:44.211435
136	POST	date	success	2023-10-13 13:50:53.028378
137	GET	date	success	2023-10-13 13:51:04.223857
138	POST	date	fail	2023-10-13 13:52:36.109641
139	GET	date	success	2023-10-13 13:52:41.836175
140	DELETE	engrais	fail	2023-10-13 14:03:08.269473
141	POST	culture	fail	2023-10-13 14:17:09.765342
142	GET	engrais	success	2023-10-13 14:18:16.451461
143	POST	engrais	success	2023-10-13 14:18:40.030659
144	POST	engrais	success	2023-10-13 14:18:42.041222
145	POST	engrais	success	2023-10-13 14:18:42.832946
146	POST	engrais	success	2023-10-13 14:18:43.440383
147	POST	engrais	success	2023-10-13 14:18:44.394104
148	POST	engrais	success	2023-10-13 14:18:55.120977
149	GET	engrais	success	2023-10-13 14:19:02.737129
150	GET	engrais	success	2023-10-13 14:19:11.258838
151	GET	engrais	success	2023-10-13 14:19:22.349904
152	GET	engrais	success	2023-10-13 14:19:36.040927
153	GET	date	success	2023-10-13 14:19:48.17115
154	GET	culture	success	2023-10-13 14:19:54.298222
155	POST	date	success	2023-10-13 14:20:13.213515
156	POST	date	success	2023-10-13 14:20:16.675582
157	POST	culture	fail	2023-10-13 14:20:23.60577
158	POST	parcelle	success	2023-10-13 14:20:53.733515
159	POST	parcelle	success	2023-10-13 14:20:55.955991
160	POST	parcelle	success	2023-10-13 14:20:56.819421
161	GET	culture	success	2023-10-13 14:21:44.041504
162	POST	culture	fail	2023-10-13 14:21:47.963671
163	POST	culture	fail	2023-10-13 14:33:38.808633
164	POST	culture	success	2023-10-13 14:33:50.265053
165	GET	culture	success	2023-10-13 14:34:02.037921
166	GET	date	success	2023-10-13 14:34:10.785932
167	GET	elements_chimiques	success	2023-10-13 14:34:15.136479
168	GET	engrais	success	2023-10-13 14:34:19.486144
169	GET	epandre	success	2023-10-13 14:34:30.741987
170	GET	parcelle	success	2023-10-13 14:34:44.128994
171	GET	parcelle	success	2023-10-13 14:35:00.19429
172	GET	parcelle	success	2023-10-13 14:35:05.638051
173	GET	posseder	success	2023-10-13 14:35:19.612299
174	GET	posseder	success	2023-10-13 14:35:24.979663
175	POST	posseder	fail	2023-10-13 14:35:41.072437
176	POST	posseder	fail	2023-10-13 14:35:42.477838
177	POST	posseder	success	2023-10-13 14:36:41.651918
178	POST	posseder	success	2023-10-13 14:36:44.41678
179	POST	posseder	success	2023-10-13 14:36:45.297333
180	POST	posseder	success	2023-10-13 14:36:46.44777
181	POST	posseder	success	2023-10-13 14:36:46.994893
182	GET	posseder	success	2023-10-13 14:36:50.789385
183	GET	posseder	success	2023-10-13 14:36:57.72999
184	GET	production	success	2023-10-13 14:37:09.918797
185	GET	production	success	2023-10-13 14:37:15.44935
186	GET	un	success	2023-10-13 14:37:26.213192
187	GET	un	success	2023-10-13 14:37:36.137936
\.


--
-- Data for Name: parcelle; Type: TABLE DATA; Schema: public; Owner: database
--

COPY public.parcelle (no_parcelle, surface, nom_parcelle, coordonnees) FROM stdin;
5	467342	parcelle154	56
6	467342	parcelle154	56
7	467342	parcelle154	561
8	467342	parcelle154	561
9	467342	parcelle154	561
10	467342	parcelle154	561
11	4672	parcelle1543	61
12	4672	parcelle1543	61
13	4672	parcelle1543	61
14	4672	parcelle1543	61
15	4672	parcelle1543	61
16	4672	parcelle1543	61
17	4672	parcelle1543	61
18	4672	parcelle1543	61
19	4672	parcelle1543	61
20	4672	parcelle1543	61
21	4672	parcelle1543	61
23	4672	parcelle1543	61
26	4672	new3	61
27	4672	new3	61
28	4672	new3	61
29	4672	new3	61
24	4	new53	61
31	4672	new3	61
32	4672	new3	61
33	4672	new3	61
\.


--
-- Data for Name: posseder; Type: TABLE DATA; Schema: public; Owner: database
--

COPY public.posseder (id_engrais, code_element, valeur) FROM stdin;
5	ae	4
6	Na	100
6	Na	100
6	Na	100
6	Na	100
6	Na	100
\.


--
-- Data for Name: production; Type: TABLE DATA; Schema: public; Owner: database
--

COPY public.production (code_production, un, nom_production) FROM stdin;
2	222	ProdUn
3	111	ProdDeux
4	333	ProdTrois
5	444	ProdQuatre
\.


--
-- Data for Name: un; Type: TABLE DATA; Schema: public; Owner: database
--

COPY public.un (un) FROM stdin;
rtez
rtey
111
222
333
444
10
99
123
456
890
14
2
1
3
4
5
6
7
8
9
945
\.


--
-- Name: culture_identifiant_culture_seq; Type: SEQUENCE SET; Schema: public; Owner: database
--

SELECT pg_catalog.setval('public.culture_identifiant_culture_seq', 12, true);


--
-- Name: engrais_id_engrais_seq; Type: SEQUENCE SET; Schema: public; Owner: database
--

SELECT pg_catalog.setval('public.engrais_id_engrais_seq', 11, true);


--
-- Name: logs_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: database
--

SELECT pg_catalog.setval('public.logs_log_id_seq', 187, true);


--
-- Name: parcelle_no_parcelle_seq; Type: SEQUENCE SET; Schema: public; Owner: database
--

SELECT pg_catalog.setval('public.parcelle_no_parcelle_seq', 33, true);


--
-- Name: production_code_production_seq; Type: SEQUENCE SET; Schema: public; Owner: database
--

SELECT pg_catalog.setval('public.production_code_production_seq', 5, true);


--
-- Name: culture culture_pkey; Type: CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.culture
    ADD CONSTRAINT culture_pkey PRIMARY KEY (identifiant_culture);


--
-- Name: date date_pkey; Type: CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.date
    ADD CONSTRAINT date_pkey PRIMARY KEY (date);


--
-- Name: elements_chimiques elementsChimiques_pkey; Type: CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.elements_chimiques
    ADD CONSTRAINT "elementsChimiques_pkey" PRIMARY KEY (code_element);


--
-- Name: engrais engrais_pkey; Type: CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.engrais
    ADD CONSTRAINT engrais_pkey PRIMARY KEY (id_engrais);


--
-- Name: logs logs_pkey; Type: CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_pkey PRIMARY KEY (log_id);


--
-- Name: parcelle parcelle_pkey; Type: CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.parcelle
    ADD CONSTRAINT parcelle_pkey PRIMARY KEY (no_parcelle);


--
-- Name: production production_pkey; Type: CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.production
    ADD CONSTRAINT production_pkey PRIMARY KEY (code_production);


--
-- Name: un un_pkey; Type: CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.un
    ADD CONSTRAINT un_pkey PRIMARY KEY (un);


--
-- Name: culture cultureParcelle; Type: FK CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.culture
    ADD CONSTRAINT "cultureParcelle" FOREIGN KEY (no_parcelle) REFERENCES public.parcelle(no_parcelle);


--
-- Name: culture cultureProduction; Type: FK CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.culture
    ADD CONSTRAINT "cultureProduction" FOREIGN KEY (code_production) REFERENCES public.production(code_production);


--
-- Name: elements_chimiques elementsChimiquesUnite; Type: FK CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.elements_chimiques
    ADD CONSTRAINT "elementsChimiquesUnite" FOREIGN KEY (un) REFERENCES public.un(un);


--
-- Name: engrais engraisUnite; Type: FK CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.engrais
    ADD CONSTRAINT "engraisUnite" FOREIGN KEY (un) REFERENCES public.un(un);


--
-- Name: epandre epandreDate; Type: FK CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.epandre
    ADD CONSTRAINT "epandreDate" FOREIGN KEY (date) REFERENCES public.date(date);


--
-- Name: epandre epandreEngrais; Type: FK CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.epandre
    ADD CONSTRAINT "epandreEngrais" FOREIGN KEY (id_engrais) REFERENCES public.engrais(id_engrais);


--
-- Name: epandre epandreParcelle; Type: FK CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.epandre
    ADD CONSTRAINT "epandreParcelle" FOREIGN KEY (no_parcelle) REFERENCES public.parcelle(no_parcelle);


--
-- Name: posseder possederElementsChimiques; Type: FK CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.posseder
    ADD CONSTRAINT "possederElementsChimiques" FOREIGN KEY (code_element) REFERENCES public.elements_chimiques(code_element);


--
-- Name: posseder possederEngrais; Type: FK CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.posseder
    ADD CONSTRAINT "possederEngrais" FOREIGN KEY (id_engrais) REFERENCES public.engrais(id_engrais);


--
-- Name: production productionUnite; Type: FK CONSTRAINT; Schema: public; Owner: database
--

ALTER TABLE ONLY public.production
    ADD CONSTRAINT "productionUnite" FOREIGN KEY (un) REFERENCES public.un(un);


--
-- PostgreSQL database dump complete
--


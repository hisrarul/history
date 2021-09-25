CREATE DATABASE codegig;

CREATE TABLE "gigs" (
  "id" serial NOT NULL,
  PRIMARY KEY ("id"),
  "title" character varying(200) NOT NULL,
  "technologies" character varying(200) NOT NULL,
  "budget" character varying(20) NOT NULL,
  "description" text NOT NULL,
  "contact_email" character varying NOT NULL,
  "createdAt" date NOT NULL,
  "updatedAt" date NOT NULL
);
-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Vendo o ocorido.
SELECT description FROM crime_scene_reports WHERE
month = 7 AND day = 28 AND street = "Chamberlin Street";
-- Vendo as testemunhas e seus relatos
SELECT name, transcript FROM interviews
WHERE year = 2020 AND month = 7 AND day = 28;
-- Vendo arquivos do tribunal.
SELECT license_plate, minute FROM courthouse_security_logs
WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute <= 25 AND activity = "exit";
-- Vendo as tranzações do ATM
SELECT account_number, amount FROM atm_transactions
WHERE year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street" AND transaction_type = "withdraw";
-- Vendo as contas bancarias dos possiveis cupados
SELECT person_id, creation_year FROM bank_accounts
WHERE account_number in (SELECT account_number FROM atm_transactions
WHERE year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street");
-- vendo aeroportos
SELECT * FROM airports WHERE city = "Fiftyville";
-- Vendo os voos que aconteceram num dia depois do roubo
SELECT id, origin_airport_id, destination_airport_id, hour FROM flights
WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND hour <= 12 ORDER BY hour;
-- Vindo 

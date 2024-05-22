-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 22 Maj 2024, 09:45
-- Wersja serwera: 10.4.24-MariaDB
-- Wersja PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `sklep_gier_komputerowych`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `gry`
--

CREATE TABLE `gry` (
  `id` int(11) NOT NULL,
  `tytul` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `gry`
--

INSERT INTO `gry` (`id`, `tytul`) VALUES
(1, 'Wiedźmin 3: Dziki Gon'),
(2, 'Cyberpunk 2077'),
(3, 'The Witcher 3: Dziki Gon'),
(4, 'Gothic'),
(5, 'Gothic 2'),
(6, 'Gothic 3'),
(7, 'Assassin\'s Creed Odyssey'),
(8, 'Assassin\'s Creed Valhalla'),
(9, 'Red Dead Redemption 2'),
(10, 'Grand Theft Auto V'),
(11, 'The Elder Scrolls V: Skyrim'),
(12, 'Fallout 4'),
(13, 'FIFA 22'),
(14, 'Call of Duty: Warzone');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `klienci`
--

CREATE TABLE `klienci` (
  `id` int(11) NOT NULL,
  `imie` varchar(100) NOT NULL,
  `nazwisko` varchar(200) NOT NULL,
  `reputacja` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `klienci`
--

INSERT INTO `klienci` (`id`, `imie`, `nazwisko`, `reputacja`) VALUES
(1, 'Jan', 'Kowalski', 5),
(2, 'Anna', 'Nowak', 4),
(3, 'Piotr', 'Wiśniewski', 3),
(4, 'Maria', 'Dąbrowska', 2),
(5, 'Tomasz', 'Lewandowski', 4),
(6, 'Magdalena', 'Wójcik', 3),
(7, 'Marcin', 'Kamiński', 5),
(8, 'Katarzyna', 'Kowalczyk', 4),
(9, 'Paweł', 'Zieliński', 3),
(10, 'Karolina', 'Szymańska', 2),
(11, 'Michał', 'Woźniak', 5),
(12, 'Beata', 'Kozłowska', 4),
(13, 'Adam', 'Jankowski', 3),
(14, 'Natalia', 'Wojciechowska', 2);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `wypozyczenia`
--

CREATE TABLE `wypozyczenia` (
  `id` int(11) NOT NULL,
  `id_klienta` int(11) NOT NULL,
  `id_gry` int(11) NOT NULL,
  `data_wypozyczenia` date NOT NULL DEFAULT curdate(),
  `data_zwrotu` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `wypozyczenia`
--

INSERT INTO `wypozyczenia` (`id`, `id_klienta`, `id_gry`, `data_wypozyczenia`, `data_zwrotu`) VALUES
(1, 1, 1, '2024-05-01', '2024-05-08'),
(2, 2, 3, '2024-05-03', '2024-05-10'),
(3, 3, 5, '2024-05-05', '2024-05-12'),
(4, 4, 7, '2024-05-07', '2024-05-14'),
(5, 5, 9, '2024-05-09', '2024-05-16'),
(6, 6, 11, '2024-05-11', '2024-05-18'),
(7, 7, 13, '2024-05-13', '2024-05-20'),
(8, 8, 2, '2024-05-15', '2024-05-22'),
(9, 9, 4, '2024-05-17', '2024-05-24'),
(10, 10, 6, '2024-05-19', '2024-05-26'),
(11, 11, 8, '2024-05-21', '2024-05-28'),
(12, 12, 10, '2024-05-23', '2024-05-30'),
(13, 13, 12, '2024-05-25', '2024-06-01'),
(14, 14, 14, '2024-05-27', '2024-06-03');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `gry`
--
ALTER TABLE `gry`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `klienci`
--
ALTER TABLE `klienci`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `wypozyczenia`
--
ALTER TABLE `wypozyczenia`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_klienta` (`id_klienta`),
  ADD KEY `id_gry` (`id_gry`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `gry`
--
ALTER TABLE `gry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT dla tabeli `klienci`
--
ALTER TABLE `klienci`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT dla tabeli `wypozyczenia`
--
ALTER TABLE `wypozyczenia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `wypozyczenia`
--
ALTER TABLE `wypozyczenia`
  ADD CONSTRAINT `wypozyczenia_ibfk_1` FOREIGN KEY (`id_klienta`) REFERENCES `klienci` (`id`),
  ADD CONSTRAINT `wypozyczenia_ibfk_2` FOREIGN KEY (`id_gry`) REFERENCES `gry` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

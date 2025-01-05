-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Янв 05 2025 г., 13:30
-- Версия сервера: 10.4.32-MariaDB
-- Версия PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `dis_faceit`
--

-- --------------------------------------------------------

--
-- Структура таблицы `сервер r1cone для разработак`
--

CREATE TABLE `сервер r1cone для разработак` (
  `id` int(11) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `mmr` int(11) NOT NULL,
  `join_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `сервер r1cone для разработак`
--

INSERT INTO `сервер r1cone для разработак` (`id`, `user_id`, `user_name`, `mmr`, `join_date`) VALUES
(1, '705322141683548250', 'r1cone', 100, '2025-01-05 12:26:13'),
(2, '1136243220322455622', 'r1cone90', 100, '2025-01-05 12:26:13'),
(3, '1136574013250994226', 'r1cone92', 100, '2025-01-05 12:26:13'),
(4, '1136577602119802920', 'r1cone091', 100, '2025-01-05 12:26:13'),
(5, '1136578442209542204', 'r1cone93', 100, '2025-01-05 12:26:13'),
(6, '1136579970534215690', 'r1cone94', 100, '2025-01-05 12:26:13'),
(7, '1136581912836718642', 'r1cone95', 100, '2025-01-05 12:26:13'),
(8, '1136582392224677940', 'r1cone96', 100, '2025-01-05 12:26:13'),
(9, '1136584152339206154', 'r1cone97', 100, '2025-01-05 12:26:13'),
(10, '1321857391565864970', 'r1cone98', 100, '2025-01-05 12:26:13'),
(11, '705322141683548250', 'r1cone', 100, '2025-01-05 12:29:28'),
(12, '1136243220322455622', 'r1cone90', 100, '2025-01-05 12:29:28'),
(13, '1136574013250994226', 'r1cone92', 100, '2025-01-05 12:29:28'),
(14, '1136577602119802920', 'r1cone091', 100, '2025-01-05 12:29:28'),
(15, '1136578442209542204', 'r1cone93', 100, '2025-01-05 12:29:28'),
(16, '1136579970534215690', 'r1cone94', 100, '2025-01-05 12:29:28'),
(17, '1136581912836718642', 'r1cone95', 100, '2025-01-05 12:29:28'),
(18, '1136582392224677940', 'r1cone96', 100, '2025-01-05 12:29:28'),
(19, '1136584152339206154', 'r1cone97', 100, '2025-01-05 12:29:28'),
(20, '1321857391565864970', 'r1cone98', 100, '2025-01-05 12:29:28');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `сервер r1cone для разработак`
--
ALTER TABLE `сервер r1cone для разработак`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `сервер r1cone для разработак`
--
ALTER TABLE `сервер r1cone для разработак`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


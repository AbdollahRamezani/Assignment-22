-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 28, 2023 at 09:33 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `todolist_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `tasks`
--

CREATE TABLE `tasks` (
  `id` int(10) NOT NULL,
  `title` varchar(30) COLLATE utf8_persian_ci NOT NULL,
  `description` varchar(256) COLLATE utf8_persian_ci NOT NULL,
  `is_done` int(1) NOT NULL DEFAULT 0,
  `priority` int(1) NOT NULL DEFAULT 0 COMMENT 'mohem=1 , adi=0',
  `time` varchar(256) COLLATE utf8_persian_ci NOT NULL,
  `date` varchar(256) COLLATE utf8_persian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

--
-- Dumping data for table `tasks`
--

INSERT INTO `tasks` (`id`, `title`, `description`, `is_done`, `priority`, `time`, `date`) VALUES
(61, 'cinema', 'tamashay film ba doostam', 0, 0, '00:00:00', ''),
(62, 'ketab', 'kharid ketab python', 1, 1, '00:00:00', ''),
(63, 'football', 'tamashay football', 0, 1, '00:00:00', ''),
(64, 'tamrin', 'anjam tamrin python', 1, 0, '10:20:30', '1402/12/09'),
(67, 'test title', 'test description', 0, 1, '10:10:00', '1402/12/11');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tasks`
--
ALTER TABLE `tasks`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=68;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

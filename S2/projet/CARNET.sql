-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Mar 21, 2020 at 01:30 PM
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `DBbazire`
--

-- --------------------------------------------------------

--
-- Table structure for table `CARNET`
--

CREATE TABLE 'CARNET' (
  'ID' int(11) NOT NULL,
  `NOM` varchar(30) DEFAULT NULL,
  `PRENOM` varchar(30) DEFAULT NULL,
  `NAISSANCE` date DEFAULT NULL,
  `VILLE` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `CARNET`
--

INSERT INTO `CARNET` (`ID`, `NOM`, `PRENOM`, `NAISSANCE`, `VILLE`) VALUES
(1, 'SMITH', 'JOHN', '1980-12-17', 'ORLEANS'),
(2, 'DURAND', 'JEAN', '1983-01-13', 'ORLEANS'),
(3, 'GUDULE', 'JEANNE', '1967-11-06', 'TOURS'),
(4, 'ZAPATA', 'EMILIO', '1956-12-01', 'ORLEANS'),
(5, 'JOURDAIN', 'NICOLAS', '2000-09-10', 'TOURS'),
(6, 'DUPUY', 'MARIE', '1986-01-11', 'BLOIS'),
(7, 'ANDREAS', 'LOU', '1861-02-12', 'ST Petersbourg'),
(9, 'Kafka', 'Franz', '1883-07-03', 'Prague'),
(11, 'Dalton', 'Joe', '2003-12-06', 'Dallas');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `CARNET`
--
ALTER TABLE `CARNET`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `CARNET`
--
ALTER TABLE `CARNET`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

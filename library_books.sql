CREATE DATABASE  IF NOT EXISTS `library` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `library`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win32 (x86)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	5.5.62

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `Book_id` char(4) NOT NULL,
  `Book_Name` varchar(50) NOT NULL,
  `Author` varchar(50) NOT NULL,
  `Genre` varchar(30) NOT NULL,
  `Qty` int(11) NOT NULL,
  `Status` varchar(30) NOT NULL,
  PRIMARY KEY (`Book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('B001','Harry Potter','Jk Rowling','Fantasy',10,'Available'),('B002','Divergent','Veronica Roth','Science Fiction',3,'Available'),('B003','Maze Runner','James Dashner','Science Fiction',3,'Available'),('B004','The Hunger Games','Suzanne Collins','Science Fiction',3,'Available'),('B005','Red Queen','Victoria Aveyard','Drama',2,'Available'),('B006','Looking for Alaska','John Green','Drama',2,'Available'),('B007','The Fault In Our Stars','John Green','Drama',1,'Available'),('B008','The Book Theif','Markus Zusak','Historical Fiction',1,'Available'),('B009','Outrun The Moon','Stacey Lee','Historical Fiction',4,'Available'),('B010','Crossing The Ebenezer Creek','Tonya Bolden','Historical Fiction',3,'Available'),('B011','A Death-struck year','Makiia Lucier','Historical Fiction',2,'Available'),('B012','Wuthering Heights','Emily Bronte','Classics',3,'Available'),('B013','Pride and Prejudice','Jane Austen','Classics',2,'Available'),('B014','Dracula ','Bram Stoker','Classics',1,'Available'),('B015','Treasure Island ','Rober Louis','Classics',1,'Available'),('B016','Murder On The Orient Express ','Agatha Cristie','Mystery',2,'Available'),('B017','The Da Vinci code','Dan Brown','Mystery',2,'Available');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-27 22:25:01

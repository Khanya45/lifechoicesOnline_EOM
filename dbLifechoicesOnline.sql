-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: dbLifechoicesOnline
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tblAdministrator`
--

DROP TABLE IF EXISTS `tblAdministrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblAdministrator` (
  `Name` varchar(50) NOT NULL,
  `Surname` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Admin_id` int unsigned NOT NULL AUTO_INCREMENT,
  `Email` varchar(60) NOT NULL,
  `LogIn` time DEFAULT NULL,
  PRIMARY KEY (`Admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblAdministrator`
--

LOCK TABLES `tblAdministrator` WRITE;
/*!40000 ALTER TABLE `tblAdministrator` DISABLE KEYS */;
INSERT INTO `tblAdministrator` VALUES ('khanya','gope','khanya@2021',1,'khanyagope93@gmail.com','14:39:27'),('bucks','owen','bucks@2021',3,'bucksowen@gmail.com','13:10:37');
/*!40000 ALTER TABLE `tblAdministrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblNextOfKin`
--

DROP TABLE IF EXISTS `tblNextOfKin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblNextOfKin` (
  `Name` varchar(100) NOT NULL,
  `Surname` varchar(100) NOT NULL,
  `Mobile` varchar(100) NOT NULL,
  `User_id` int unsigned DEFAULT NULL,
  KEY `User_id` (`User_id`),
  CONSTRAINT `tblNextOfKin_ibfk_1` FOREIGN KEY (`User_id`) REFERENCES `tblUser` (`User_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblNextOfKin`
--

LOCK TABLES `tblNextOfKin` WRITE;
/*!40000 ALTER TABLE `tblNextOfKin` DISABLE KEYS */;
INSERT INTO `tblNextOfKin` VALUES ('walker','hayes','824565432',2),('sam','hunt','654567876',4),('robert','greene','37564821',9),('jordan','peterson','46372827',10),('gavin','evans','837844847',11),('luke','bryan','7593757',15),('george','strait','45637658',16),('chuck','wicks','0731237349',17),('drake','white','0635462314',19),('carl','jung','0824657364',20),('rob','dials','0726473527',21);
/*!40000 ALTER TABLE `tblNextOfKin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblUser`
--

DROP TABLE IF EXISTS `tblUser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblUser` (
  `Name` varchar(30) NOT NULL,
  `Surname` varchar(30) NOT NULL,
  `ID` varchar(50) NOT NULL,
  `Mobile` varchar(20) NOT NULL,
  `logIn` time DEFAULT NULL,
  `logOut` time DEFAULT NULL,
  `User_id` int unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblUser`
--

LOCK TABLES `tblUser` WRITE;
/*!40000 ALTER TABLE `tblUser` DISABLE KEYS */;
INSERT INTO `tblUser` VALUES ('bongani','gope','7564836453648','0731237349','15:50:19',NULL,2),('kyle','lint','234567219','647382945',NULL,NULL,4),('tom','phillips','73647392','735462735',NULL,NULL,9),('mark','manson','7874653','737556338',NULL,NULL,10),('elon','mask','78465736','7847483',NULL,NULL,11),('mitchell','tenpenny','84756947','8465848',NULL,NULL,15),('keith','urban','58634896','75683457','17:56:29',NULL,16),('billy','ray','0210160451089','0814450796','21:30:45',NULL,17),('morgan','wallen','7587453624351','0876543212','15:33:35','15:33:41',19),('marcus','aurelius','6302265447080','0645362718','15:40:40',NULL,20),('alan','jackson','7307110601087','0721938463','19:40:16',NULL,21);
/*!40000 ALTER TABLE `tblUser` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-09 21:32:24

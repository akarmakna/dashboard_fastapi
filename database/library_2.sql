/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 10.4.32-MariaDB : Database - library_2
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`library_2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `library_2`;

/*Table structure for table `books` */

DROP TABLE IF EXISTS `books`;

CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `books` */

insert  into `books`(`id`,`title`,`author`,`user_id`) values 
(1,'Book Title 1','Author 1',1),
(2,'Book Title 2','Author 2',1),
(3,'Book Title 3','Author 3',10),
(13,'Dewataku','Dewa',10),
(14,'Mbalik papan','Nanda',15);

/*Table structure for table `cities` */

DROP TABLE IF EXISTS `cities`;

CREATE TABLE `cities` (
  `city_code` varchar(10) NOT NULL,
  `city_name` varchar(100) NOT NULL,
  `latitude` decimal(9,6) NOT NULL,
  `longitude` decimal(9,6) NOT NULL,
  PRIMARY KEY (`city_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `cities` */

insert  into `cities`(`city_code`,`city_name`,`latitude`,`longitude`) values 
('BDG','Bandung',-6.917500,107.619100),
('BPN','Balikpapan',-1.266000,116.900000),
('DEN','Denpasar',-8.409500,115.188900),
('JK01','Jakarta',-6.208800,106.845600),
('MED','Medan',3.595200,98.672200),
('MKS','Makassar',-5.147700,119.432800),
('SBY','Surabaya',-7.257500,112.752100),
('SMG','Semarang',-6.993900,110.416200),
('TGL','Tangerang',-6.178400,106.630000),
('YOG','Yogyakarta',-7.795600,110.369500);

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `city_code` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `city_code` (`city_code`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`city_code`) REFERENCES `cities` (`city_code`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `users` */

insert  into `users`(`id`,`username`,`password`,`city_code`) values 
(1,'user1','$2b$12$KIX1Z1Q1Z1Z1Z1Z1Z1Z1Z1u1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1','YOG'),
(2,'user2','$2b$12$KIX1Z1Q1Z1Z1Z1Z1Z1Z1Z1u1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1','YOG'),
(3,'user3','$2b$12$KIX1Z1Q1Z1Z1Z1Z1Z1Z1Z1u1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1','MKS'),
(10,'mif','$2b$12$w54J6Y6/US.5/DBSoTZmyeC/LgCMOTA4p7LNeWiWFV3iT4L8IGcBq','DEN'),
(14,'unun','$2b$12$uIj55TdzAM2FQBOSclpP8etrC0C8S.aoZzJ13ysjQOPYaNOWS3mJi','SMG'),
(15,'nanda','$2b$12$sfOYuXru33MQEjtybvd4M.L0/w8b5kuEARcKquRI0qqv5QX20PhbS','BPN');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

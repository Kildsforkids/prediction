-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3360
-- Время создания: Фев 21 2019 г., 03:31
-- Версия сервера: 5.6.38
-- Версия PHP: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `diagmed`
--

-- --------------------------------------------------------

--
-- Структура таблицы `directory`
--

CREATE TABLE `directory` (
  `id` int(11) NOT NULL,
  `sex` varchar(1) NOT NULL,
  `age` int(11) NOT NULL,
  `tongue` varchar(100) DEFAULT NULL,
  `stomach` varchar(100) DEFAULT NULL,
  `gallbladder_size` double DEFAULT NULL,
  `gallbladder_form` varchar(100) DEFAULT NULL,
  `gallbladder_wall_thickness` double DEFAULT NULL,
  `gallbladder_bending` tinyint(1) DEFAULT NULL,
  `gallbladder_uniformity_of_walls` tinyint(1) DEFAULT NULL,
  `gallbladder_visibility_of_stones` tinyint(1) DEFAULT NULL,
  `gallbladder_lumen_of_bladder` tinyint(1) DEFAULT NULL,
  `pancreas_cysts` tinyint(1) DEFAULT NULL,
  `pancreas_contours` varchar(100) DEFAULT NULL,
  `pancreas_structure` varchar(100) DEFAULT NULL,
  `pancreas_thickness_of_head` double DEFAULT NULL,
  `pancreas_length_of_body` double DEFAULT NULL,
  `pancreas_echogenicity_of_parenchyma` double DEFAULT NULL,
  `pancreas_duct_width` double DEFAULT NULL,
  `FGDS_color` varchar(100) DEFAULT NULL,
  `FGDS_deffects` tinyint(1) DEFAULT NULL,
  `FGDS_walls_mucus` tinyint(1) DEFAULT NULL,
  `FGDS_walls` varchar(100) DEFAULT NULL,
  `FGDS_cardia_closes` tinyint(1) DEFAULT NULL,
  `nausea` tinyint(1) DEFAULT NULL,
  `pain_upper_abdomen` tinyint(1) DEFAULT NULL,
  `upper_quadrant_pain` tinyint(1) DEFAULT NULL,
  `vomiting` tinyint(1) DEFAULT NULL,
  `abdominal_distention` tinyint(1) DEFAULT NULL,
  `pain_on_palpation` tinyint(1) DEFAULT NULL,
  `participation_of_breathing` tinyint(1) DEFAULT NULL,
  `eructation` tinyint(1) DEFAULT NULL,
  `heartburn` tinyint(1) DEFAULT NULL,
  `weight_loss` tinyint(1) DEFAULT NULL,
  `soe` double DEFAULT NULL,
  `amylase` double DEFAULT NULL,
  `pancreatic_amylase` double DEFAULT NULL,
  `lipase` double DEFAULT NULL,
  `trypsin` double DEFAULT NULL,
  `direct_bilirubin` double DEFAULT NULL,
  `total_bilirubin` double DEFAULT NULL,
  `alkaline_phosphatase` double DEFAULT NULL,
  `erythrocytes` double DEFAULT NULL,
  `hemoglobin` double DEFAULT NULL,
  `hematocrit` double DEFAULT NULL,
  `lymphocytes` double DEFAULT NULL,
  `neutrophils` double DEFAULT NULL,
  `platelets` double DEFAULT NULL,
  `leukocytes` double DEFAULT NULL,
  `diagnose` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `directory`
--

INSERT INTO `directory` (`id`, `sex`, `age`, `tongue`, `stomach`, `gallbladder_size`, `gallbladder_form`, `gallbladder_wall_thickness`, `gallbladder_bending`, `gallbladder_uniformity_of_walls`, `gallbladder_visibility_of_stones`, `gallbladder_lumen_of_bladder`, `pancreas_cysts`, `pancreas_contours`, `pancreas_structure`, `pancreas_thickness_of_head`, `pancreas_length_of_body`, `pancreas_echogenicity_of_parenchyma`, `pancreas_duct_width`, `FGDS_color`, `FGDS_deffects`, `FGDS_walls_mucus`, `FGDS_walls`, `FGDS_cardia_closes`, `nausea`, `pain_upper_abdomen`, `upper_quadrant_pain`, `vomiting`, `abdominal_distention`, `pain_on_palpation`, `participation_of_breathing`, `eructation`, `heartburn`, `weight_loss`, `soe`, `amylase`, `pancreatic_amylase`, `lipase`, `trypsin`, `direct_bilirubin`, `total_bilirubin`, `alkaline_phosphatase`, `erythrocytes`, `hemoglobin`, `hematocrit`, `lymphocytes`, `neutrophils`, `platelets`, `leukocytes`, `diagnose`) VALUES
(2, 'M', 51, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'P'),
(3, 'F', 46, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'X');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `directory`
--
ALTER TABLE `directory`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `directory`
--
ALTER TABLE `directory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

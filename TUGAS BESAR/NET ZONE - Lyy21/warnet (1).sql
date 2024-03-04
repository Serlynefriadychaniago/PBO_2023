-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 25 Feb 2024 pada 15.38
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `warnet`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `nota`
--

CREATE TABLE `nota` (
  `ID` int(11) NOT NULL,
  `NAMA_USER` varchar(100) NOT NULL,
  `ID_KOMPUTER` enum('PC01','PC02','PC03','PC04','PC05','PC06','PC07','PC08','PC09','PC10','PC11','PC12','PC13','PC14','PC15','PC16','PC17','PC18','PC19','PC20') NOT NULL,
  `TANGGAL` date NOT NULL,
  `JAM_MULAI` varchar(100) NOT NULL,
  `JAM_SELESAI` varchar(100) NOT NULL,
  `LAMA_WAKTU` varchar(100) NOT NULL,
  `TARIF_PER_JAM` varchar(100) NOT NULL,
  `TOTAL_BAYAR` varchar(100) NOT NULL,
  `STATUS_BAYAR` enum('TAGIHAN','LUNAS') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `nota`
--

INSERT INTO `nota` (`ID`, `NAMA_USER`, `ID_KOMPUTER`, `TANGGAL`, `JAM_MULAI`, `JAM_SELESAI`, `LAMA_WAKTU`, `TARIF_PER_JAM`, `TOTAL_BAYAR`, `STATUS_BAYAR`) VALUES
(1, 'PITRI', 'PC07', '2024-02-25', '10:00 WIB', '11:00 WIB', '1 JAM', 'RP.5000', 'RP.5000', 'TAGIHAN'),
(2, 'DIVA', 'PC10', '2024-02-02', '11:00 WIB', '13:00 WIB', '2 JAM', 'RP.5000', 'RP.10.000', 'TAGIHAN'),
(3, 'ANGGA', 'PC03', '2024-01-31', '15:00 WIB', '16:00 WIB', '1 JAM', 'RP.5000', 'RP.5000', 'LUNAS'),
(4, 'ALFIAN', 'PC02', '2024-01-29', '13:00 WIB', '15:00 WIB', '2 JAM', 'RP.5000', 'RP.10.000', 'LUNAS');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pelanggan`
--

CREATE TABLE `pelanggan` (
  `ID` int(11) NOT NULL,
  `NAMA_USER` varchar(100) NOT NULL,
  `JENIS_KELAMIN` enum('PEREMPUAN','LAKI-LAKI') NOT NULL,
  `EMAIL` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `pelanggan`
--

INSERT INTO `pelanggan` (`ID`, `NAMA_USER`, `JENIS_KELAMIN`, `EMAIL`) VALUES
(1, 'PITRI', 'PEREMPUAN', 'pitri12@gmail.com'),
(2, 'ALFIAN', 'LAKI-LAKI', 'alfian@gmail.com'),
(3, 'ANGGA', 'LAKI-LAKI', 'angga@gmail.com'),
(4, 'DIVA', 'PEREMPUAN', 'diva@gmail.com');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `EMAIL` varchar(255) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `level` enum('admin','dosen','mahasiswa') NOT NULL DEFAULT 'mahasiswa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`ID`, `EMAIL`, `nama`, `password`, `level`) VALUES
(1, 'serlynecha@umc.ac.id', 'Serly ', '$2y$10$BzqqNPejAUyOraPKKKCK2.xbrToZgOq9GnlmBtAMThvtB2zCTg4O.', 'mahasiswa');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `nota`
--
ALTER TABLE `nota`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `NAMA_USER` (`NAMA_USER`);

--
-- Indeks untuk tabel `pelanggan`
--
ALTER TABLE `pelanggan`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `NAMA USER` (`NAMA_USER`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `email` (`EMAIL`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `nota`
--
ALTER TABLE `nota`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT untuk tabel `pelanggan`
--
ALTER TABLE `pelanggan`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

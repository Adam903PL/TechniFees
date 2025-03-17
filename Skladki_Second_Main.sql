-- kod mo¿e siê wykonywaæ do 20s przez userów i loginy 
use master
go
ALTER DATABASE Skladki_TechniSchools SET SINGLE_USER WITH ROLLBACK IMMEDIATE;



if exists (select 1 from sys.databases where name = 'Skladki_TechniSchools')
begin
		drop database Skladki_TechniSchools;
end

create database Skladki_TechniSchools;
go

use Skladki_TechniSchools;
go


create table Student(
    StudentID int identity(1,1) primary key,
    FirstName varchar(255),
    LastName varchar(255),
    LastLogin datetime
)
create table LoginCredits(
    LoginCreditsID int identity(1,1) primary key,
    StudentID int,
    Login varchar(255),
    Password varchar(255),
    User_Email varchar(255),
	MacAddres char(12),
    CONSTRAINT FK_Student_id FOREIGN KEY(StudentID) REFERENCES Student (StudentID)
)

create table FeesHeader(
    FeesID int identity(1,1) primary key,
    TypeName varchar(255),
    Price int,
    DateStart datetime,
    DateEnd datetime
)

create table FeesItems(
    FeesItemsID int identity(1,1) primary key,
    FeesID int,
    StudentID int,
    Status char(3),
    CONSTRAINT FK_Student_2_id FOREIGN KEY(StudentID) REFERENCES Student (StudentID),
    CONSTRAINT FK_Fees_id FOREIGN KEY(FeesID) REFERENCES  FeesHeader (FeesID)
)



go
insert into Student (FirstName,LastName,LastLogin)
values
    ('Adam', 'Pukaluk', '2024-03-17 11:12:00'),
    ('Aleksander', 'D¹browski', '2024-03-14'),
    ('Antoni', 'Barczak', '2024-03-14'),
    ('Cezary', 'Dziuba', '2024-03-14'),
    ('B³a¿ej', 'Ciepiel', '2024-03-14'),
    ('Kuba.L', 'Leœniak', '2024-03-14'),
    ('Kuba.M', 'Mazurek', '2024-03-14'),
    ('Jerzy', 'Wcise³', '2024-03-14'),
    ('Marceli', 'Karman', '2024-03-14'),
    ('Kazik', 'Napora', '2024-03-14'),
    ('Konrad', 'Klautzch', '2024-03-14'),
    ('Ksawery', 'Bloch', '2024-03-14'),
    ('Maksymilian.R', 'Ro¿ek', '2024-03-14'),
    ('Maksymilian.W', 'Wójcik', '2024-03-14'),
    ('Marcel', 'Geba', '2024-03-14'),
    ('Oskar.S', 'Staniszewski', '2024-03-14'),
    ('Micha³.K', 'Karwacki', '2024-03-14'),
    ('Micha³.¯', '¯yszkiewicz', '2024-03-14'),
    ('Mi³osz', 'Kamiñski', '2024-03-14'),
    ('Oskar.K', 'Kurzyna', '2024-03-14'),
    ('Oskar.R', 'Rybczyñski', '2024-03-14'),
    ('Patryk.Z', 'Jurak', '2024-03-14'),
    ('Patryk.J', 'Zaj¹c', '2024-03-14'),
    ('S³awek', 'Kruszyñski', '2024-03-14'),
    ('Szymon', 'Sidor', '2024-03-14'),
    ('Tomek', 'Zaj¹c', '2024-03-14'),
    ('Wiktor', 'Wójcik', '2024-03-14'),
    ('Wiktoria', 'Galkowska', '2024-03-14'),
    ('Wojtek', 'Turkiewicz', '2024-03-14'),
    ('Admin', NULL, '2024-03-17 14:59:00');

go
insert into LoginCredits(StudentID,Login,User_Email)
values
    (1, 'Adam', 'u46_adpuk_lbn@technischools.com'),
    (2, 'Aleksander', 'u59_aldab_lbn@technischools.com'),
    (3, 'Antoni', 'u15_antbar_lbn@technischools.com'),
    (4, 'Cezary', 'u84_cezdzi_lbn@technischools.com'),
    (5, 'B³a¿ej', 'u37_blacie_lbn@technischools.com'),
    (6, 'Kuba.L', 'u91_kulle_lbn@technischools.com'),
    (7, 'Kuba.M', 'u33_kubmaz_lbn@technischools.com'),
    (8, 'Jerzy', 'u46_jerwc_lbn@technischools.com'),
    (9, 'Marceli', 'u22_mackar_lbn@technischools.com'),
    (10, 'Kazik', 'u64_kaznap_lbn@technischools.com'),
    (11, 'Konrad', 'u78_konkla_lbn@technischools.com'),
    (12, 'Ksawery', 'u20_ksablo_lbn@technischools.com'),
    (13, 'Maksymilian.R', 'u52_makroz_lbn@technischools.com'),
    (14, 'Maksymilian.W', 'u28_makwoj_lbn@technischools.com'),
    (15, 'Marcel', 'u94_margeb_lbn@technischools.com'),
    (16, 'Oskar.S', 'u11_oststa_lbn@technischools.com'),
    (17, 'Micha³.K', 'u71_mickar_lbn@technischools.com'),
    (18, 'Micha³.¯', 'u80_miczy_lbn@technischools.com'),
    (19, 'Mi³osz', 'u26_mikka_lbn@technischools.com'),
    (20, 'Oskar.K', 'u14_oskku_lbn@technischools.com'),
    (21, 'Oskar.R', 'u57_oskry_lbn@technischools.com'),
    (22, 'Patryk.Z', 'u06_patjur_lbn@technischools.com'),
    (23, 'Patryk.J', 'u03_patzaj_lbn@technischools.com'),
    (24, 'S³awek', 'u67_slakru_lbn@technischools.com'),
    (25, 'Szymon', 'u89_szyssi_lbn@technischools.com'),
    (26, 'Tomek', 'u38_tomzaj_lbn@technischools.com'),
    (27, 'Wiktor', 'u49_wikwoj_lbn@technischools.com'),
    (28, 'Wiktoria', 'u98_wikgal_lbn@technischools.com'),
    (29, 'Wojtek', 'u70_wojtur_lbn@technischools.com'),
    (30,'Admin','pukaluk.adam505@gmail.com');

use Skladki_TechniSchools 
go
update LoginCredits
set Password = CONVERT(VARCHAR(32), HASHBYTES('MD5', 'pass123'), 2)
where LoginCreditsID = 30

UPDATE LoginCredits
SET Password = CONVERT(VARCHAR(32), HASHBYTES('MD5', 'inne'), 2)
WHERE LoginCreditsID != 30;

go


create procedure Last_Loged_Admin 
as
begin
    update Student set LastLogin = getdate() where StudentID = 30
end
go

use Skladki_TechniSchools 
go
create procedure select_column_tabel @Table varchar(255) 
as  
begin 
    select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = @Table
end
go



go
INSERT INTO FeesHeader(TypeName, Price, DateStart, DateEnd)
VALUES
    ('Pizza', 3, '2024-06-02', '2025-01-01')
go
INSERT INTO FeesItems (FeesID, StudentID, Status)
VALUES
(1, 1, 'Tak'),
(1, 2, 'Nie'),
(1, 3, 'Nie'),
(1, 4, 'Tak'),
(1, 5, 'Nie'),
(1, 6, 'Tak'),
(1, 7, 'Nie'),
(1, 8, 'Nie'),
(1, 9, 'Tak'),
(1, 10, 'Tak'),
(1, 11, 'Nie'),
(1, 12, 'Tak'),
(1, 13, 'Nie'),
(1, 14, 'Tak'),
(1, 15, 'Nie'),
(1, 16, 'Nie'),
(1, 17, 'Tak'),
(1, 18, 'Tak'),
(1, 19, 'Tak'),
(1, 20, 'Nie'),
(1, 21, 'Nie'),
(1, 22, 'Nie'),
(1, 23, 'Tak'),
(1, 24, 'Nie'),
(1, 25, 'Nie'),
(1, 26, 'Tak'),
(1, 27, 'Tak'),
(1, 28, 'Tak'),
(1, 29, 'Nie')
go
use Skladki_TechniSchools 
go


create proc create_labels_and_buttons_sec  @selected_text varchar(60), @selected_column varchar(60)
as
begin
	UPDATE FeesItems  
    SET Status = 'Tak'
    WHERE StudentID = (SELECT StudentID FROM Student WHERE FirstName = @selected_text)
    AND FeesID = (SELECT FeesID FROM FeesHeader WHERE TypeName = @selected_column)
end

go
use Skladki_TechniSchools 
go
create proc get_status @selected_text varchar(60), @selected_column varchar(60)
as
begin
                SELECT Status FROM FeesItems 
                WHERE StudentID = (SELECT StudentID FROM Student WHERE FirstName = @selected_text)
                AND FeesID = (SELECT FeesID FROM FeesHeader WHERE TypeName = @selected_column)
end
go


insert into FeesHeader(TypeName,Price,DateStart,DateEnd)
values('Kwiaty',5,GETDATE(),'2025-05-08')
go
insert into FeesHeader(TypeName,Price,DateStart,DateEnd)
values('Wycieczka',50,GETDATE(),'2026-07-08')
go
insert into FeesHeader(TypeName,Price,DateStart,DateEnd)
values('Woda',50,'2024-01-01','2024-04-04')


go
INSERT INTO FeesItems(FeesID, StudentID, Status)
VALUES
(2, 1, 'Tak'),
(2, 2, 'Nie'),
(2, 3, 'Nie'),
(2, 4, 'Tak'),
(2, 5, 'Nie'),
(2, 6, 'Tak'),
(2, 7, 'Nie'),
(2, 8, 'Nie'),
(2, 9, 'Tak'),
(2, 10, 'Tak'),
(2, 11, 'Nie'),
(2, 12, 'Tak'),
(2, 13, 'Nie'),
(2, 14, 'Tak'),
(2, 15, 'Nie'),
(2, 16, 'Nie'),
(2, 17, 'Tak'),
(2, 18, 'Tak'),
(2, 19, 'Tak'),
(2, 20, 'Nie'),
(2, 21, 'Nie'),
(2, 22, 'Nie'),
(2, 23, 'Tak'),
(2, 24, 'Nie'),
(2, 25, 'Nie'),
(2, 26, 'Tak'),
(2, 27, 'Tak'),
(2, 28, 'Tak'),
(2, 29, 'Nie')
go
INSERT INTO FeesItems(FeesID, StudentID, Status)
VALUES
(3, 1, 'Tak'),
(3, 2, 'Nie'),
(3, 3, 'Nie'),
(3, 4, 'Tak'),
(3, 5, 'Nie'),
(3, 6, 'Tak'),
(3, 7, 'Nie'),
(3, 8, 'Nie'),
(3, 9, 'Tak'),
(3, 10, 'Tak'),
(3, 11, 'Nie'),
(3, 12, 'Tak'),
(3, 13, 'Nie'),
(3, 14, 'Tak'),
(3, 15, 'Nie'),
(3, 16, 'Nie'),
(3, 17, 'Tak'),
(3, 18, 'Tak'),
(3, 19, 'Tak'),
(3, 20, 'Nie'),
(3, 21, 'Nie'),
(3, 22, 'Nie'),
(3, 23, 'Tak'),
(3, 24, 'Nie'),
(3, 25, 'Nie'),
(3, 26, 'Tak'),
(3, 27, 'Tak'),
(3, 28, 'Tak'),
(3, 29, 'Nie')

go
INSERT INTO FeesItems(FeesID, StudentID, Status)
VALUES
(4, 1, 'Tak'),
(4, 2, 'Nie'),
(4, 3, 'Nie'),
(4, 4, 'Tak'),
(4, 5, 'Nie'),
(4, 6, 'Tak'),
(4, 7, 'Nie'),
(4, 8, 'Nie'),
(4, 9, 'Tak'),
(4, 10, 'Tak'),
(4, 11, 'Nie'),
(4, 12, 'Tak'),
(4, 13, 'Nie'),
(4, 14, 'Tak'),
(4, 15, 'Nie'),
(4, 16, 'Nie'),
(4, 17, 'Tak'),
(4, 18, 'Tak'),
(4, 19, 'Tak'),
(4, 20, 'Nie'),
(4, 21, 'Nie'),
(4, 22, 'Nie'),
(4, 23, 'Tak'),
(4, 24, 'Nie'),
(4, 25, 'Nie'),
(4, 26, 'Tak'),
(4, 27, 'Tak'),
(4, 28, 'Tak'),
(4, 29, 'Nie')


go

use Skladki_TechniSchools 
go
create or alter proc newFees 
@FeesName varchar(50), 
@Price decimal(10,2),
@DateStart date,
@DateEnd date
as
begin
begin tran
	if @DateEnd > @DateStart
		begin
				insert into FeesHeader(TypeName,Price,DateStart,DateEnd)
	values(@FeesName,@Price,@DateStart,@DateEnd)

	declare @Code varchar(60) 
	set @Code = (select FeesID from FeesHeader where TypeName = @FeesName)

	insert into FeesItems(FeesID,StudentID,Status)
	values
(@Code, 1,'Nie'),
(@Code, 2,'Nie'),
(@Code, 3,'Nie'),
(@Code, 4,'Nie'),
(@Code, 5,'Nie'),
(@Code, 6,'Nie'),
(@Code, 7,'Nie'),
(@Code, 8,'Nie'),
(@Code, 9,'Nie'),
(@Code, 10,'Nie'),
(@Code, 11,'Nie'),
(@Code, 12,'Nie'),
(@Code, 13,'Nie'),
(@Code, 14,'Nie'),
(@Code, 15,'Nie'),
(@Code, 16,'Nie'),
(@Code, 17,'Nie'),
(@Code, 18,'Nie'),
(@Code, 19,'Nie'),
(@Code, 20,'Nie'),
(@Code, 21,'Nie'),
(@Code, 22,'Nie'),
(@Code, 23,'Nie'),
(@Code, 24,'Nie'),
(@Code, 25,'Nie'),
(@Code, 26,'Nie'),
(@Code, 27,'Nie'),
(@Code, 28,'Nie'),
(@Code, 29,'Nie')
commit tran
		end
		else
			rollback tran
end








go
create or alter proc getPaid @FeesName varchar(50)
as
begin

SELECT FirstName FROM FeesItems as I
left join FeesHeader as  H on I.FeesID = H.FeesID
left join Student as S on I.StudentID = S.StudentID
where H.TypeName = @FeesName and
Status = 'Tak' 

end

go
create or alter proc getNotPaid @FeesName varchar(50)
as
begin

SELECT FirstName FROM FeesItems as I
left join FeesHeader as  H on I.FeesID = H.FeesID
left join Student as S on I.StudentID = S.StudentID
where H.TypeName = @FeesName and
Status = 'Nie' 
end

go
create or alter proc verifyUser @UserName varchar(50),@MacAddres varchar(50)
as
begin
begin tran
	if  not exists (SELECT MacAddres from LoginCredits as LC left join Student as S on S.StudentID = LC.StudentID where S.FirstName =@UserName)
	begin
		update LoginCredits
		set MacAddres = @MacAddres
		where StudentID  = (select StudentID from Student where FirstName = @UserName)
		print'Dodano MacAddres dla ucznia '  + @UserName
		commit tran
	end
	else if (SELECT MacAddres from LoginCredits where StudentID  = (select StudentID from Student where FirstName = @UserName)) = @MacAddres
	begin
		print'Weryfikacja zakoñczona'
		commit tran
	end
	else
	begin
				print'Próba w³amu'
	end

end

go 
create or alter proc cancelPaid @UserName varchar(50), @FeesName varchar(50)
as
begin
begin tran 
if exists (select 1 from FeesItems as Fi
inner join FeesHeader as Fh on Fi.FeesID = Fh.FeesID
left join Student as S on Fi.StudentID = S.StudentID
where S.FirstName = @UserName and Fh.TypeName = @FeesName and
Fi.Status = 'Tak '
)

begin
	update FeesItems
	set Status = 'Nie'
	where FeesID = (select FeesID from FeesHeader where TypeName = @FeesName) and
	StudentID = (select StudentID from Student  where FirstName = @UserName)
	commit tran
end
else	
begin
	print'Wp³¹ta nie zosta³a dokonana'
	rollback tran

end
end

go 
create or alter proc makePaidMan @UserName varchar(50), @FeesName varchar(50)
as
begin
begin tran 
if exists (select 1 from FeesItems as Fi
inner join FeesHeader as Fh on Fi.FeesID = Fh.FeesID
left join Student as S on Fi.StudentID = S.StudentID
where S.FirstName = @UserName and Fh.TypeName = @FeesName and
Fi.Status = 'Nie '
)

begin
	update FeesItems
	set Status = 'Tak'
	where FeesID = (select FeesID from FeesHeader where TypeName = @FeesName) and
	StudentID = (select StudentID from Student  where FirstName = @UserName)
	commit tran
end
else	
begin
	print'Wp³¹ta zosta³a dokonana'
	rollback tran

end
end
	
		
go 
create or alter proc makeNotPaidMan @UserName varchar(50), @FeesName varchar(50)
as
begin
begin tran 
if exists (select 1 from FeesItems as Fi
inner join FeesHeader as Fh on Fi.FeesID = Fh.FeesID
left join Student as S on Fi.StudentID = S.StudentID
where S.FirstName = @UserName and Fh.TypeName = @FeesName and
Fi.Status = 'Nie '
)

begin
	update FeesItems
	set Status = 'Tak'
	where FeesID = (select FeesID from FeesHeader where TypeName = @FeesName) and
	StudentID = (select StudentID from Student  where FirstName = @UserName)
	commit tran
end
else	
begin
	print'Wp³¹ta zosta³a dokonana'
	rollback tran

end
end
	


go
create or alter proc getEmailNotPaidMan @FeesName varchar(50)
as
begin
select User_Email from LoginCredits  as LC
left join Student as S on LC.StudentID = S.StudentID
left join FeesItems as FI on FI.StudentID = S.StudentID
left join FeesHeader as FH on FI.FeesID = FH.FeesID
where FH.TypeName = @FeesName and
FI.Status = 'Nie'
end

go
create or alter proc changeSettingsFees @FeesNameMain varchar(50), @NewFeesName varchar(50), @Price int,@DateStartNew date,@DateEndNew date
as
begin
	declare @MainStartDate date, @MainEndDate date
	set @MainStartDate = (select DateStart from FeesHeader where TypeName = @FeesNameMain)
	set @MainEndDate = (select DateEnd from FeesHeader where TypeName = @FeesNameMain)

	if @NewFeesName IS NULL OR @NewFeesName = ''
		set @NewFeesName = (select TypeName from FeesHeader where TypeName = @FeesNameMain)
	if @Price IS NULL OR @Price = 0
		set @Price = (select Price from FeesHeader where TypeName = @FeesNameMain)
	if @DateStartNew IS NULL OR @DateStartNew = ''
		set @DateStartNew = @MainStartDate
	if @DateEndNew IS NULL OR @DateEndNew = ''
		set @DateEndNew = @MainEndDate

	update FeesHeader
	set TypeName = @NewFeesName,
		Price = @Price,
		DateStart = @DateStartNew,
		DateEnd = @DateEndNew
	where TypeName = @FeesNameMain

	return
end

go 
create or alter proc  user_change_setting @LoginMain varchar(30),@NewLogin varchar(30),@NewEmail varchar(30),@NewPassword varchar(255)
as
begin

	if @NewLogin IS NULL OR @NewLogin  = ''
		set @NewLogin  =  (select Login from  LoginCredits  where Login = @LoginMain)
	if @NewEmail IS NULL OR @NewEmail = ''
		set @NewEmail =  (select User_Email from  LoginCredits  where Login = @LoginMain)
	if @NewPassword IS NULL OR @NewPassword = ''
		set @NewPassword =  (select Password from  LoginCredits  where Login = @LoginMain)

	update LoginCredits
	set Login = @NewLogin,
	User_Email = @NewEmail,
	Password = @NewPassword
	where Login = @LoginMain
end





----- userzy loginy itp
---------------------------------




-- tworzenie usera i loginu admina 
if exists (select 1 from sys.database_principals where name = 'Admin_Techni_Fees')
begin
    drop user  Admin_Techni_Fees;
end

if exists (select 1 from sys.database_principals where name = 'rl_Admin_Techni_Fees')
begin
    drop role rl_Admin_Techni_Fees;
end

declare @kill_cmd nvarchar(max) = '';

select @kill_cmd = @kill_cmd + 'KILL ' + cast(session_id as varchar) + ';'
from sys.dm_exec_sessions
where login_name = 'Admin_Techni_Fees';

exec(@kill_cmd);

if exists (select 1 from sys.server_principals where name = 'Admin_Techni_Fees')
begin
    drop login Admin_Techni_Fees;
end
go

use Skladki_TechniSchools;
go

alter database Skladki_TechniSchools set single_user with rollback immediate;
go


if exists (select * from sys.database_principals where name = 'Admin_Techni_Fees')
begin
    drop user Admin_Techni_Fees;
end


if exists (select * from sys.server_principals where name = 'Admin_Techni_Fees')
begin
	drop login Admin_Techni_Fees;
end

create login Admin_Techni_Fees with password = 'pass123'
create user Admin_Techni_Fees for login  Admin_Techni_Fees
alter role db_owner  add member Admin_Techni_Fees




-- tworzenie usera i loginu do logowania
----------------------------------------------


use Skladki_TechniSchools;
go
-- tworzenie usera i loginu admina 
if exists (select 1 from sys.database_principals where name = 'Login_Techni_Fees')
begin
    drop user Login_Techni_Fees;
end

if exists (select 1 from sys.database_principals where name = 'rl_Login_Techni_Fees')
begin
    drop role rl_Login_Techni_Fees;
end

declare @kill_cmd nvarchar(max) = '';

select @kill_cmd = @kill_cmd + 'KILL ' + cast(session_id as varchar) + ';'
from sys.dm_exec_sessions
where login_name = 'Login_Techni_Fees'

exec(@kill_cmd);

if exists (select 1 from sys.server_principals where name = 'Login_Techni_Fees')
begin
    drop login Login_Techni_Fees;
end
go

use Skladki_TechniSchools;
go




-- Dodawanie nowego u¿ytkownika
use Skladki_TechniSchools;
go
create login Login_Techni_Fees with password = 'pass123'
create user Login_Techni_Fees for login Login_Techni_Fees
create role rl_Login_Techni_Fees 
grant select on LoginCredits to rl_Login_Techni_Fees
grant select on Student to rl_Login_Techni_Fees
alter role rl_Login_Techni_Fees add member Login_Techni_Fees




----------------------DODAWANIE STUDENTA-------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------




use Skladki_TechniSchools
go
-- tworzenie usera i loginu admina 
if exists (select 1 from sys.database_principals where name = 'Student_Techni_Fees')
begin
    drop user Student_Techni_Fees
end

if exists (select 1 from sys.database_principals where name = 'rl_Student_Techni_Fees')
begin
    drop role rl_Student_Techni_Fees
end

declare @kill_cmd nvarchar(max) = '';

select @kill_cmd = @kill_cmd + 'KILL ' + cast(session_id as varchar) + ';'
from sys.dm_exec_sessions
where login_name = 'Student_Techni_Fees'

exec(@kill_cmd)

if exists (select 1 from sys.server_principals where name = 'Student_Techni_Fees')
begin
    drop login Student_Techni_Fees
end
go

use Skladki_TechniSchools;
go




-- Dodawanie nowego u¿ytkownika
create login Student_Techni_Fees with password = 'stud123'
create user Student_Techni_Fees for login Student_Techni_Fees
create role rl_Student_Techni_Fees
grant select, update on dbo.LoginCredits to rl_Student_Techni_Fees
grant select, update on dbo.Student to rl_Student_Techni_Fees
grant select, update on dbo.FeesItems to rl_Student_Techni_Fees
grant select, update on dbo.FeesHeader to rl_Student_Techni_Fees
grant exec on user_change_setting to rl_Student_Techni_Fees;
alter role rl_Student_Techni_Fees add member Student_Techni_Fees



go

-- przywracanie  normalne ustawienia bazy danyc
alter database Skladki_TechniSchools set multi_user


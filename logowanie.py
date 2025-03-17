import customtkinter
from customtkinter import *
import pyodbc
from tkinter import filedialog
from tkinter import Scrollbar
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import traceback
from tkinter import Tk, Frame, Canvas, Scrollbar
from tkcalendar import *
import uuid
import math
import pandas as pd
import hashlib


def zle_dane_logwania():
    messagebox.showerror("Błąd","Błędny login lub chasło spróbuj ponownie")


def logowanie(Login, Pass):
    connection = None
    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        insert_query = f"""
              SELECT Login FROM LoginCredits
              WHERE Login = ? AND Password = ?
        """

        cursor.execute(insert_query, (Login, Pass))
        row = cursor.fetchone()

        if row:
            print(f"Pomyślnie zalogowano jako {Login}")
            app.destroy()
            if Login == "Admin":
                open_admin()
            else:
                open_user(Login=Login)

        else:
            print("Błędny login lub hasło")
            zle_dane_logwania()
    except pyodbc.Error as ex:
        print(f'Błąd połączenia z bazą danych: {ex}')
    finally:
        if connection:
            connection.close()


def open_user(Login):
    print(f"Dostęp do panelu urzytkownika {Login}")

    def show_send_email():
        messagebox.showinfo("Email",
                            "Twoja wiadomość zostałą przekazana do administratora aplikacji dziękujemy za pomoc")

    server = 'localhost'
    database = 'Skladki_TechniSchools'
    username = 'Login_Techni_Fees'
    password = 'SuperHaslo123!'

    # Ciąg połączenia
    connection_string = (
        f"Driver={{ODBC Driver 17 for SQL Server}};"
        f"Server={server};"
        f"Database={database};"
        f"UID={username};"
        f"PWD={password};"
    )

    def ID(Login):
        ID = None

        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            select_id = f"""SELECT StudentID FROM LoginCredits WHERE Login = ?"""
            cursor.execute(select_id, (Login,))

            row = cursor.fetchone()

            if row:
                ID = row[0]

            connection.commit()
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
        finally:
            if connection:
                connection.close()
        return ID

    StudentID = ID(Login)
    print(StudentID)

    def Last_login():
        columns = []
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            select_all = f"""UPDATE Student set Last_login = getdate() WHERE StudentID = '{StudentID}'"""
            # SELECT CURRENT_TIMESTAMP;

            cursor.execute(select_all)
            connection.commit()
            print("Zaktualizowano ostatnie logowanie")
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')

        finally:
            if connection:
                connection.close()
        return columns

    def name_column(StudentID):
        columns = []
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            select_all = f"""SELECT * FROM Student WHERE StudentID = {StudentID}"""
            cursor.execute(select_all)
            connection.commit()
            print()
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')

        finally:
            if connection:
                connection.close()
        return columns

    def date_last():
        last_login = None
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            select_query = f"""SELECT LastLogin FROM Student WHERE StudentID = '{StudentID}'"""
            cursor.execute(select_query)
            result = cursor.fetchone()
            if result:
                last_login = result[0].strftime('%Y-%m-%d')

            connection.commit()
            print("Ostatnie logowanie:", last_login)
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
        finally:
            if connection:
                connection.close()
        return last_login

    last_login = date_last()

    print(last_login)

    def all(StudentID):
        first_name = None
        last_name = None

        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            FName = "SELECT FirstName FROM Student WHERE StudentID = ?"
            cursor.execute(FName, (StudentID,))

            row = cursor.fetchone()

            if row:
                first_name = row[0]

            LName = "SELECT LastName FROM Student WHERE StudentID = ?"
            cursor.execute(LName, (StudentID,))

            row = cursor.fetchone()

            if row:
                last_name = row[0]

            connection.commit()
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
        finally:
            if connection:
                connection.close()
        return first_name, last_name

    all_info = all(StudentID)
    FirstName = all_info[0]
    LastName = all_info[1]

    def email(StudentID):
        email_address = None

        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            select_email = f"""SELECT User_Email FROM LoginCredits WHERE StudentID = ?"""
            cursor.execute(select_email, (StudentID,))

            row = cursor.fetchone()

            if row:
                email_address = row[0]

            connection.commit()
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
        finally:
            if connection:
                connection.close()
        return email_address

    user_email = email(StudentID)

    def info_box():
        messagebox.showinfo("Zmiany",
                            "Zmiany zostały zapisane nastąpi wylogowanie prosze ponowanie uruchomić aplikacje")


    user = customtkinter.CTk()
    user.title(f"Panel składek użytkownika {Login}")
    user.geometry('800x680')
    user.iconbitmap("TechniFees.ico")

    ####################################################
    ####################################################
    ####################################################
    ####################################################
    ####################################################
    custom_font = ("Helvetica", 15, "bold")
    custom_font_column = ("Helvetica", 25, "bold")
    custom_fontb = ("Helvetica", 30, "bold")
    custom_fontc = ("Helvetica", 20, "bold")
    custom_font45 = ("Helvetica", 45)


    def show_new_window():
        def send_email():
            email = "pukaluk.adam505@gmail.com"
            receiver_email = "u46_adapuk_lbn@technischools.com"

            subject = input_err.get()
            message_body = text_area.get('1.0', customtkinter.END)

            msg = MIMEMultipart()

            msg['Subject'] = subject

            msg.attach(MIMEText(message_body, 'plain', 'utf-8'))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            server.login(email, "yiny vvvt ixlz lzfz")

            server.sendmail(email, receiver_email, msg.as_string())

            server.quit()

            print(f"Email has been sent to {receiver_email} with subject: {subject}")
            new_window.destroy()

        def sum_send():
            send_email()
            show_send_email()

        new_window = customtkinter.CTk()
        new_window.geometry('350x400')
        new_window.title("Report errors")
        new_window.iconbitmap("err_send.ico")

        label_err = customtkinter.CTkButton(new_window, text="Report error", fg_color="#0779d4", font=custom_fontb,
                                            width=220, height=38, command=sum_send)
        label_err.pack(side=TOP, pady=(15, 0))

        label_name_err = customtkinter.CTkLabel(new_window, text="Podaj temat emailu", font=custom_font_column)
        label_name_err.pack(side=TOP, pady=(10, 0))

        input_err = customtkinter.CTkEntry(new_window, width=235, height=37)
        input_err.pack(side=TOP, pady=5)

        label_name_test = customtkinter.CTkLabel(new_window, text="Podaj treść emailu", font=custom_font_column)
        label_name_test.pack(side=TOP, pady=(10, 0))

        text_area = customtkinter.CTkTextbox(new_window, width=235, height=200)
        text_area.pack(side=TOP, pady=5)

        new_window.mainloop()

    frame_report_error_settings = customtkinter.CTkFrame(user,width=800,height=50,fg_color='transparent')
    frame_report_error_settings.pack_propagate(False)
    frame_report_error_settings.pack(side=TOP,padx=5,pady=5)


    button_show_errors = customtkinter.CTkButton(frame_report_error_settings, width=80,height=30, text="Report error", font=custom_fontb, command=show_new_window)
    button_show_errors.pack(side=LEFT, anchor=customtkinter.NW, padx=(20, 0), pady=(10, 0))

    def open_user_sett():
        user_sett = customtkinter.CTk()
        user_sett.geometry('400x450')
        user_sett.title("Usetawienia profilu")
        user_sett.iconbitmap("err_send.ico")


        label_setting_name = customtkinter.CTkLabel(user_sett,text='Ustawienia profilu',font=custom_fontb)
        label_setting_name.pack(side=TOP)

        frame_profile = customtkinter.CTkFrame(user_sett, width=200, height=150)
        frame_profile.pack_propagate(False)
        frame_profile.pack(side=TOP, padx=10, pady=5)

        circle = customtkinter.CTkFrame(frame_profile, width=50, height=50, corner_radius=100, fg_color='#274695')
        circle.pack(side=TOP, pady=(10, 0), padx=20)

        frame_rectangle = customtkinter.CTkFrame(frame_profile, width=100, height=50, corner_radius=100,fg_color='#274695')
        frame_rectangle.pack(side=TOP)



        frame_change_login = customtkinter.CTkFrame(user_sett,width=350,height=50,fg_color='transparent')
        frame_change_login.pack_propagate(False)
        frame_change_login.pack(side=TOP,padx=5,pady=5)


        label_login_name = customtkinter.CTkLabel(frame_change_login,text=Login,font=custom_font_column)
        label_login_name.pack(side=LEFT,padx=(0,5))


        enter_new_login = customtkinter.CTkEntry(frame_change_login,width=200,height=40,placeholder_text='Login',font=custom_font_column)
        enter_new_login.pack(side=LEFT)

        frame_change_email = customtkinter.CTkFrame(user_sett, width=350, height=50, fg_color='transparent')
        frame_change_email.pack_propagate(False)
        frame_change_email.pack(side=TOP, padx=5, pady=5)

        label_email_name = customtkinter.CTkLabel(frame_change_email, text="Email:", font=custom_font_column)
        label_email_name.pack(side=LEFT, padx=(0, 5))

        enter_new_email = customtkinter.CTkEntry(frame_change_email, width=150, height=40, placeholder_text='xyz@gmail.com',font=custom_font_column)
        enter_new_email.pack(side=LEFT)



        frame_change_password = customtkinter.CTkFrame(user_sett,width=350,height=50,fg_color='transparent')
        frame_change_password.pack_propagate(False)
        frame_change_password.pack(side=TOP,padx=5,pady=5)


        label_password_name = customtkinter.CTkLabel(frame_change_password,text='Password:',font=custom_font_column)
        label_password_name.pack(side=LEFT,padx=(0,5))


        enter_new_password= customtkinter.CTkEntry(frame_change_password,width=200,height=40,font=custom_font_column)
        enter_new_password.pack(side=LEFT)

        def change_sett():
            if enter_new_email == '':
                if '@' not in enter_new_email.get():
                    messagebox.showinfo('Info', 'Nie poprawny format emailu')
                    user_sett.mainloop()
                    return
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                passgen = generate_md5_hash(enter_new_password.get())

                select_query = f"""exec user_change_setting '{Login}','{enter_new_login.get()}','{enter_new_email.get() }','{passgen}'"""
                
                cursor.execute(select_query)
                cursor.commit()
                messagebox.showinfo('Info','Pomyślnie zmieniono dane')
                user_sett.mainloop()
            except pyodbc.Error as ex:
                messagebox.showerror('Błąd','Podczas działania programu wystąpił błąd skontkuj się z administratoram aplikacji w celu naprawy błędu')
                print(f'Błąd połączenia z bazą danych: {ex}')
            finally:
                if connection:
                    connection.close()

        button_commit_changes = customtkinter.CTkButton(user_sett,width=80,height=40,text='Zapisz',font=custom_fontb,command=change_sett)
        button_commit_changes.pack(anchor='sw',padx=10,pady=10)


        user_sett.mainloop()

    label_setting = customtkinter.CTkButton(frame_report_error_settings,width=50,height=50,text='⚙️',font=custom_fontb,command=open_user_sett)
    label_setting.pack(side=RIGHT,padx=5,pady=5)



    frame_main_fesses_by_user= customtkinter.CTkFrame(user,width=800,height=500,fg_color='transparent')
    frame_main_fesses_by_user.pack_propagate(False)
    frame_main_fesses_by_user.pack(side=TOP,padx=20,pady=20)

    frame_fees_name_price = customtkinter.CTkScrollableFrame(frame_main_fesses_by_user,width=480,height=500)
    frame_fees_name_price.pack(side=LEFT,padx=10,pady=5)


    def get_all_fees_by_user():
        feeses = {}
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            select_email = f"""
            select FH.TypeName,FI.Status,FH.Price,DATEDIFF(DAY,GETDATE(),FH.DateEnd)  as 'Day' from FeesItems as FI
            left join FeesHeader as FH on FI.FeesID = Fh.FeesID
            left join Student as S on FI.StudentID = S.StudentID
            where S.StudentID = {StudentID}
            order by (DATEDIFF(DAY, GETDATE(), FH.DateEnd)) desc
            
            """
            cursor.execute(select_email)
            for row in cursor.fetchall():
                feeses[row.TypeName] = {}
                feeses[row.TypeName]['Status'] = row.Status
                feeses[row.TypeName]['Price'] = row.Price
                feeses[row.TypeName]['Day'] = row.Day
                if row.Status == 'Tak':
                    feeses[row.TypeName]['Color'] = '#099909'
                else:
                    feeses[row.TypeName]['Color'] = '#099909'




        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
        finally:
            if connection:
                connection.close()
        return feeses




    fees_tab = get_all_fees_by_user()
    print(fees_tab)
    frame_date_fees = customtkinter.CTkScrollableFrame(frame_main_fesses_by_user,width=400,height=500)
    frame_date_fees.pack(side=RIGHT,padx=5,pady=5)
    zakonczone_added = False
    aktywne = False

    for i in fees_tab:
        if int(fees_tab[i]['Day']) > 0 and not aktywne:
            label_started_end = customtkinter.CTkLabel(frame_fees_name_price, text="Aktywne", font=custom_fontb)
            label_started_end.pack(side=TOP,pady=5)

            label_started_end = customtkinter.CTkLabel(frame_date_fees, text="Koniec za", font=custom_fontb)
            label_started_end.pack(side=TOP,pady=5)
            aktywne = True


        if int(fees_tab[i]['Day']) < 0 and not zakonczone_added:
            label_started_end = customtkinter.CTkLabel(frame_fees_name_price, text="Zakończone", font=custom_fontb)
            label_started_end.pack(side=TOP,pady=5)

            label_started_end = customtkinter.CTkLabel(frame_date_fees, text="Skończone ", font=custom_fontb)
            label_started_end.pack(side=TOP,pady=5)
            zakonczone_added = True

        frame_fees_user = customtkinter.CTkFrame(frame_fees_name_price, width=440, height=50,fg_color='#333333')
        frame_fees_user.pack_propagate(False)
        frame_fees_user.pack(side=TOP, padx=20, pady=10)



        status_text = 'Wpłacono' if fees_tab[i]['Status'] == 'Tak' else 'Nie wpłacono'
        label_fees_info_by_user = customtkinter.CTkLabel(frame_fees_user,text=f"{i}: {status_text} {fees_tab[i]['Price']} zł",font=custom_font_column)
        label_fees_info_by_user.pack(side=LEFT, padx=5, pady=5)


        frame_fees_user_days = customtkinter.CTkFrame(frame_date_fees, width=80, height=50,fg_color='#333333')
        frame_fees_user_days.pack_propagate(False)
        frame_fees_user_days.pack(side=TOP,pady=10)

        day_final = fees_tab[i]['Day']
        if day_final < 0:
            day_final *= -1
        label_fees_info_by_user_days = customtkinter.CTkLabel(frame_fees_user_days,text=f"{day_final}",font=custom_font_column)
        label_fees_info_by_user_days.pack(side=TOP,pady=(10,0))



        for j in fees_tab[i]:
            print(j)









    user.mainloop()
    # Last_login()

































def open_admin():


    #### ZROBIĆ WSZYSTKIE ZAPYTANIE NA PROCKI ITP ITD

    def update_mac_address():
        mac_address = uuid.getnode()
        mac_address_formatted = ':'.join(
            ['{:02x}'.format((mac_address >> elements) & 0xff) for elements in range(0, 2 * 6, 2)][::-1])
        return mac_address_formatted

    MacAddres = update_mac_address()
    UserName = 'Admin'
    print(MacAddres)
    print(len(MacAddres))

    server = 'localhost'
    database = 'Skladki_TechniSchools'
    username = 'Login_Techni_Fees'
    password = 'SuperHaslo123!'

    # Ciąg połączenia
    connection_string = (
        f"Driver={{ODBC Driver 17 for SQL Server}};"
        f"Server={server};"
        f"Database={database};"
        f"UID={username};"
        f"PWD={password};"
    )
    #
    # def verify(student_name,MacAddres):
    #     connection = None
    #     try:
    #         connection = pyodbc.connect(connection_string)
    #         cursor = connection.cursor()
    #
    #         query = f"execute verifyUser '{student_name}', '{MacAddres}'"
    #
    #         cursor.execute(query)
    #
    #
    #         print('Działą verifykacja')
    #
    #         connection.commit()
    #     except pyodbc.Error as ex:
    #         print(f'Błąd połączenia z bazą danych: {ex}')
    #
    #     finally:
    #         if connection:
    #             connection.close()

    #
    #
    # verify(UserName,MacAddres)
    #

    def show_error_popup():
        messagebox.showerror("Błąd", "Błedne dane. Sprawdź czy podane przez ciebie dane istnieją w bazie danych")

    def show_error_no_text_in_input_send_email():
        messagebox.showerror("Błąd", "Nie wprowadzon wiadomości")

    def column_not_exsist():
        messagebox.showinfo("Informacja", "Podana columna nie istnieje")

    def wrong_column_name():
        messagebox.showinfo("Informacja", "Nie możesz wprowadźić danych do tej columny ")

    def not_data_in_input_inf():
        messagebox.showinfo("Informacja", "Nie wprowadzono danych")

    def file_import_error():
        messagebox.showerror("Błąd",
                             "Sprawdź czy podana przez ciebie columna istnieje w bazie danych oraz czy plik z któego importujesz dane ma 29 lini")

    def not_exist_file():
        messagebox.showinfo("Informacja", "Nie wprowadzono pliku")

    def show_send_email():
        messagebox.showinfo("Email",
                            "Twoja wiadomość zostałą przekazana do administratora aplikacji dziękujemy za pomoc")

    def succesful_data_go():
        messagebox.showinfo("Informacja", "Twoje dane zostały pomyślnie dodane!!!")

    def Last_login():
        columns = []
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            select_all = f"""execute  Last_Loged_Admin"""
            cursor.execute(select_all)
            connection.commit()
            print("Zaktualizowano ostatnie logowanie dla admina")
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')

        finally:
            if connection:
                connection.close()
        return columns

    Last_login()

    # def add_column(column_name, column_type, check, tabel, nullable):
    #     connection = None
    #
    #     try:
    #         connection = pyodbc.connect(connection_string)
    #         cursor = connection.cursor()
    #
    #         if nullable == False:
    #             nullable_clause = "NULL"
    #         else:
    #             nullable_clause = "NOT NULL"
    #
    #         if check == '':
    #             insert_query = f"""
    #             ALTER TABLE {tabel}
    #             ADD {column_name} {column_type} {nullable_clause};
    #             """
    #         else:
    #             insert_query = f"""
    #             ALTER TABLE {tabel}
    #             ADD {column_name} {column_type} {nullable_clause} CHECK({column_name} <= {check});
    #             """
    #
    #         cursor.execute(insert_query)
    #         connection.commit()
    #
    #         print(f"Nowa kolumna '{column_name}' została dodana pomyślnie.")
    #         succesful_data_go()
    #     except pyodbc.Error as ex:
    #         show_error_popup()
    #         print(f'Błąd połączenia z bazą danych: {ex}')
    #     finally:
    #         if connection:
    #             connection.close()

    def add_column(column_name, column_type, tabel, check):
        connection = None

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            if check == None:
                insert_query = f"""
                    ALTER TABLE {tabel}
                    ADD {column_name} {column_type} CONSTRAINT CK_{column_name}  NULL ;  
                    """
            else:
                insert_query = f"""
                    ALTER TABLE {tabel}
                    ADD {column_name} {column_type} CONSTRAINT CK_{column_name} CHECK ({column_name} <= {check}) NULL;  
                """

            cursor.execute(insert_query)
            connection.commit()

            print(f"Nowa kolumna '{column_name}' została dodana pomyślnie.")
            succesful_data_go()
        except pyodbc.Error as ex:
            show_error_popup()
            print(f'Błąd połączenia z bazą danych: {ex}')
        finally:
            if connection:
                connection.close()

    def succeful_dell_column():
        messagebox.showinfo("Informacja", "Pomyślnie usunięto columne")

    ##tutaj

    def del_column(column_to_delete):
        tabel = combo_box_tabels_in_frame_main.get()
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            if column_to_delete == "exit":
                exit()

            alter_constraint_query = f"""
               ALTER TABLE {tabel}
               DROP CONSTRAINT CK_{column_to_delete}
               """

            cursor.execute(alter_constraint_query)

            alter_column_query = f"""
                ALTER TABLE {tabel}
                DROP COLUMN {column_to_delete}
            """
            cursor.execute(alter_column_query)
            connection.commit()

            print(f"Kolumna '{column_to_delete}' została usunięta pomyślnie.")
            succeful_dell_column()
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
            show_error_popup()
        except pyodbc.ProgrammingError as ex:
            print(f"Kolumna '{column_to_delete}' nie istnieje.")
            column_not_exsist()
        finally:
            if connection:
                connection.close()

    def del_column_button_click_2():
        column_to_delete = input_name_colum_to_dell.get()
        del_column(column_to_delete)

    # def add_data(last_name, column, data):
    #     connection = None
    #     try:
    #         connection = pyodbc.connect(connection_string)
    #         cursor = connection.cursor()
    #
    #         update_query = f"""
    #               UPDATE Skladki
    #               SET {column} = '{data}'
    #               WHERE LastName = '{last_name}'
    #               """
    #
    #         cursor.execute(update_query)
    #         connection.commit()
    #
    #         print("Dane dodane pomyślnie.")
    #         succesful_data_go()
    #     except pyodbc.Error as ex:
    #         print(f'Błąd połączenia z bazą danych: {ex}')
    #         show_error_popup()
    #
    #     finally:
    #         if connection:
    #             connection.close()

    def succesful_dell_data():
        messagebox.showinfo("Informacja", "Pomyślnie usunięto dane")

    def remove_data(last_name, column):
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            update_query = f"""
            UPDATE Skladki
            SET {column} = NULL
            WHERE LastName = '{last_name}'
            """
            # zmiennej tabeli nie można do procki
            cursor.execute(update_query)
            connection.commit()

            print(f"Dane z kolumny {column} usunięte pomyślnie dla ucznia {last_name}.")
            succesful_dell_data()
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
            show_error_popup()

        finally:
            if connection:
                connection.close()

    def succesful_mod_data():
        messagebox.showinfo("Informacje", "Pomyślnie zmodyfikowano daną")

    def mod_dane():
        column_name = input_column_name_modify.get()
        id = input_id_modify.get()
        value = input_value_mod.get()
        main_id = main_id_mod.get()

        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            update_query = f"""
            UPDATE {combo_box_tabels.get()}
            SET {column_name} = '{value}'
            WHERE {main_id} = '{id}'
            """
            # zmiennej tabeli nie można do procki
            cursor.execute(update_query)
            connection.commit()

            succesful_mod_data()
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
            show_error_popup()

        finally:
            if connection:
                connection.close()

    def succesful_dell_all_data_column():
        messagebox.showinfo("Informacja", "Pomylnie usunięto wszystkie dane z wybranej columny")

    def delete_data_from_column(column_name):
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            delete_query = f"""
            UPDATE {combo_box_tabels.get()}
            SET {column_name} = NULL
            """
            # zmiennej tabeli nie można do procki
            cursor.execute(delete_query)
            connection.commit()

            print(f'Wszystkie dane z kolumny {column_name} zostały usunięte pomyślnie.')
            succesful_dell_all_data_column()
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
            show_error_popup()

        finally:
            if connection:
                connection.close()

    def delete_data_button_click():
        column_name = input_column_name_dell_all_data_from_column.get()

        if column_name:
            delete_data_from_column(column_name)
        else:
            print("Wprowadź nazwę kolumny.")
            show_error_popup()

    def choose_file():
        file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        input_file.delete(0, END)
        input_file.insert(0, file_path)

    def succesful_import_data_to_column():
        messagebox.showinfo("Informcaja", "Pomyśnie zaimportowano wszystkie dane z pliku")

    def can_not_add_data_to_this_tabel():
        messagebox.showinfo("Informcaja", "Nie możesz dodać wielu danych do tej tabeli")

    def import_data_from_file():
        # do naprawienia jak skońćze konfigurować to coś z danymi tak/nie
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            column_name = input_column_name.get()
            file_path = input_file.get()
            tabel_name = combo_box_tabels_in_frame_main.get()
            if tabel_name == "HeaderSkładki":
                can_not_add_data_to_this_tabel()
            else:
                if not column_name:
                    print("Nazwa kolumny nie została wprowadzona.")
                    not_data_in_input_inf()
                    return

                if not file_path:
                    print("Nie wybrano pliku.")
                    not_exist_file()
                    return

                with open(file_path, 'r', encoding='utf-8') as plik:
                    for i, linia in enumerate(plik, start=1):
                        data_value = linia.strip()
                        insert_query = f"""
                        UPDATE {tabel_name}
                        SET {column_name} = '{data_value}'
                        WHERE StudentID = {i}
                        """
                        # zmiennej tabeli nie można do procki
                        cursor.execute(insert_query)
                        connection.commit()

                        print(f"Dane '{data_value}' dodane do wiersza {i} w kolumnie {column_name}.")

                print("Import danych z pliku zakończony pomyślnie.")
                succesful_import_data_to_column()


        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
            file_import_error()

        finally:
            if connection:
                connection.close()

    def display_columns():
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{combo_box_tabels.get()}'")
            columns = [row.COLUMN_NAME for row in cursor.fetchall()]
            columns_text = "\n".join(columns)
            label_column.configure(text=columns_text)

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} display_columns')

        finally:
            if connection:
                connection.close()

    def refresh_columns():
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{combo_box_tabels.get()}'")
            columns = [row.COLUMN_NAME for row in cursor.fetchall()]
            columns_text = "\n".join(columns)
            label_column.configure(text=columns_text)


        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} , dla funkcji refresh_column')

        finally:
            if connection:
                connection.close()

    def refresh_name_column():
        name_column()
        # name_column() to pod

    def name_column():
        columns = []
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute("select TypeName from FeesHeader")
            columns = [row.TypeName for row in cursor.fetchall()]

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}, dla funkcji name_column')

        finally:
            if connection:
                connection.close()
        return columns

    fees_name = name_column()

    # def refresh_combobox():
    #     column = name_column()
    #     input_acc['values'] = column

    def show_new_window():
        def send_email():
            email = "pukaluk.adam505@gmail.com"
            receiver_email = "u46_adapuk_lbn@technischools.com"

            subject = input_err.get()
            message_body = text_area.get('1.0', customtkinter.END)

            msg = MIMEMultipart()

            msg['Subject'] = subject

            msg.attach(MIMEText(message_body, 'plain', 'utf-8'))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            server.login(email, "yiny vvvt ixlz lzfz")

            server.sendmail(email, receiver_email, msg.as_string())

            server.quit()

            print(f"Email has been sent to {receiver_email} with subject: {subject}")
            new_window.destroy()

        def sum_send():
            send_email()
            show_send_email()

        new_window = customtkinter.CTk()
        new_window.geometry('350x400')
        new_window.title("Report errors")
        new_window.iconbitmap("err_send.ico")

        label_err = customtkinter.CTkButton(new_window, text="Report error", fg_color="#0779d4",
                                            font=custom_font_biggest, width=220, height=38, command=sum_send)
        label_err.pack(side=TOP, pady=(15, 0))

        label_name_err = customtkinter.CTkLabel(new_window, text="Podaj temat emailu", font=custom_font_column)
        label_name_err.pack(side=TOP, pady=(10, 0))

        input_err = customtkinter.CTkEntry(new_window, width=235, height=37)
        input_err.pack(side=TOP, pady=5)

        label_name_test = customtkinter.CTkLabel(new_window, text="Podaj treść emailu", font=custom_font_column)
        label_name_test.pack(side=TOP, pady=(10, 0))

        text_area = customtkinter.CTkTextbox(new_window, width=235, height=200)
        text_area.pack(side=TOP, pady=5)

        new_window.mainloop()

    #                                       CHECKPOINT MORDO
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################

    root = customtkinter.CTk()
    root.title('App TechniSchools Lublin - Składki Klasa IA ')
    root.geometry('1920x1080')
    root.iconbitmap("FeesLogo.ico")

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    custom_font = ("Helvetica", 15, "bold")
    custom_font_column = ("Helvetica", 25, "bold")
    custom_font_biggest = ("Helvetica", 30, "bold")
    custom_font_35 = ("Helvetica", 35, "bold")
    custom_fontc = ("Helve  tica", 20, "bold")
    custom_fontd = ("Helve  tica", 17, "bold")
    font_acc_label = ("Helvetica", 20, "bold")
    custom_font_test = ("Helvetica", 40, "bold")
    custom_font_very_big = ("Helvetica", 60, "bold")

    button_show_errors = customtkinter.CTkButton(master=root, width=20, text="Report error", font=custom_fontc,
                                                 command=show_new_window)
    button_show_errors.pack(side=customtkinter.TOP, anchor=customtkinter.NW, padx=(80, 0), pady=(10, 0))

    tabview = customtkinter.CTkTabview(master=root, width=250, height=1040)
    tabview.pack(side=LEFT, padx=20, pady=(2, 10))

    tabview.add("Accept")
    tabview.set("Accept")

    label_acc = customtkinter.CTkLabel(master=tabview.tab("Accept"), text="Accept", fg_color="#0779d4",
                                       font=custom_font_biggest, width=180, height=38, corner_radius=10)
    label_acc.pack(side=TOP, pady=(0, 0))

    frame_tks = customtkinter.CTkFrame(master=tabview.tab("Accept"))

    frame_tks.pack(side=TOP, pady=10)

    label_acc = customtkinter.CTkLabel(frame_tks, text="Wybierz składke", font=custom_fontc)
    label_acc.pack(side=LEFT, padx=5)

    def multiple_resrefh_is_paid():
        refresh_tabview_sec()
        refresh_after_change_to_yes()

    button_rfresh_if_paid = customtkinter.CTkButton(frame_tks, font=custom_font_column, width=30, height=30, text="⟳",
                                                    fg_color="#0779d4", corner_radius=10,
                                                    command=multiple_resrefh_is_paid)
    button_rfresh_if_paid.pack(side=RIGHT)

    input_acc = customtkinter.CTkComboBox(master=tabview.tab("Accept"), values=fees_name)
    input_acc.pack(side=TOP, padx=(0, 0), pady=(0, 0))

    frame_acc_a = customtkinter.CTkFrame(master=tabview.tab("Accept"), width=100)
    frame_acc_a.pack(side=TOP)

    def get_all_first_names():
        first_names = []

        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT FirstName FROM Student")
            for row in cursor.fetchall():
                if row.FirstName != 'Admin':
                    first_names.append(row.FirstName)

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}, dla def get_all_first_names')

        finally:
            if connection:
                connection.close()

        return first_names if first_names else []

    column = get_all_first_names()

    another_tab_view_xd = customtkinter.CTkTabview(master=frame_acc_a, width=200)
    another_tab_view_xd.pack()

    another_tab_view_xd.add("First")
    another_tab_view_xd.set("First")

    frame_to_objext_paid_make = customtkinter.CTkScrollableFrame(master=another_tab_view_xd.tab("First"), width=200,
                                                                 height=1000, fg_color='transparent')
    frame_to_objext_paid_make.pack(side=TOP)

    def refresh_after_change_to_yes():
        for widget in frame_to_objext_paid_make.winfo_children():
            widget.destroy()


        create_labels_and_buttons()


    def get_status(student_name):
        status = None
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            query = f"""
                SELECT FI.Status
                FROM FeesItems FI
                INNER JOIN Student S ON FI.StudentID = S.StudentID
                WHERE S.FirstName = ?
                AND  FeesID = (SELECT FeesID from FeesHeader where TypeName = '{input_acc.get()}')
            """

            cursor.execute(query, student_name)
            row = cursor.fetchone()
            if row:
                status = row[0]

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}, dla def get_status')

        finally:
            if connection:
                connection.close()

        return status

    def set_button_color(button, status):
        if status == 'Tak':
            button.configure(fg_color="#099909")
        else:
            button.configure(fg_color="#bf0202")

    def sucesful_change_to_yes(name):
        messagebox.showinfo("Info", f"Pomyślnie zaktualizowano wpłate dla ucznia {name}")

    def already_paid(name):
        messagebox.showinfo("Info", f"Uczeń {name} już dokonał wpłaty")

    def create_labels_and_buttons():
        def button_action(selected_text, selected_column):
            connection = None
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()

                check_query = f"""
                    exec get_status '{selected_text}','{selected_column}'
                """

                cursor.execute(check_query)
                row = cursor.fetchone()
                if row and row[0] == "Tak":
                    already_paid(selected_text)
                else:
                    update_query = f"""
                        execute create_labels_and_buttons_sec '{selected_text}','{selected_column}'
                    """

                    cursor.execute(update_query)
                    connection.commit()

                    print(f'Zaktualizowano kolumnę "{selected_column}" dla studenta o imieniu "{selected_text}".')
                    sucesful_change_to_yes(selected_text)
                    refresh_tabview_sec()
                    refresh_after_change_to_yes()




            except pyodbc.Error as ex:
                print(f'Błąd połączenia z bazą danych: {ex} , dla def button_action tego pierszego')
                wrong_column_name()

            finally:
                if connection:
                    connection.close()

        for i in range(0, 29):

            if i < len(column):
                student_name = column[i]
            else:
                student_name = "Brak danych"

            frame_main_fir_but = customtkinter.CTkFrame(master=frame_to_objext_paid_make)
            frame_main_fir_but.pack(side=TOP, pady=(10, 0))

            label_name = customtkinter.CTkLabel(master=frame_main_fir_but, width=100, height=15, text=student_name)
            label_name.pack(side=LEFT, padx=5, pady=5)

            button = customtkinter.CTkButton(
                master=frame_main_fir_but,
                width=100,
                height=15,
                text=f"Wpłacone",
                command=lambda name=student_name: button_action(name, input_acc.get())
            )
            status = get_status(student_name)
            set_button_color(button, status)

            button.pack(side=RIGHT, padx=5, pady=5)



    def select_tabels_from_database():
        tabels = []

        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES")
            tabels = [row.TABLE_NAME for row in cursor.fetchall()]


        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} select_tabels_from_database')

        finally:
            if connection:
                connection.close()
        return tabels

    tables_list = select_tabels_from_database()

    create_labels_and_buttons()


    tabview.add("Columns")
    tabview.set("Columns")

    #                                       CHECKPOINT MORDO
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    #                                      VERY IMPORTANT BRO

    # label_sett = customtkinter.CTkLabel(master=tabview.tab("Columns"), text="Columny", fg_color="#0779d4",font=custom_font_biggest, width=180, height=38)
    # label_sett.pack(side=TOP, pady=(0, 0)) może się przyda ale raczej nie

    select_tabels_from_database()

    frame_select_tabels_and_refresh = customtkinter.CTkFrame(master=tabview.tab("Columns"))
    frame_select_tabels_and_refresh.pack(side=TOP)

    combo_box_tabels = customtkinter.CTkComboBox(master=frame_select_tabels_and_refresh, font=custom_fontd, width=160,
                                                 height=25, values=tables_list)
    combo_box_tabels.pack(side=LEFT, pady=10)

    # def refresh_name_column_sec():
    # name_column()

    def name_column_sec():
        columns = []
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute(
                f"exec select_column_tabel '{combo_box_tabels.get()}'")  # coś może nie działac sprawdzić w przysżłości pozdrawiam
            columns = [row.COLUMN_NAME for row in cursor.fetchall()]

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} name_column_sec')

        finally:
            if connection:
                connection.close()
        return columns

    def column_content_sec(column_name):
        connection = None
        try:
            connection = pyodbc.connect(connection_string)

            cursor = connection.cursor()

            query = f"SELECT {column_name} FROM {combo_box_tabels.get()}"
            cursor.execute(query)

            column_data = [row[0] for row in cursor.fetchall()]

            return column_data

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} column_content_sec')
            show_error_popup()

        finally:
            if connection:
                connection.close()

    def select_column_from_tabel_to_comb(tabel):
        connection = None
        try:
            connection = pyodbc.connect(connection_string)

            cursor = connection.cursor()

            query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tabel}'"
            cursor.execute(query)  # NIE DZIAŁA 1242 linia kod sprawdzić

            column_data_from_tabel = [row[0] for row in cursor.fetchall()]
            print(column_data_from_tabel)
            return column_data_from_tabel

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
            show_error_popup()

        finally:
            if connection:
                connection.close()

    def refresh_tabview_sec():
        global tabview
        tabview.destroy()
        tabview = customtkinter.CTkTabview(master=frame_use_inny, width=250, height=1040)
        tabview.pack(side=LEFT, padx=5, pady=5)

        columns = name_column_sec()
        for i, column_name in enumerate(columns):
            tabview.add(i)

            frame_scroll = customtkinter.CTkScrollableFrame(master=tabview.tab(i), height=900)
            frame_scroll.pack()

            label_data = customtkinter.CTkLabel(master=frame_scroll, text="", font=custom_font)
            label_data.pack(pady=(2, 0))

            data = column_content_sec(column_name)

            formatted_data = f"\n ".join(map(str, data))
            label_data.configure(text=formatted_data)

    def multiple_refresh():
        refresh_tabview_sec()
        refresh_columns()
        refresh_name_column()

    button_rfresh_all_columns = customtkinter.CTkButton(master=frame_select_tabels_and_refresh, font=custom_font_column,
                                                        width=30, height=30, text="⟳", fg_color="#0779d4",
                                                        corner_radius=10, command=multiple_refresh)
    button_rfresh_all_columns.pack(side=RIGHT, padx=5)

    frame_use_inny = customtkinter.CTkFrame(master=tabview.tab("Columns"))
    frame_use_inny.pack()

    label_column = customtkinter.CTkLabel(frame_use_inny, text="", font=custom_font, width=200)
    label_column.pack(pady=(0, 0))

    tabview = customtkinter.CTkTabview(master=frame_use_inny, width=250, height=1040)
    tabview.pack(side=LEFT, padx=5, pady=2)

    columns = name_column_sec()

    for i, column_name in enumerate(columns):
        tabview.add(i)

        frame_scroll = customtkinter.CTkScrollableFrame(master=tabview.tab(i), height=900)
        frame_scroll.pack()

        label_data = customtkinter.CTkLabel(master=frame_scroll, text="", font=custom_font)
        label_data.pack(pady=(2, 0))

        data = column_content_sec(column_name)

        formatted_data = f"\n ".join(map(str, data))
        label_data.configure(text=formatted_data)

    def refresh_combobox():
        selected_table = combo_box_tabels_in_frame_main.get()
        columns = select_column_from_tabel_to_comb(selected_table)
        input_name_colum_to_dell['values'] = columns

    tabview_main = customtkinter.CTkTabview(master=root, width=1600, height=1040)
    tabview_main.pack(side=RIGHT, padx=20)

    tabview_main.add("Zarządzanie bazą danych")
    tabview_main.set("Zarządzanie bazą danych")

    tabview_main.add("Składki")
    tabview_main.set("Składki")

    frame_group = customtkinter.CTkFrame(tabview_main.tab("Składki"), width=700, height=130, fg_color='transparent')
    frame_group.pack_propagate(False)
    frame_group.pack(anchor='nw', padx=20, pady=10)

    frame_add_fees = customtkinter.CTkFrame(frame_group, width=300, height=130, fg_color='#333333')
    frame_add_fees.pack_propagate(False)
    frame_add_fees.pack(side=LEFT)

    frame_show_fees_by_student = customtkinter.CTkFrame(frame_group, width=300, height=130, fg_color='#333333')

    frame_show_fees_by_student.pack_propagate(False)
    frame_show_fees_by_student.pack(side=LEFT, padx=20)

    students = get_all_first_names()

    label_show_student = customtkinter.CTkLabel(frame_show_fees_by_student, font=custom_font_biggest,
                                                text="Historia ucznia")

    label_show_student.pack(side=TOP, padx=10, pady=10)

    frame_gorup_student_ang_go_to_fees_user = customtkinter.CTkFrame(frame_show_fees_by_student, height=60,
                                                                     fg_color='transparent', width=300)
    # frame_gorup_student_ang_go_to_fees_user.pack_propagate(False)

    frame_gorup_student_ang_go_to_fees_user.pack(side=TOP, padx=10, pady=10)

    combobox_student = customtkinter.CTkComboBox(frame_gorup_student_ang_go_to_fees_user, width=160, height=40,
                                                 values=students, font=custom_font_column)
    combobox_student.pack(side=LEFT, padx=5)

    def open_user_data_panel():

        studentname = combobox_student.get()

        def get_all_inf_fees_user():
            all_inf = {}
            connection = None
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()

                cursor.execute(
                    f"SELECT FH.TypeName,FI.Status FROM FeesItems as FI left join FeesHeader as FH on FH.FeesId = FI.FeesId  left join Student as S on FI.StudentId =S.StudentId where S.FirstName = '{studentname}'")
                for row in cursor.fetchall():
                    all_inf[row.TypeName] = row.Status


            except pyodbc.Error as ex:
                print(f'Błąd połączenia z bazą danych: {ex}, dla def get_all_first_names')

            finally:
                if connection:
                    connection.close()

            return all_inf

        user_data = customtkinter.CTk()
        user_data.title('App TechniSchools Lublin - Historia Ucznia')
        user_data.geometry('350x500')
        user_data.iconbitmap("FeesLogo.ico")

        label_student_name = customtkinter.CTkLabel(user_data, text=studentname, font=custom_font_biggest)
        label_student_name.pack(side=TOP, pady=10)

        student_inf = get_all_inf_fees_user()

        info_frame = customtkinter.CTkScrollableFrame(user_data, width=300, height=400)
        info_frame.pack(anchor='sw', padx=20, pady=10)

        for info in student_inf:
            frame_info_fees = customtkinter.CTkFrame(info_frame, width=300, height=100, corner_radius=10)
            frame_info_fees.pack(side=TOP, padx=10, pady=10)

            label_fees_name_by_user = customtkinter.CTkLabel(frame_info_fees, text=info, font=custom_font_biggest,
                                                             fg_color='transparent')
            label_fees_name_by_user.pack(side=LEFT, padx=5, pady=5)

            button_fees_by_usser = customtkinter.CTkFrame(frame_info_fees, width=80, height=30, fg_color='transparent')
            button_fees_by_usser.pack(side=LEFT, padx=5, pady=5)

            labels_name_fes_somthing = customtkinter.CTkLabel(button_fees_by_usser, text=student_inf[info],
                                                              font=custom_font_biggest, fg_color='transparent')
            labels_name_fes_somthing.pack(side=TOP)

            if student_inf[info] == 'Nie':
                frame_info_fees.configure(fg_color="#bf0202")
            else:
                frame_info_fees.configure(fg_color="#099909")

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        user_data.mainloop()

    button_open_show_student = customtkinter.CTkButton(frame_gorup_student_ang_go_to_fees_user, width=160, height=50,
                                                       font=custom_font_biggest, text="Wejdź",
                                                       command=open_user_data_panel)
    button_open_show_student.pack(side=LEFT, padx=5)

    label_add_fees_frame = customtkinter.CTkLabel(frame_add_fees, font=custom_font_biggest, text="Nowa składka")

    label_add_fees_frame.pack(side=LEFT, padx=(10, 0))

    # @FeesName varchar(50),
    # @Price decimal(10,2),
    # @DateStart date,
    # @DateEnd date

    def new_fees_gui():
        def Calendar_start_date():
            myCalendar = CTk()

            myCalendar.title("Calendar")

            myCalendar.geometry("280x250")

            myCalendar.configure(background="gray")

            MyCalndr = Calendar(myCalendar, selectmode="day", date_pattern="YYYY-MM-DD")
            MyCalndr.pack(pady=5)

            def selected_date():
                if MyCalndr.get_date() < '2023-09-01':
                    messagebox.showinfo('Info', 'Nie możesz wprowadzić tej daty')
                else:
                    date.configure(text=MyCalndr.get_date())
                    input_fees_start_date.delete(0, END)
                    input_fees_start_date.insert(0, MyCalndr.get_date())
                    myCalendar.mainloop()

            calendar_buttom = customtkinter.CTkButton(myCalendar, text="SELECT A DATE", command=selected_date)

            calendar_buttom.pack(pady=5)

            date = customtkinter.CTkLabel(myCalendar, text="")

            date.pack(pady=5)

            myCalendar.mainloop()

        def Calendar_end_date():
            myCalendar = CTk()

            myCalendar.title("Calendar")

            myCalendar.geometry("280x250")

            myCalendar.configure(background="gray")

            MyCalndr = Calendar(myCalendar, selectmode="day", date_pattern="YYYY-MM-DD")
            MyCalndr.pack(pady=5)

            def selected_date():
                date_end_main = MyCalndr.get_date()
                if date_end_main > '2028-06-25':
                    messagebox.showinfo('Info', 'Nie możesz wprowadzić tej daty')
                else:
                    date.configure(text=MyCalndr.get_date())
                    input_fees_end_date.delete(0, END)
                    input_fees_end_date.insert(0, MyCalndr.get_date())
                    myCalendar.mainloop()

            calendar_buttom = customtkinter.CTkButton(myCalendar, text="SELECT A DATE", command=selected_date)

            calendar_buttom.pack(pady=5)

            date = customtkinter.CTkLabel(myCalendar, text="")

            date.pack(pady=5)

            myCalendar.mainloop()

        def succesful_add_fees(FeesName):
            messagebox.showinfo('Info', f'Pomyślnie dodano skłądke {FeesName} ')

        def newFees(FeesName, Price, StartDate, EndDate):
            columns = []
            connection = None
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()

                select_all = f"""exec newFees '{FeesName}', {Price}, '{StartDate}', '{EndDate}'"""
                cursor.execute(select_all)
                connection.commit()
                succesful_add_fees(FeesName)
                print("Dodano skłądke")
            except pyodbc.Error as ex:
                print(f'Błąd połączenia z bazą danych: {ex}')

            finally:
                if connection:
                    connection.close()
            return columns

        fees = customtkinter.CTk()
        fees.title('App TechniSchools Lublin - Nowa Składka ')
        fees.geometry('500x500')
        fees.iconbitmap("FeesLogo.ico")

        label_fees_name = customtkinter.CTkLabel(fees, text="Nazwa składki", font=custom_font_biggest)
        label_fees_name.pack(anchor='nw', pady=10, padx=10)

        frame_name_price_fees = customtkinter.CTkFrame(fees, width=500, fg_color='transparent')
        # frame_name_price_fees.pack_propagate(False)
        frame_name_price_fees.pack(anchor='nw')

        input_fees_name = customtkinter.CTkEntry(frame_name_price_fees, width=360, height=40,
                                                 placeholder_text='Fees name', font=custom_font_column,
                                                 placeholder_text_color='#424446', border_color='#424446',
                                                 border_width=4)
        input_fees_name.pack(side=LEFT, pady=10, padx=10)

        input_fees_price = customtkinter.CTkEntry(frame_name_price_fees, width=90, height=40, placeholder_text="Price",
                                                  font=custom_font_column, placeholder_text_color='#424446',
                                                  border_color='#424446', border_width=4)
        input_fees_price.pack(side=LEFT, pady=10, padx=10)

        frame_start_date_new_fees = customtkinter.CTkFrame(fees, width=500, height=40, fg_color='transparent')
        # frame_start_date_new_fees.pack_propagate(False)
        frame_start_date_new_fees.pack(anchor='nw')

        label_start_date = customtkinter.CTkLabel(frame_start_date_new_fees, text='Startdate', font=custom_font_biggest)
        label_start_date.pack(anchor='nw', padx=10)

        frame_random_name = customtkinter.CTkFrame(frame_start_date_new_fees, width=340, height=40,
                                                   fg_color='transparent')
        frame_random_name.pack_propagate(False)
        frame_random_name.pack(anchor='nw')

        input_fees_start_date = customtkinter.CTkEntry(frame_random_name, width=200, height=40,
                                                       placeholder_text="YYYY-MM-DD", font=custom_font_column,
                                                       placeholder_text_color='#424446', border_color='#424446',
                                                       border_width=4)
        input_fees_start_date.pack(side=LEFT, padx=10)

        button_calendar_start_date = customtkinter.CTkButton(frame_random_name, width=100, height=40, text='Choose',
                                                             command=Calendar_start_date)
        button_calendar_start_date.pack(side=LEFT, padx=10)

        label_end_date = customtkinter.CTkLabel(frame_start_date_new_fees, text='Enddate', font=custom_font_biggest)
        label_end_date.pack(anchor='nw', padx=10)

        frame_random_name_sec = customtkinter.CTkFrame(frame_start_date_new_fees, width=340, height=40,
                                                       fg_color='transparent')
        frame_random_name_sec.pack_propagate(False)
        frame_random_name_sec.pack(anchor='nw')

        input_fees_end_date = customtkinter.CTkEntry(frame_random_name_sec, width=200, height=40,
                                                     placeholder_text="YYYY-MM-DD", font=custom_font_column,
                                                     placeholder_text_color='#424446', border_color='#424446',
                                                     border_width=4)
        input_fees_end_date.pack(side=LEFT, padx=10)

        button_calendar_end_date = customtkinter.CTkButton(frame_random_name_sec, width=100, height=40, text='Choose',
                                                           command=Calendar_end_date)
        button_calendar_end_date.pack(side=LEFT, padx=10)

        def add_fees_button():
            fees_new_name = input_fees_name.get()
            feeses_price = input_fees_price.get()
            new_start_date = input_fees_start_date.get()
            end_date = input_fees_end_date.get()


            if feeses_price and feeses_price.isdigit():
                feeses_price = int(feeses_price)
            else:
                messagebox.showinfo('Info', 'Cena musi być liczbą całkowitą większą lub równą zero')
                return

            if len(fees_new_name) > 20 or fees_new_name == '':
                messagebox.showinfo('Info', 'Zła nazwa składki lub brak wypełnionego pola')
            elif feeses_price < 0:
                messagebox.showinfo('Info', 'Cena musi być liczbą nieujemną')
            elif len(new_start_date) > 10 or new_start_date == '':
                messagebox.showinfo('Info', 'Zła data')
            elif len(end_date) > 10 or end_date == '':
                messagebox.showinfo('Info', 'Zła data')

            else:
                newFees(fees_new_name,feeses_price,new_start_date,end_date)
                print(frame_group.winfo_children())
                for widget in frame_group.winfo_children():
                    print(widget,"widgety")
                    widget.destroy()





                frame_group.pack_propagate(False)
                frame_group.pack(anchor='nw', padx=20, pady=10)

                frame_show_fees_by_student.pack_propagate(False)
                frame_show_fees_by_student.pack(side=LEFT, padx=20)
                frame_add_fees.pack_propagate(False)
                frame_add_fees.pack(side=LEFT)

                tabview_fees.pack(side=BOTTOM, padx=20)
                label_add_fees_frame.pack(side=LEFT, padx=(10, 0))
                button_plus_fees.pack(side=RIGHT, padx=(0, 10))

                label_show_student.pack(side=TOP, padx=10, pady=10)
                frame_gorup_student_ang_go_to_fees_user.pack(side=TOP, padx=10, pady=10)
                combobox_student.pack(side=LEFT, padx=5)
                button_open_show_student.pack(side=LEFT, padx=5)


                refresh_fees_frame()



        button_new_fees = customtkinter.CTkButton(fees, width=300, height=60, text='New Fees', font=custom_font_biggest,
                                                  command=add_fees_button)
        button_new_fees.pack(anchor='nw', padx=10, pady=10)
        fees.mainloop()

    button_plus_fees = customtkinter.CTkButton(frame_add_fees, width=70, height=60, text="+", font=custom_font_very_big,
                                               command=new_fees_gui)
    button_plus_fees.pack(side=RIGHT, padx=(0, 10))

    tabview_fees = customtkinter.CTkTabview(tabview_main.tab("Składki"), width=1600, height=600, fg_color='#333333')
    tabview_fees.pack(side=BOTTOM, padx=20)

    tabview_fees.add("Aktywne")
    tabview_fees.set("Aktywne")

    tabview_fees.add("Zakończone")
    tabview_fees.set("Zakończone")

    frame_all_fees_active = customtkinter.CTkFrame(tabview_fees.tab("Aktywne"), width=1600, height=550,
                                                   fg_color='transparent')
    frame_all_fees_active.pack_propagate(False)
    frame_all_fees_active.pack(side=BOTTOM)

    frame_scroll_fees_active = customtkinter.CTkScrollableFrame(frame_all_fees_active, width=1600, height=550,
                                                                fg_color='transparent')
    frame_scroll_fees_active.pack(side=TOP)

    frame_all_fees_end = customtkinter.CTkFrame(tabview_fees.tab("Zakończone"), width=1600, height=550,
                                                fg_color='transparent')
    frame_all_fees_end.pack_propagate(False)
    frame_all_fees_end.pack(side=BOTTOM)

    frame_scroll_fees_not_active = customtkinter.CTkScrollableFrame(frame_all_fees_end, width=1600, height=550,
                                                                    fg_color='transparent')
    frame_scroll_fees_not_active.pack(side=TOP)

    # skłądki aktywne
    ###########################################################
    ###########################################################
    ###########################################################
    ###########################################################
    ###########################################################
    ###########################################################
    ###########################################################
    def how_much_fees_is_exists():
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                SELECT COUNT(FeesID) AS CountFees 
                FROM FeesHeader 
                WHERE DateEnd >= GETDATE()
            """)

            row = cursor.fetchone()

            if row:
                count_fees = row.CountFees
                return count_fees
            else:
                return 0

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} how_much_fees_is_exists')
            return None

        finally:
            if connection:
                connection.close()

    def feses_list_id():
        feeses_id_list = []
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                SELECT FeesID AS CountFees 
                FROM FeesHeader 
                WHERE DateEnd >= GETDATE()
            """)

            for row in cursor.fetchall():
                feeses_id_list.append(row.CountFees)

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} feses_list_id')
            return None

        finally:
            if connection:
                connection.close()

        return feeses_id_list

    def get_paid_mans(FeesName):
        print(FeesName, "tu")
        paid_man = []
        try:    
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute(f"""
                exec getPaid '{FeesName}'
            """)

            for row in cursor.fetchall():
                paid_man.append(row.FirstName)
                print(row, "row ten zły")

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} get_paid_mans')
            return None

        finally:
            if connection:
                connection.close()
        print(paid_man, 'tu')
        return paid_man

    def get_email_not_paid(FeesName):
        email = []
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute(f"""
                exec getEmailNotPaidMan '{FeesName}'
            """)

            for row in cursor.fetchall():
                email.append(row.User_Email)

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} get_email_not_paid')
            return None

        finally:
            if connection:
                connection.close()

        return email

    def get_not_paid_mans(FeesName):
        not_paid_man = []
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute(f"""
                exec getNotPaid '{FeesName}'
            """)

            for row in cursor.fetchall():
                not_paid_man.append(row.FirstName)

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} get_not_paid_mans')
            return None

        finally:
            if connection:
                connection.close()

        return not_paid_man

    def get_price_fees(FeesName):
        price_fees = 0
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute(f"""
               SELECT Price FROM FeesHeader WHERE TypeName = '{FeesName}'
            """)

            for row in cursor.fetchall():
                price_fees += row[0]

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} get_price_fees')
            return None

        finally:
            if connection:
                connection.close()

        return price_fees

    def get_datas_fees(FeesName):
        datas = []
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute(f"""
               select CONVERT(varchar, DateStart, 23) as 'DateStart',CONVERT(varchar, DateEnd, 23) as DateEnd from FeesHeader WHERE TypeName = '{FeesName}'
            """)

            for row in cursor.fetchall():
                datas.append(row.DateStart)
                datas.append(row.DateEnd)

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} get_price_fees')
            return None

        finally:
            if connection:
                connection.close()

        return datas

    def openFeesPanel(FeesName):
        frame_group.forget()
        frame_show_fees_by_student.forget()
        frame_add_fees.forget()
        label_add_fees_frame.forget()
        button_plus_fees.forget()
        tabview_fees.forget()

        frame_feses_main = customtkinter.CTkFrame(tabview_main.tab("Składki"), width=1600, height=1040,
                                                  fg_color='transparent')
        frame_feses_main.pack_propagate(False)
        frame_feses_main.pack(side=TOP)

        label_fees_name = customtkinter.CTkLabel(frame_feses_main, text=FeesName, font=custom_font_very_big)
        label_fees_name.pack(side=TOP)

        scrollball_frame_feeses = customtkinter.CTkScrollableFrame(frame_feses_main, width=1600, height=800)
        scrollball_frame_feeses.pack_propagate(True)
        scrollball_frame_feeses.pack(side=TOP)

        label_paid_not_paid = customtkinter.CTkLabel(scrollball_frame_feeses,
                                                     text="Wpłacono                                  Nie Wpłacono",
                                                     font=custom_font_test)
        label_paid_not_paid.pack(side=TOP)  # |                                  |

        frame_paid_and_not_paid = customtkinter.CTkFrame(scrollball_frame_feeses, width=1600, height=350)
        frame_paid_and_not_paid.pack_propagate(False)
        frame_paid_and_not_paid.pack(side=TOP, padx=10)

        frame_paid = customtkinter.CTkFrame(frame_paid_and_not_paid, width=550, height=330)
        frame_paid.pack_propagate(False)
        frame_paid.pack(side=LEFT, padx=(20, 10))

        getPaidMans = get_paid_mans(FeesName)
        paid_mans_text = " ".join(getPaidMans)

        frame_lables_fees = customtkinter.CTkFrame(frame_paid, width=550, height=330, fg_color='transparent')
        frame_lables_fees.pack_propagate(False)
        frame_lables_fees.pack(side=LEFT, padx=5)

        len_paid = len(getPaidMans)
        label_how_many_is_paid = customtkinter.CTkLabel(frame_lables_fees, text=f"Wpłacono:{len_paid}",
                                                        font=custom_font_column)
        label_how_many_is_paid.pack(anchor='nw', padx=20, pady=(10, 5))

        fees_price = get_price_fees(FeesName)

        fees_price_count = len(getPaidMans) * fees_price
        label_money_get = customtkinter.CTkLabel(frame_lables_fees, text=f"Suma:{fees_price_count} zł",
                                                 font=custom_font_column)
        label_money_get.pack(anchor='nw', padx=20, pady=(5, 10))

        frame_paid_scroll = customtkinter.CTkScrollableFrame(frame_lables_fees, width=550, height=200,
                                                             orientation="horizontal")
        frame_paid_scroll.pack(anchor='nw', padx=20, pady=(10, 5))

        paid_mans_text = paid_mans_text.split()

        ## od tąd mi się pomyliły i źle azywałem obiekty w programie ale działą dam gdzi jest notpaid powinno być paid i odwrotnie
        def cancel_paid_go(student_name):
            FName = FeesName
            cancel_paid(FName, student_name)
            print(FName, student_name)
            frame_feses_main.forget()
            openFeesPanel(FeesName)
            makeStudentPaid()

        def cancel_paid(FeesName, UserName):
            connection = None
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()

                select_all = f"exec cancelPaid '{UserName}','{FeesName}'  "
                cursor.execute(select_all)
                connection.commit()
                print(select_all)
                print('Anulowano wpłąte ')

            except pyodbc.Error as ex:
                print(f'Błąd połączenia z bazą danych: {ex} cancel_paid')

            finally:
                if connection:
                    connection.close()

        def makeStudentPaid():
            for student_name in paid_mans_text:
                frame_man = customtkinter.CTkFrame(frame_paid_scroll, height=200, width=250)
                frame_man.pack_propagate(False)
                frame_man.pack(side=LEFT, padx=5, pady=5)

                frame_profile = customtkinter.CTkFrame(frame_man, width=200, height=300)
                frame_profile.pack_propagate(False)
                frame_profile.pack(side=TOP, padx=10, pady=5)

                circle = customtkinter.CTkFrame(frame_profile, width=50, height=50, corner_radius=100,
                                                fg_color='#274695')
                circle.pack(side=TOP, pady=(10, 0), padx=20)

                frame_rectangle = customtkinter.CTkFrame(frame_profile, width=100, height=50, corner_radius=100,
                                                         fg_color='#274695')
                frame_rectangle.pack(side=TOP)

                def mulitpe_cancel(student=student_name):
                    cancel_paid_go(student)

                button_cancel_paid = customtkinter.CTkButton(frame_profile, width=100, height=25, text='Anuluj',
                                                             fg_color='red', command=mulitpe_cancel)
                button_cancel_paid.pack(side=BOTTOM, pady=5)

                label_name = customtkinter.CTkLabel(frame_profile, text=student_name, font=custom_font)
                label_name.pack(side=BOTTOM, pady=5)

        makeStudentPaid()

        # label_data_paid = customtkinter.CTkLabel(frame_paid_scroll, text=paid_mans_text, font=custom_font)
        # label_data_paid.pack(pady=20)

        #                     CHECK POINT LUDZIE KÓTRZY NIE WPŁĄCILI
        ##############################################################################
        ##############################################################################
        ##############################################################################
        ##############################################################################
        ##############################################################################
        ##############################################################################
        ##############################################################################
        ##############################################################################
        ##############################################################################

        frame_not_paid = customtkinter.CTkFrame(frame_paid_and_not_paid, width=550, height=330)
        frame_not_paid.pack_propagate(False)
        frame_not_paid.pack(side=LEFT, padx=20)

        frame_lables_fees_not_paid = customtkinter.CTkFrame(frame_not_paid, width=550, height=330,
                                                            fg_color='transparent')
        frame_lables_fees_not_paid.pack_propagate(False)
        frame_lables_fees_not_paid.pack(side=LEFT, padx=5)

        len_not_paid = len(get_not_paid_mans(FeesName))

        frame_button_frame_scroll_not_paid_man = customtkinter.CTkFrame(frame_lables_fees_not_paid, width=550,
                                                                        height=60, fg_color='transparent')
        frame_button_frame_scroll_not_paid_man.pack_propagate(False)
        frame_button_frame_scroll_not_paid_man.pack(side=TOP)

        label_how_many_is_not_paid = customtkinter.CTkLabel(frame_button_frame_scroll_not_paid_man,
                                                            text=f"Nie Wpłacono:{len_not_paid}",
                                                            font=custom_font_column)
        label_how_many_is_not_paid.pack(side=LEFT, padx=20, pady=(10, 5))

        getNotPaidMans = get_not_paid_mans(FeesName)
        notPaidMans = " ".join(getNotPaidMans)

        notPaidMans = notPaidMans.split()

        def longEmailSendProcess():
            messagebox.showinfo("Informacja", "Ten proces może być czasochłony prosimy o cierpliwość.")

        def sendEmailEnded():
            messagebox.showinfo("Informacja", "Proces wysłania wiadomości został zakończony")

        emails = get_email_not_paid(FeesName)
        price = get_price_fees(FeesName)

        def remindAboutFees():
            longEmailSendProcess()
            for i in emails:
                print(i)
                email = "pukaluk.adam505@gmail.com"
                receiver_email = i

                subject = 'Przypomnaienie o zaległej składce'
                message_body = f"""
                    Witaj 
                    Szanowny Użytkowniku,

                    Przesyłamy to przypomnienie w związku z zaległą składką na {FeesName}, którą należy uregulować. Prosimy o dokonanie wpłaty w najbliższym czasie, aby uniknąć ewentualnych konsekwencji 
                    związanych z opóźnieniem w regulowaniu opłat.

                    Dane do przelewu:
                    Numer tel: 695031104
                    Kwota: {price}
                    Tytuł przelewu: Nazwa składki za która dokonuje się wpłaty

                    Prosimy o potwierdzenie dokonania płatności po jej wykonaniu.

                    Z poważaniem,
                    Zespół Obsługi Klienta

                    ---
                    Ta wiadomość została wygenerowana automatycznie. Prosimy nie odpowiadać na nią.

                    """

                msg = MIMEMultipart()

                msg['Subject'] = subject

                msg.attach(MIMEText(message_body, 'plain', 'utf-8'))

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()

                server.login(email, "yiny vvvt ixlz lzfz")

                server.sendmail(email, receiver_email, msg.as_string())

                server.quit()

                print(f"Email has been sent to {receiver_email} with subject: {subject}")
            sendEmailEnded()

        button_remind_fees_paid = customtkinter.CTkButton(frame_button_frame_scroll_not_paid_man, width=200, height=50,
                                                          text='Przypomnij', font=custom_font_column,
                                                          command=remindAboutFees)
        button_remind_fees_paid.pack(side=LEFT, padx=20, pady=(10, 5))

        frame_not_paid_scroll = customtkinter.CTkScrollableFrame(frame_lables_fees_not_paid, width=550, height=200,
                                                                 orientation="horizontal")
        frame_not_paid_scroll.pack(side=BOTTOM, padx=20, pady=(10, 10))

        def changeToYes(student_name):
            FName = FeesName
            paidChange(FName, student_name)
            print(FName, student_name)
            frame_feses_main.forget()
            openFeesPanel(FeesName)
            makeStudentPaid()

        def paidChange(FeesName, UserName):
            connection = None
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()

                select_all = f"exec makePaidMan '{UserName}','{FeesName}'  "
                cursor.execute(select_all)
                connection.commit()
                print(select_all)
                print('Anulowano wpłąte ')

            except pyodbc.Error as ex:
                print(f'Błąd połączenia z bazą danych: {ex} paidChange')

            finally:
                if connection:
                    connection.close()

        def makeStudentNotPaid():
            print(notPaidMans)
            for student_name in notPaidMans:
                frame_man_not_paid = customtkinter.CTkFrame(frame_not_paid_scroll, height=200, width=250)
                frame_man_not_paid.pack_propagate(False)
                frame_man_not_paid.pack(side=LEFT, padx=5, pady=5)

                frame_profile_not_paid = customtkinter.CTkFrame(frame_man_not_paid, width=200, height=300)
                frame_profile_not_paid.pack_propagate(False)
                frame_profile_not_paid.pack(side=TOP, padx=10, pady=5)

                circle_not_paid = customtkinter.CTkFrame(frame_profile_not_paid, width=50, height=50, corner_radius=100,
                                                         fg_color='#274695')
                circle_not_paid.pack(side=TOP, pady=(10, 0), padx=20)

                frame_rectangle_not_paid = customtkinter.CTkFrame(frame_profile_not_paid, width=100, height=50,
                                                                  corner_radius=100, fg_color='#274695')
                frame_rectangle_not_paid.pack(side=TOP)

                def mulitpe_cahnge_to_yes(student=student_name):
                    changeToYes(student)
                    sucesful_change_to_yes(student)

                button_cancel_not_paid = customtkinter.CTkButton(frame_profile_not_paid, width=100, height=25,
                                                                 text='Wpłacone', fg_color="#099909",
                                                                 command=mulitpe_cahnge_to_yes)
                button_cancel_not_paid.pack(side=BOTTOM, pady=5)

                label_name_not_paid = customtkinter.CTkLabel(frame_profile_not_paid, text=student_name,
                                                             font=custom_font)
                label_name_not_paid.pack(side=BOTTOM, pady=5)

        makeStudentNotPaid()

        # modify fees

        label_modify_fees = customtkinter.CTkLabel(scrollball_frame_feeses, text='Konfiguracji Składki',
                                                   font=custom_font_test)
        label_modify_fees.pack(side=TOP, pady=20, padx=20)

        frame_mofidy_fees_settings = customtkinter.CTkFrame(scrollball_frame_feeses, width=700, height=350,
                                                            fg_color='#333333')
        # frame_mofidy_fees_settings.pack_propagate(False)
        frame_mofidy_fees_settings.pack(side=TOP)

        frame_change_data_fees = customtkinter.CTkFrame(frame_mofidy_fees_settings, width=350, height=270,
                                                        fg_color='transparent')
        frame_change_data_fees.pack_propagate(False)
        frame_change_data_fees.pack(side=LEFT, anchor='n', padx=(5, 0))

        def start_date(FeesName):
            startDate = None
            connection = None
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()

                cursor.execute(
                    f"""            
                    SELECT CONVERT(varchar, DateStart, 23) AS DateStart FROM FeesHeader
                    WHERE TypeName = '{FeesName}'
                    """)
                startDate = [row.DateStart for row in cursor.fetchall()]

            except pyodbc.Error as ex:
                print(f'Błąd połączenia z bazą danych: {ex} start_date')

            finally:
                if connection:
                    connection.close()
            return startDate

        Start_Date = start_date(FeesName)

        label_start_date = customtkinter.CTkLabel(frame_change_data_fees, text='Data rozpoczęcia',
                                                  font=custom_font_biggest)
        label_start_date.pack(anchor='nw', padx=20, pady=10)

        frame_main_change_start_date = customtkinter.CTkFrame(frame_change_data_fees, fg_color='transparent')
        frame_main_change_start_date.pack(anchor='nw', pady=10, padx=20)

        input_change_start_date = customtkinter.CTkEntry(frame_main_change_start_date, width=200, height=40,
                                                         placeholder_text=Start_Date, font=custom_font_column,
                                                         placeholder_text_color='#424446', border_color='#424446',
                                                         border_width=4)
        input_change_start_date.pack(side=LEFT)

        def Calendar_start_date_change():
            myCalendar = CTk()

            myCalendar.title("Calendar")

            myCalendar.geometry("280x250")

            myCalendar.configure(background="gray")

            MyCalndr = Calendar(myCalendar, selectmode="day", date_pattern="YYYY-MM-DD")
            MyCalndr.pack(pady=5)

            def selected_date():
                final_start_date = MyCalndr.get_date()
                if final_start_date <= '2023-09-01':
                    messagebox.showinfo('Info', 'Nie możesz wprowadzić tej daty')
                else:
                    date.configure(text=final_start_date)
                    input_change_start_date.delete(0, END)
                    input_change_start_date.insert(0, MyCalndr.get_date())
                    myCalendar.mainloop()

            calendar_buttom = customtkinter.CTkButton(myCalendar, text="SELECT A DATE", command=selected_date)

            calendar_buttom.pack(pady=5)

            date = customtkinter.CTkLabel(myCalendar, text="")

            date.pack(pady=5)

            myCalendar.mainloop()

        button_calendar_start_date_change = customtkinter.CTkButton(frame_main_change_start_date, width=100, height=40,
                                                                    text='Choose', command=Calendar_start_date_change)
        button_calendar_start_date_change.pack(side=LEFT, padx=10)

        label_end_date = customtkinter.CTkLabel(frame_change_data_fees, text='Data zakończenia',
                                                font=custom_font_biggest)
        label_end_date.pack(anchor='nw', padx=20, pady=10)

        frame_main_change_end_date = customtkinter.CTkFrame(frame_change_data_fees, fg_color='transparent')
        frame_main_change_end_date.pack(anchor='nw', pady=10, padx=20)

        input_change_end_date = customtkinter.CTkEntry(frame_main_change_end_date, width=200, height=40,
                                                       placeholder_text=Start_Date, font=custom_font_column,
                                                       placeholder_text_color='#424446', border_color='#424446',
                                                       border_width=4)
        input_change_end_date.pack(side=LEFT)

        def Calendar_end_date_change():
            myCalendar = CTk()

            myCalendar.title("Calendar")

            myCalendar.geometry("280x250")

            myCalendar.configure(background="gray")

            MyCalndr = Calendar(myCalendar, selectmode="day", date_pattern="YYYY-MM-DD")
            MyCalndr.pack(pady=5)

            def selected_date():
                final_end_date = MyCalndr.get_date()
                if final_end_date > '2028-06-25':
                    messagebox.showinfo('Info', 'Nie możesz wprowadzić tej daty')
                else:
                    date.configure(text=final_end_date)
                    input_change_end_date.delete(0, END)
                    input_change_end_date.insert(0, MyCalndr.get_date())
                    myCalendar.mainloop()

            calendar_buttom = customtkinter.CTkButton(myCalendar, text="SELECT A DATE", command=selected_date)

            calendar_buttom.pack(pady=5)

            date = customtkinter.CTkLabel(myCalendar, text="")

            date.pack(pady=5)

            myCalendar.mainloop()

        button_calendar_end_date_change = customtkinter.CTkButton(frame_main_change_end_date, width=100, height=40,
                                                                  text='Choose', command=Calendar_end_date_change)
        button_calendar_end_date_change.pack(side=LEFT, padx=10)

        frame_change_price_and_name_fees = customtkinter.CTkFrame(frame_mofidy_fees_settings, height=270, width=300,
                                                                  fg_color='transparent')
        frame_change_price_and_name_fees.pack_propagate(False)
        frame_change_price_and_name_fees.pack(anchor='nw', padx=10)

        label_name_fees = customtkinter.CTkLabel(frame_change_price_and_name_fees, width=80, text='Nazwa Składki',
                                                 font=custom_font_biggest)
        label_name_fees.pack(anchor='nw', pady=10, padx=10)

        input_chnage_name_fees = customtkinter.CTkEntry(frame_change_price_and_name_fees, width=150, height=40,
                                                        placeholder_text=f"{FeesName}", font=custom_font_column,
                                                        placeholder_text_color='#424446', border_color='#424446',
                                                        border_width=4)
        input_chnage_name_fees.pack(anchor='nw', pady=10, padx=10)

        label_change_price_fees = customtkinter.CTkLabel(frame_change_price_and_name_fees, text='Cena Składki',
                                                         font=custom_font_biggest)
        label_change_price_fees.pack(anchor='nw', padx=10, pady=10)

        input_change_price_fees = customtkinter.CTkEntry(frame_change_price_and_name_fees, placeholder_text=price,
                                                         font=custom_font_column, placeholder_text_color='#424446',
                                                         border_color='#424446', border_width=4)
        input_change_price_fees.pack(anchor='nw', padx=10, pady=10)

        def change_fees_settings(NewName, NewPrice, NewStartDate, NewEndDate):
            if NewPrice == '':
                NewPrice = 0
            FName = FeesName

            connection = None
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                query = f"exec  changeSettingsFees '{FName}','{NewName}',{NewPrice},'{NewStartDate}','{NewEndDate}'"
                cursor.execute(query)
                cursor.commit()

                messagebox.showinfo('Info', 'Zmieniono dane składki')
            except pyodbc.Error as ex:
                print(f'Błąd połączenia z bazą danych: {ex} change_fees_settings')

            finally:
                if connection:
                    connection.close()

        def execChangeSettFees():
            FeesNameNew = input_chnage_name_fees.get()
            NewPriceFees = input_change_price_fees.get()
            NewStartDate = input_change_start_date.get()
            NewEndDate = input_change_end_date.get()

            change_fees_settings(FeesNameNew, NewPriceFees, NewStartDate, NewEndDate)
            frame_feses_main.forget()
            if FeesNameNew == '':
                openFeesPanel(FeesName)
            else:
                openFeesPanel(FeesNameNew)

        button_save_new_data = customtkinter.CTkButton(frame_mofidy_fees_settings, width=150, height=50, text='Zapisz',
                                                       font=custom_font_biggest, command=execChangeSettFees)
        button_save_new_data.pack(side=RIGHT, anchor='se', padx=10, pady=10)

        def comback_to_feeses_panel():

            frame_feses_main.forget()

            frame_group.pack_propagate(False)
            frame_group.pack(anchor='nw', padx=20, pady=10)

            frame_show_fees_by_student.pack_propagate(False)
            frame_show_fees_by_student.pack(side=LEFT, padx=20)
            frame_add_fees.pack_propagate(False)
            frame_add_fees.pack(side=LEFT)

            tabview_fees.pack(side=BOTTOM, padx=20)
            label_add_fees_frame.pack(side=LEFT, padx=(10, 0))
            button_plus_fees.pack(side=RIGHT, padx=(0, 10))

            label_show_student.pack(side=TOP, padx=10, pady=10)
            frame_gorup_student_ang_go_to_fees_user.pack(side=TOP, padx=10, pady=10)
            combobox_student.pack(side=LEFT, padx=5)
            button_open_show_student.pack(side=LEFT, padx=5)

            refresh_fees_frame()

        buton_comback_to_feese = customtkinter.CTkButton(scrollball_frame_feeses, width=250, height=40, text='Powrót d',
                                                         command=comback_to_feeses_panel, font=custom_font_biggest)
        buton_comback_to_feese.pack(anchor='sw', pady=20, padx=20)

    #                                       CHECKPOINT MORDO
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    #####################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################

    def get_fee_name_by_id(fee_id):
        fee_name = ""
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute(f"SELECT TypeName FROM FeesHeader WHERE FeesID = ?", (fee_id,))
            row = cursor.fetchone()
            if row:
                fee_name = row[0]

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')

        finally:
            if connection:
                connection.close()

        return fee_name

    def create_rows():
        z = 0
        y = 3
        x = 1
        idk = 0
        count_fees = how_much_fees_is_exists()
        id_list = feses_list_id()
        for _ in range(math.ceil(how_much_fees_is_exists() / 3)):
            frame_active_fees = customtkinter.CTkFrame(frame_scroll_fees_active, width=1600, height=200,
                                                       fg_color='transparent')
            frame_active_fees.pack(side=TOP)

            for i in range(z, y):
                if count_fees == 0:
                    break
                else:
                    frame_fees_name_frame = customtkinter.CTkFrame(frame_active_fees, fg_color='transparent')
                    frame_fees_name_frame.pack(side=LEFT)

                    fee_name = get_fee_name_by_id(id_list[idk])

                    label_fees_name = customtkinter.CTkLabel(frame_fees_name_frame, text=f"{fee_name}",
                                                             font=custom_font_column)
                    label_fees_name.pack(side=TOP)

                    frame_fees = customtkinter.CTkFrame(frame_fees_name_frame, width=350, height=200)
                    frame_fees.pack(side=TOP, padx=10, pady=10)
                    frame_fees.pack_propagate(False)

                    def label_paid_count(id):
                        try:
                            connection = pyodbc.connect(connection_string)
                            cursor = connection.cursor()
                            cursor.execute(
                                f"SELECT COUNT(Status) as PaidCount FROM FeesItems WHERE FeesID = {id} AND Status = 'Tak'")
                            row = cursor.fetchone()
                            if row:
                                paid_count = row.PaidCount
                            else:
                                paid_count = 0
                        except pyodbc.Error as ex:
                            print(f'Błąd połączenia z bazą danych: {ex}')
                            paid_count = 0
                        finally:
                            if connection:
                                connection.close()
                        return paid_count

                    def label_not_paid_cunt(id):
                        try:
                            connection = pyodbc.connect(connection_string)
                            cursor = connection.cursor()
                            cursor.execute(
                                f"SELECT COUNT(Status) as NotPaidCount FROM FeesItems WHERE FeesID = {id} AND Status = 'Nie'")
                            row = cursor.fetchone()
                            if row:
                                notpaid_count = row.NotPaidCount
                            else:
                                notpaid_count = 0
                        except pyodbc.Error as ex:
                            print(f'Błąd połączenia z bazą danych: {ex}')
                            notpaid_count = 0
                        finally:
                            if connection:
                                connection.close()
                        return notpaid_count

                    paid_count = label_paid_count(id_list[idk])
                    not_paid_coint = label_not_paid_cunt(id_list[idk])

                    label_paid = customtkinter.CTkLabel(frame_fees, text=f'Wpłacono: {paid_count}', font=custom_fontc)
                    label_paid.pack(anchor='nw', padx=20, pady=(10, 5))

                    label_not_paid = customtkinter.CTkLabel(frame_fees, text=f'Nie wpłacone: {not_paid_coint}',
                                                            font=custom_fontc)
                    label_not_paid.pack(anchor='nw', padx=20, pady=(5, 10))

                    def goFees(fee_name=fee_name):
                        openFeesPanel(fee_name)

                    buton_go_to_fees = customtkinter.CTkButton(
                        frame_fees,
                        width=300,
                        height=60,
                        text='Wejdź',
                        font=custom_font_biggest,
                        command=lambda fn=fee_name: goFees(fn))
                    buton_go_to_fees.pack(side=BOTTOM, padx=20, pady=(5, 20))

                    x += 1
                    count_fees -= 1
                    idk += 1

        z += 3
        y += 3

    create_rows()

    def refresh_fees_frame():
        for widget in frame_scroll_fees_active.winfo_children():
            widget.destroy()
        create_rows()

    #                   Składi zakończone
    ###########################################################
    ###########################################################
    ###########################################################
    ###########################################################
    ###########################################################
    ###########################################################

    def how_much_fees_is_ended():
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                SELECT COUNT(FeesID) AS CountFees 
                FROM FeesHeader 
                WHERE DateEnd < GETDATE()
            """)

            row = cursor.fetchone()

            if row:
                count_fees = row.CountFees
                return count_fees
            else:
                return 0

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} how_much_fees_is_exists')
            return None

        finally:
            if connection:
                connection.close()

    def feses_list_id_end():
        feeses_id_list_end = []
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                SELECT FeesID AS CountFees 
                FROM FeesHeader 
                WHERE DateEnd < GETDATE()
            """)

            for row in cursor.fetchall():
                feeses_id_list_end.append(row.CountFees)

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} feses_list_id')
            return None

        finally:
            if connection:
                connection.close()

        return feeses_id_list_end

    def fees_datas_to_eksport(FeesName):
        print(f"Eksport: {FeesName}")
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute(f"""
                SELECT S.FirstName, S.LastName, FH.TypeName, FI.Status 
                FROM FeesItems AS FI
                LEFT JOIN FeesHeader AS FH ON FI.FeesID = FH.FeesID
                LEFT JOIN Student AS S ON FI.StudentID = S.StudentID
                WHERE FH.TypeName = '{FeesName}'
            """)

            rows = cursor.fetchall()

            # Pobierz nazwy kolumn
            columns = [column[0] for column in cursor.description]

            # Utwórz ramkę danych pandas
            df = pd.DataFrame.from_records(rows, columns=columns)
            print(df, "datas")

            # Eksportuj ramkę danych do pliku CSV
            df.to_csv('fees_export.csv', index=False, encoding='utf-8-sig')

            print("Dane zostały wyeksportowane do pliku fees_export.csv")

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} w funkcji fees_datas_to_eksport')
        finally:
            if connection:
                connection.close()

    def openEndedFeesPanel(FeesName):
        frame_group.forget()
        frame_add_fees.forget()
        frame_show_fees_by_student.forget()
        label_add_fees_frame.forget()
        button_plus_fees.forget()
        tabview_fees.forget()

        frame_feses_main = customtkinter.CTkFrame(tabview_main.tab("Składki"), width=1600, height=900,
                                                  fg_color='transparent')
        frame_feses_main.pack(side=TOP)

        frame_feses_main_sec = customtkinter.CTkFrame(frame_feses_main, fg_color='transparent', width=1600, height=80)
        frame_feses_main_sec.pack_propagate(False)
        frame_feses_main_sec.pack(side=BOTTOM)

        label_fees_name = customtkinter.CTkLabel(frame_feses_main, text=FeesName, font=custom_font_very_big)
        label_fees_name.pack(side=TOP)

        frame_data_about_ended_fees = customtkinter.CTkFrame(frame_feses_main, fg_color='#333333', height=400,
                                                             width=440)
        frame_data_about_ended_fees.pack_propagate(False)
        frame_data_about_ended_fees.pack(anchor='n', side=LEFT, padx=(20, 10), pady=10)

        label_price_fees = customtkinter.CTkLabel(frame_data_about_ended_fees,
                                                  text=f"Cena: {get_price_fees(FeesName)}zł", font=custom_font_column)
        label_price_fees.pack(anchor='nw', padx=20, pady=10)

        feesSumPLN = get_price_fees(FeesName) * len(get_paid_mans(FeesName))
        print(feesSumPLN)
        print(get_price_fees(FeesName))

        label_sum_price = customtkinter.CTkLabel(frame_data_about_ended_fees, text=f"Suma: {feesSumPLN}zł",
                                                 font=custom_font_column)
        label_sum_price.pack(anchor='nw', padx=20, pady=10)

        datas = get_datas_fees(FeesName)

        label_datas_fees = customtkinter.CTkLabel(frame_data_about_ended_fees, text=f"Termin: {datas[0]} - {datas[1]}",
                                                  font=custom_font_column)
        label_datas_fees.pack(anchor='nw', padx=20, pady=10)

        def eksport_fees():
            fees_datas_to_eksport(FeesName)
            messagebox.showinfo('Info', f'Pomyślne wykesportowano dane do pliku {FeesName}_Fees.csv')

        button_import_to_csv = customtkinter.CTkButton(frame_data_about_ended_fees, width=100, height=40,text='Eksport Danych', command=eksport_fees)
        button_import_to_csv.pack(anchor='nw', padx=20, pady=10)

        frame_all_paid_not_paid_Scrolls_alnd_labels = customtkinter.CTkFrame(frame_feses_main, height=600, width=1200,
                                                                             fg_color='transparent')
        frame_all_paid_not_paid_Scrolls_alnd_labels.pack_propagate(False)
        frame_all_paid_not_paid_Scrolls_alnd_labels.pack(side=LEFT, padx=(10, 20))

        label_text_paid_fees_in_EndedFees = customtkinter.CTkLabel(frame_all_paid_not_paid_Scrolls_alnd_labels,
                                                                   text=f"Wpłacone:{len(get_paid_mans(FeesName))}",
                                                                   font=custom_font_35)
        label_text_paid_fees_in_EndedFees.pack(anchor='nw', padx=20, pady=10)

        getPaidMans = get_paid_mans(FeesName)

        paid_mans_text = " ".join(getPaidMans)
        print(getPaidMans, '1')
        paid_mans_text = paid_mans_text.split()
        print(paid_mans_text, '2')

        frame_paid_mans = customtkinter.CTkScrollableFrame(frame_all_paid_not_paid_Scrolls_alnd_labels, height=200,
                                                           width=1600, orientation="horizontal", fg_color='transparent')
        frame_paid_mans.pack(anchor='nw', padx=20, pady=10)

        def makeStudentPaid():
            for student_name in paid_mans_text:
                frame_man = customtkinter.CTkFrame(frame_paid_mans, height=200, width=250)
                frame_man.pack_propagate(False)
                frame_man.pack(side=LEFT, padx=5, pady=5)

                frame_profile = customtkinter.CTkFrame(frame_man, width=200, height=300)
                frame_profile.pack_propagate(False)
                frame_profile.pack(side=TOP, padx=10, pady=5)

                circle = customtkinter.CTkFrame(frame_profile, width=50, height=50, corner_radius=100,
                                                fg_color='#274695')
                circle.pack(side=TOP, pady=(10, 0), padx=20)

                frame_rectangle = customtkinter.CTkFrame(frame_profile, width=100, height=50, corner_radius=100,
                                                         fg_color='#274695')
                frame_rectangle.pack(side=TOP)

                frame_grren_paid = customtkinter.CTkFrame(frame_profile, fg_color="#099909", width=140, height=25)
                frame_grren_paid.pack(side=BOTTOM, pady=5)

                label_paid_in_thin_green_paid = customtkinter.CTkLabel(frame_grren_paid, text='Wpłacone')
                label_paid_in_thin_green_paid.pack(side=BOTTOM, padx=5)

                label_name = customtkinter.CTkLabel(frame_profile, text=student_name, font=custom_font)
                label_name.pack(side=BOTTOM, pady=5)

        makeStudentPaid()

        label_text_not_paid_fees_in_EndedFees = customtkinter.CTkLabel(frame_all_paid_not_paid_Scrolls_alnd_labels,
                                                                       text=f"Nie Wpłacone:{len(get_not_paid_mans(FeesName))}",
                                                                       font=custom_font_35)
        label_text_not_paid_fees_in_EndedFees.pack(anchor='nw', padx=20, pady=10)

        getNotPaidMans = get_not_paid_mans(FeesName)
        notPaidMans = " ".join(getNotPaidMans)

        notPaidMans = notPaidMans.split()

        frame_not_paid_mans = customtkinter.CTkScrollableFrame(frame_all_paid_not_paid_Scrolls_alnd_labels, height=200,
                                                               width=1600, orientation="horizontal",
                                                               fg_color='transparent')
        frame_not_paid_mans.pack(anchor='nw', padx=20, pady=10)

        def makeStudentNotPaid():
            for student_name in notPaidMans:
                frame_man = customtkinter.CTkFrame(frame_not_paid_mans, height=200, width=250)
                frame_man.pack_propagate(False)
                frame_man.pack(side=LEFT, padx=5, pady=5)

                frame_profile = customtkinter.CTkFrame(frame_man, width=200, height=300)
                frame_profile.pack_propagate(False)
                frame_profile.pack(side=TOP, padx=10, pady=5)

                circle = customtkinter.CTkFrame(frame_profile, width=50, height=50, corner_radius=100,
                                                fg_color='#274695')
                circle.pack(side=TOP, pady=(10, 0), padx=20)

                frame_rectangle = customtkinter.CTkFrame(frame_profile, width=100, height=50, corner_radius=100,
                                                         fg_color='#274695')
                frame_rectangle.pack(side=TOP)

                frame_grren_paid = customtkinter.CTkFrame(frame_profile, fg_color="red", width=140, height=25)
                frame_grren_paid.pack(side=BOTTOM, pady=5)

                label_paid_in_thin_green_paid = customtkinter.CTkLabel(frame_grren_paid, text='Nie Wpłacone')
                label_paid_in_thin_green_paid.pack(side=BOTTOM, padx=5)

                label_name = customtkinter.CTkLabel(frame_profile, text=student_name, font=custom_font)
                label_name.pack(side=BOTTOM, pady=5)

        makeStudentNotPaid()

        def comback_to_feeses_panel():
            frame_feses_main.forget()
            frame_group.pack_propagate(False)
            frame_group.pack(anchor='nw', padx=20, pady=10)

            frame_show_fees_by_student.pack_propagate(False)
            frame_show_fees_by_student.pack(side=LEFT, padx=20)
            frame_add_fees.pack_propagate(False)
            frame_add_fees.pack(side=LEFT)

            tabview_fees.pack(side=BOTTOM, padx=20)
            label_add_fees_frame.pack(side=LEFT, padx=(10, 0))
            button_plus_fees.pack(side=RIGHT, padx=(0, 10))

            label_show_student.pack(side=TOP, padx=10, pady=10)
            frame_gorup_student_ang_go_to_fees_user.pack(side=TOP, padx=10, pady=10)
            combobox_student.pack(side=LEFT, padx=5)
            button_open_show_student.pack(side=LEFT, padx=5)

            refresh_fees_frame()

            refresh_fees_frame()

        buton_comback_to_feese = customtkinter.CTkButton(frame_feses_main_sec, width=250, height=40, text='Powrót z',
                                                         command=comback_to_feeses_panel, font=custom_font_biggest)
        buton_comback_to_feese.pack(anchor='sw', pady=20, padx=20)

    #                     checkPoint
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################

    def create_rows_end():
        z = 0
        y = 3
        x = 1
        idk = 0
        count_fees = how_much_fees_is_ended()
        id_list = feses_list_id_end()
        for _ in range(math.ceil(how_much_fees_is_exists() / 3)):
            frame_not_fees = customtkinter.CTkFrame(frame_scroll_fees_not_active, width=1600, height=200,
                                                    fg_color='transparent')
            frame_not_fees.pack(side=TOP)

            for i in range(z, y):
                if count_fees == 0:
                    break
                else:
                    frame_fees_name_frame = customtkinter.CTkFrame(frame_not_fees, fg_color='transparent')
                    frame_fees_name_frame.pack(side=LEFT)

                    fee_name = get_fee_name_by_id(id_list[idk])

                    label_fees_name = customtkinter.CTkLabel(frame_fees_name_frame, text=f"{fee_name}",
                                                             font=custom_font_column)
                    label_fees_name.pack(side=TOP)

                    frame_fees = customtkinter.CTkFrame(frame_fees_name_frame, width=350, height=200)
                    frame_fees.pack(side=TOP, padx=10, pady=10)
                    frame_fees.pack_propagate(False)

                    def label_paid_count_end(id):
                        try:
                            connection = pyodbc.connect(connection_string)
                            cursor = connection.cursor()
                            cursor.execute(
                                f"SELECT COUNT(Status) as PaidCount FROM FeesItems WHERE FeesID = {id} AND Status = 'Tak'")
                            row = cursor.fetchone()
                            if row:
                                paid_count = row.PaidCount
                            else:
                                paid_count = 0
                        except pyodbc.Error as ex:
                            print(f'Błąd połączenia z bazą danych: {ex}')
                            paid_count = 0
                        finally:
                            if connection:
                                connection.close()
                        return paid_count

                    def label_not_paid_cunt_end(id):
                        try:
                            connection = pyodbc.connect(connection_string)
                            cursor = connection.cursor()
                            cursor.execute(
                                f"SELECT COUNT(Status) as NotPaidCount FROM FeesItems WHERE FeesID = {id} AND Status = 'Nie'")
                            row = cursor.fetchone()
                            if row:
                                notpaid_count = row.NotPaidCount
                            else:
                                notpaid_count = 0
                        except pyodbc.Error as ex:
                            print(f'Błąd połączenia z bazą danych: {ex}')
                            notpaid_count = 0
                        finally:
                            if connection:
                                connection.close()
                        return notpaid_count

                    paid_count = label_paid_count_end(id_list[idk])
                    not_paid_coint = label_not_paid_cunt_end(id_list[idk])

                    label_paid = customtkinter.CTkLabel(frame_fees, text=f'Wpłacono: {paid_count}', font=custom_fontc)
                    label_paid.pack(anchor='nw', padx=20, pady=(10, 5))

                    label_not_paid = customtkinter.CTkLabel(frame_fees, text=f'Nie wpłacone: {not_paid_coint}',
                                                            font=custom_fontc)
                    label_not_paid.pack(anchor='nw', padx=20, pady=(5, 10))

                    def goFees_end(fee_name=fee_name):
                        openEndedFeesPanel(fee_name)

                    buton_go_to_fees = customtkinter.CTkButton(
                        frame_fees,
                        width=300,
                        height=60,
                        text='Wejdź',
                        font=custom_font_biggest,
                        fg_color='grey',
                        command=lambda fn=fee_name: goFees_end(fn))
                    buton_go_to_fees.pack(side=BOTTOM, padx=20, pady=(5, 20))

                    x += 1
                    count_fees -= 1
                    idk += 1

        z += 3
        y += 3

    create_rows_end()

    def refresh_fees_frame():
        for widget in frame_scroll_fees_not_active.winfo_children():
            widget.destroy()
        create_rows_end()

    #                                       CHECKPOINT MORDO
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################

    frame_select_what_to_do = customtkinter.CTkFrame(master=tabview_main.tab("Zarządzanie bazą danych"))
    frame_select_what_to_do.pack(side=TOP)

    combo_box_tabels_in_frame_main = customtkinter.CTkComboBox(master=frame_select_what_to_do, width=300, height=30,
                                                               values=tables_list, font=custom_font_biggest)
    combo_box_tabels_in_frame_main.pack(side=TOP, pady=10, padx=10)

    frame_things = customtkinter.CTkFrame(master=frame_select_what_to_do, fg_color='transparent')
    frame_things.pack(side=TOP, pady=20)

    #                      SMALL CHECKPOINT
    ###################################################################
    ###################################################################
    ###################################################################

    def go_to_add():
        frame_add_things.pack_forget()
        frame_del_things_2.pack_forget()
        frame_modify_things_3.pack_forget()
        frame_adding.pack(side=TOP)

    def comeback_from_add():

        frame_adding.pack_forget()

        frame_add_things.pack(side=LEFT, padx=20, pady=(50, 10))
        frame_del_things_2.pack(side=LEFT, padx=20, pady=(50, 10))
        frame_modify_things_3.pack(side=LEFT, padx=20, pady=(50, 10))

    frame_add_things = customtkinter.CTkFrame(master=frame_things, width=350, height=200, fg_color='#323232')
    frame_add_things.pack(side=LEFT, padx=20, pady=(50, 10))

    label_adding = customtkinter.CTkLabel(master=frame_add_things, font=custom_font,
                                          text="Dodawanie i usuwanie column \n Dodawanie danych z pliku\nDodawanie danych pojedyńczo")
    label_adding.pack(side=TOP, pady=(20, 10), padx=40)

    button_go_to_add = customtkinter.CTkButton(frame_add_things, width=250, height=60, text='Dodaj', font=custom_fontc,
                                               command=go_to_add)
    button_go_to_add.pack(side=BOTTOM, padx=20, pady=(30, 20))

    frame_adding = customtkinter.CTkFrame(frame_things, width=1500, height=1000, fg_color='#323232')
    frame_adding.pack_propagate(False)

    label_add_text = customtkinter.CTkLabel(frame_adding, text="Dodaj", font=custom_font_test)
    label_add_text.pack(side=TOP, pady=(10, 0))

    frame_to_adding_frames = customtkinter.CTkFrame(frame_adding, fg_color='transparent')
    frame_to_adding_frames.pack(side=TOP, pady=(20, 0))

    #          MINI CHECKPOINT
    #####################################
    #####################################

    frame_first_add = customtkinter.CTkFrame(frame_to_adding_frames, width=360, height=490, fg_color='transparent')
    frame_first_add.pack(side=LEFT, padx=20)
    frame_first_add.pack_propagate(False)

    label_add_column_name = customtkinter.CTkLabel(master=frame_first_add, text="Dodaj Columne",
                                                   font=custom_font_biggest)
    label_add_column_name.pack(anchor='nw')

    input_name_colum_to_add = customtkinter.CTkEntry(frame_first_add, width=320, height=40,
                                                     placeholder_text='Column name', font=custom_font_column,
                                                     placeholder_text_color='#424446', border_color='#424446',
                                                     border_width=4)
    input_name_colum_to_add.pack(anchor='nw', pady=10)

    type_column = ["INT", "Varchar(..)", "CHAR(..)", "BIT", "DATA", "TIME", "VARBINARY(...)"]

    label_add_column = customtkinter.CTkLabel(master=frame_first_add, text="Typ Danych", font=custom_font_biggest)
    label_add_column.pack(anchor='nw')

    type_column_add = customtkinter.CTkComboBox(frame_first_add, width=230, height=40, values=type_column,
                                                font=custom_font_column, border_color='#424446', border_width=4)
    type_column_add.pack(anchor='nw', pady=10)

    label_add_check = customtkinter.CTkLabel(master=frame_first_add, text="Check", font=custom_font_biggest)
    label_add_check.pack(anchor='nw')

    frame_idk = customtkinter.CTkFrame(frame_first_add, fg_color='transparent')
    frame_idk.pack(side=TOP)

    check_column_add = customtkinter.CTkEntry(frame_idk, width=150, height=40, placeholder_text='5zł',
                                              font=custom_font_column, placeholder_text_color='#424446',
                                              border_color='#424446', border_width=4)
    check_column_add.pack(side=LEFT, pady=10)

    def add_column_button_click():
        tabel = combo_box_tabels_in_frame_main.get()
        column_name = input_name_colum_to_add.get()
        column_type = type_column_add.get()
        check = check_column_add.get()
        if check == '':
            check = None

        add_column(column_name, column_type, tabel, check)
        print(column_name)

    def combined_command_add():
        add_column_button_click()
        refresh_columns()
        refresh_tabview_sec()
        refresh_tabview_sec()
        multiple_refresh()

    button_add_final = customtkinter.CTkButton(frame_idk, font=custom_fontc, text='Dodaj', width=200, height=50,
                                               command=combined_command_add)
    button_add_final.pack(side=RIGHT, pady=10, padx=(10, 0))

    #   MINI CHECKPOINT
    ########################
    ########################

    frame_sec_add = customtkinter.CTkFrame(frame_to_adding_frames, width=360, height=490, fg_color='transparent')
    frame_sec_add.pack(side=LEFT, padx=20)
    frame_sec_add.pack_propagate(False)

    label_add_file_data = customtkinter.CTkLabel(frame_sec_add, text="Dodaj dane z pliku", font=custom_font_biggest)
    label_add_file_data.pack(side=TOP, padx=(0, 50))

    input_file = customtkinter.CTkEntry(frame_sec_add, width=320, height=40, placeholder_text='File',
                                        font=custom_font_column, placeholder_text_color='#424446',
                                        border_color='#424446', border_width=4)
    input_file.pack(side=TOP, pady=10)

    button_choose_file_2 = customtkinter.CTkButton(frame_sec_add, text="Wybierz plik", command=choose_file, width=100,
                                                   height=40, font=custom_font, corner_radius=10)
    button_choose_file_2.pack(anchor='nw', side=TOP, padx=(20, 0))

    input_column_name = customtkinter.CTkEntry(frame_sec_add, width=320, height=40, placeholder_text='Column name',
                                               font=custom_font_column, placeholder_text_color='#424446',
                                               border_color='#424446', border_width=4)
    input_column_name.pack(side=TOP, pady=10)

    def combined_command_import_data_file():
        import_data_from_file()
        refresh_columns()
        refresh_tabview_sec()

    button_add_file_data = customtkinter.CTkButton(frame_sec_add, font=custom_fontc, text='Dodaj', width=200, height=50,
                                                   command=combined_command_import_data_file)
    button_add_file_data.pack(side=TOP, pady=10, padx=0)

    #   MINI CHECKPOINT
    ########################
    ########################
    ########################
    ########################

    ########################
    ########################
    ########################
    ########################
    ########################
    ########################
    ########################
    ########################

    frame_thir_add = customtkinter.CTkFrame(frame_to_adding_frames, width=360, height=490, fg_color='transparent')
    frame_thir_add.pack(side=LEFT, padx=20)
    frame_thir_add.pack_propagate(False)

    label_add_one_data = customtkinter.CTkLabel(frame_thir_add, text="Dodaj dane pojedyńczo", font=custom_font_biggest)
    label_add_one_data.pack(side=TOP, padx=(10, 0))

    input_column_name_2 = customtkinter.CTkEntry(frame_thir_add, width=320, height=40, placeholder_text='Column name',
                                                 font=custom_font_column, placeholder_text_color='#424446',
                                                 border_color='#424446', border_width=4)
    input_column_name_2.pack(side=TOP, pady=10)

    frame_nextv4 = customtkinter.CTkFrame(frame_thir_add, fg_color='transparent')
    frame_nextv4.pack(side=TOP)

    input_value = customtkinter.CTkEntry(frame_nextv4, width=150, height=40, placeholder_text='Wartość',
                                         font=custom_font_column, placeholder_text_color='#424446',
                                         border_color='#424446', border_width=4)
    input_value.pack(side=LEFT, pady=5)

    input_int_id_add_one_data = customtkinter.CTkEntry(frame_nextv4, width=50, height=40, placeholder_text='ID',
                                                       font=custom_font_column, placeholder_text_color='#424446',
                                                       border_color='#424446', border_width=4)
    input_int_id_add_one_data.pack(side=RIGHT, pady=5, padx=(10, 110))

    input_main_id = customtkinter.CTkEntry(frame_thir_add, width=320, height=40, placeholder_text='Nazwa ID columny',
                                           font=custom_font_column, placeholder_text_color='#424446',
                                           border_color='#424446', border_width=4)
    input_main_id.pack(side=TOP, pady=10)

    def add_data(id_column_name, id_int, column, data, tabel):
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            update_query = f"""
                  UPDATE {tabel}
                  SET {column} = '{data}'
                  WHERE {id_column_name} = '{id_int}'
                  """

            cursor.execute(update_query)
            connection.commit()

            print("Dane dodane pomyślnie.")
            succesful_data_go()
        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')
            show_error_popup()

        finally:
            if connection:
                connection.close()

    def combined_command_add_data():
        tabel_name_add_one = combo_box_tabels_in_frame_main.get()
        id_add = input_main_id.get()
        column_name_add_one_data = input_column_name_2.get()
        data_add_one = input_value.get()
        id_int = input_int_id_add_one_data.get()

        add_data(id_add, id_int, column_name_add_one_data, data_add_one, tabel_name_add_one)

        refresh_columns()
        refresh_tabview_sec()

    button_add_one_date = customtkinter.CTkButton(frame_thir_add, font=custom_fontc, text='Dodaj', width=200, height=50,
                                                  command=combined_command_add_data)
    button_add_one_date.pack(side=TOP, pady=10, padx=0)

    ###################################################################
    button_comeback = customtkinter.CTkButton(master=frame_adding, text="Powrót x ", font=custom_fontc,
                                              command=comeback_from_add, width=200, height=40)
    button_comeback.pack(side=BOTTOM, anchor='sw', padx=20, pady=20)

    #                      SMALL CHECKPOINT
    ###################################################################
    ###################################################################
    ###################################################################

    def go_to_dell():
        frame_add_things.pack_forget()
        frame_del_things_2.pack_forget()
        frame_modify_things_3.pack_forget()

        frame_delling.pack(side=TOP)

    frame_del_things_2 = customtkinter.CTkFrame(master=frame_things, width=350, height=200, fg_color='#323232')
    frame_del_things_2.pack(side=LEFT, padx=20, pady=(50, 10))

    label_delling = customtkinter.CTkLabel(master=frame_del_things_2, font=custom_font,
                                           text="Usuń kolumne \n Usuń dane z columny \n")
    label_delling.pack(side=TOP, pady=(20, 10), padx=40)

    button_go_to_dell = customtkinter.CTkButton(frame_del_things_2, width=250, height=60, text='Usuń',
                                                font=custom_fontc, command=go_to_dell)
    button_go_to_dell.pack(side=BOTTOM, padx=20, pady=(30, 20))

    ###################################################################

    frame_delling = customtkinter.CTkFrame(frame_things, width=1500, height=1000, fg_color='#323232')
    frame_delling.pack_propagate(False)

    frame_to_delling_frames = customtkinter.CTkFrame(frame_delling, fg_color='transparent')
    frame_to_delling_frames.pack(side=TOP, pady=(20, 0))
    ############

    frame_first_dell = customtkinter.CTkFrame(frame_to_delling_frames, width=360, height=490, fg_color='transparent')
    frame_first_dell.pack_propagate(False)
    frame_first_dell.pack(side=LEFT)

    frame_first_top_first_dell = customtkinter.CTkFrame(frame_first_dell, width=360, height=245, fg_color='transparent')
    frame_first_top_first_dell.pack_propagate(False)
    frame_first_top_first_dell.pack(side=TOP, pady=10)

    label_dell_column_name = customtkinter.CTkLabel(master=frame_first_top_first_dell, text="Usuń Columne",
                                                    font=custom_font_biggest)
    label_dell_column_name.pack(anchor='nw', pady=(0, 10))

    input_name_colum_to_dell = customtkinter.CTkEntry(frame_first_top_first_dell, width=320, height=40,
                                                      placeholder_text='Column name', font=custom_font_column,
                                                      placeholder_text_color='#424446', border_color='#424446',
                                                      border_width=4)
    input_name_colum_to_dell.pack(anchor='nw')

    def combined_command_del_2():
        del_column_button_click_2()
        refresh_columns()
        refresh_tabview_sec()

    button_dell_final = customtkinter.CTkButton(frame_first_top_first_dell, font=custom_fontc, text='Usuń', width=200,
                                                height=50, command=combined_command_del_2)
    button_dell_final.pack(anchor='nw', pady=10)

    frame_first_top_second_dell = customtkinter.CTkFrame(frame_first_dell, width=360, height=245,
                                                         fg_color='transparent')
    frame_first_top_second_dell.pack_propagate(False)
    frame_first_top_second_dell.pack(side=TOP)

    def combined_command_delete_all_data():
        delete_data_button_click()
        refresh_columns()
        refresh_tabview_sec()

    label_first_top_second_dell = customtkinter.CTkLabel(frame_first_top_second_dell, text="Usuń dane z columny",
                                                         font=custom_font_biggest)
    label_first_top_second_dell.pack(anchor='nw')

    input_column_name_dell_all_data_from_column = customtkinter.CTkEntry(frame_first_top_second_dell, width=320,
                                                                         height=40, placeholder_text='Column name',
                                                                         font=custom_font_column,
                                                                         placeholder_text_color='#424446',
                                                                         border_color='#424446', border_width=4)
    input_column_name_dell_all_data_from_column.pack(anchor='nw', pady=10)

    button_dell_final_all_data_column = customtkinter.CTkButton(frame_first_top_second_dell, font=custom_fontc,
                                                                text='Usuń', width=200, height=50,
                                                                command=combined_command_delete_all_data)
    button_dell_final_all_data_column.pack(anchor='nw', pady=10)

    ############

    frame_sec_dell = customtkinter.CTkFrame(frame_to_delling_frames, width=360, height=490, fg_color='transparent')
    frame_sec_dell.pack_propagate(False)
    frame_sec_dell.pack(side=LEFT, padx=20)

    frame_sec_top_f_dell = customtkinter.CTkFrame(frame_sec_dell, width=360, height=245, fg_color='transparent')
    frame_sec_top_f_dell.pack_propagate(False)
    frame_sec_top_f_dell.pack(side=TOP)

    def no_proc_vw_in_database():
        messagebox.showerror("Error", "Brak podajnej procedury lub widoku w bazie danych")

    def sucseful_del_proc_vw():
        messagebox.showinfo("Info", "Pomyślne usnięto ")

    def delete_proc_vw():
        connection = None
        try:

            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute(f"DROP {combobox_proc_or_vw.get()} {combobox_column_name_dell_proc_vw.get()}")

            connection.commit()

            print("Procedury zostały usunięte pomyślnie.")
            sucseful_del_proc_vw()
        except pyodbc.Error as ex:
            no_proc_vw_in_database()
            print(f'Błąd połączenia z bazą danych: {ex}')

        finally:
            if connection:
                connection.close()

    def combined_command_delete_proc_vw():
        delete_proc_vw()
        delete_data_button_click()
        refresh_columns()
        refresh_tabview_sec()

    label_secod_top_f_dell_proc_vw = customtkinter.CTkLabel(frame_sec_top_f_dell, text="Usuń procedure/widok",
                                                            font=custom_font_biggest)
    label_secod_top_f_dell_proc_vw.pack(anchor='nw', pady=10)

    frame_combo_vw_proc_show = customtkinter.CTkFrame(frame_sec_top_f_dell, width=360, height=40,
                                                      fg_color='transparent')
    frame_combo_vw_proc_show.pack_propagate(False)
    frame_combo_vw_proc_show.pack(side=TOP)

    vw_proc = ["Proc", "View"]

    combobox_proc_or_vw = customtkinter.CTkComboBox(frame_combo_vw_proc_show, width=220, height=40, values=vw_proc,
                                                    font=custom_font_column, border_color='#424446', border_width=4)
    combobox_proc_or_vw.pack(side=LEFT)

    def gui_with_vw_proc():
        def get_all_procedures():
            procedures = []
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                cursor.execute("SELECT name FROM sys.procedures")
                procedures = [row.name for row in cursor.fetchall()]

            except pyodbc.Error as ex:
                print(f'Błąd połączenia z bazą danych: {ex}')

            finally:
                if connection:
                    connection.close()

            return procedures

        def get_all_views():
            views = []
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                cursor.execute("SELECT name FROM sys.views")
                views = [row.name for row in cursor.fetchall()]

            except pyodbc.Error as ex:
                print(f'Błąd połączenia z bazą danych: {ex}')

            finally:
                if connection:
                    connection.close()

            return views

        def set_proc_vw_name_input(value):
            combobox_column_name_dell_proc_vw.delete(0, customtkinter.END)
            combobox_column_name_dell_proc_vw.insert(0, value)
            print(value)

        def create_buttons(frame, items):
            for item in items:
                button = customtkinter.CTkButton(frame, text=item, font=custom_font, width=100, height=20,
                                                 command=lambda value=item: set_proc_vw_name_input(value))
                button.pack(side=TOP, pady=5)

        proc_names = get_all_procedures()
        view_names = get_all_views()

        vw_proc = customtkinter.CTk()
        vw_proc.title('App TechniSchools Lublin - Procedrury i Widoki ')
        vw_proc.geometry('300x500')
        vw_proc.iconbitmap("TechniFees.ico")

        vw_proc_frame1 = customtkinter.CTkScrollableFrame(vw_proc, width=300, height=250)
        vw_proc_frame1.pack(side=TOP)
        create_buttons(vw_proc_frame1, proc_names)

        vw_proc_frame2 = customtkinter.CTkScrollableFrame(vw_proc, width=300, height=250)
        vw_proc_frame2.pack(side=TOP)
        create_buttons(vw_proc_frame2, view_names)

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        vw_proc.mainloop()

    button_show_all_proc_vw = customtkinter.CTkButton(frame_combo_vw_proc_show, font=custom_fontd, text='SHOW',
                                                      width=60, height=20, command=gui_with_vw_proc)
    button_show_all_proc_vw.pack(side=LEFT, padx=(10, 0))

    combobox_column_name_dell_proc_vw = customtkinter.CTkEntry(frame_sec_top_f_dell, width=360, height=40,
                                                               placeholder_text='Proc/vw name', font=custom_font_column,
                                                               placeholder_text_color='#424446', border_color='#424446',
                                                               border_width=4)
    combobox_column_name_dell_proc_vw.pack(anchor='nw', pady=10)

    button_dell_proc_vw = customtkinter.CTkButton(frame_sec_top_f_dell, font=custom_fontc, text='Usuń', width=200,
                                                  height=50, command=combined_command_delete_proc_vw)
    button_dell_proc_vw.pack(anchor='nw', pady=10)

    ############

    frame_thirt_dell = customtkinter.CTkFrame(frame_to_delling_frames, width=360, height=490, fg_color='transparent')
    frame_thirt_dell.pack(anchor='nw', padx=20)

    def combined_command_mod_data():
        mod_dane()
        refresh_columns()
        refresh_tabview_sec()

    frame_thirt_top_modify = customtkinter.CTkFrame(frame_thirt_dell, width=360, height=340, fg_color='transparent')
    frame_thirt_top_modify.pack_propagate(False)
    frame_thirt_top_modify.pack(side=TOP)

    label_thirt_top_modify = customtkinter.CTkLabel(frame_thirt_top_modify, text="Modyfikuj dane",
                                                    font=custom_font_biggest)
    label_thirt_top_modify.pack(anchor='nw', pady=10)

    input_column_name_modify = customtkinter.CTkEntry(frame_thirt_top_modify, width=240, height=40,
                                                      placeholder_text='Column name', font=custom_font_column,
                                                      placeholder_text_color='#424446', border_color='#424446',
                                                      border_width=4)
    input_column_name_modify.pack(anchor='nw', pady=10)

    frame_j = customtkinter.CTkFrame(frame_thirt_top_modify, width=360, height=40, fg_color='transparent')
    frame_j.pack(anchor='nw')

    main_id_mod = customtkinter.CTkEntry(frame_j, width=220, height=40, placeholder_text='Column main id ',
                                         font=custom_font_column, placeholder_text_color='#424446',
                                         border_color='#424446', border_width=4)
    main_id_mod.pack(side=LEFT, pady=10, padx=(0, 10))

    input_id_modify = customtkinter.CTkEntry(frame_j, width=100, height=40, placeholder_text='ID',
                                             font=custom_font_column, placeholder_text_color='#424446',
                                             border_color='#424446', border_width=4)
    input_id_modify.pack(side=LEFT, pady=10, padx=(10, 0))

    input_value_mod = customtkinter.CTkEntry(frame_thirt_top_modify, width=340, height=40, placeholder_text='Wartość',
                                             font=custom_font_column, placeholder_text_color='#424446',
                                             border_color='#424446', border_width=4)
    input_value_mod.pack(anchor='nw')

    button_modify = customtkinter.CTkButton(frame_thirt_top_modify, font=custom_fontc, text='Modyfikuj', width=200,
                                            height=50, command=combined_command_mod_data)
    button_modify.pack(anchor='nw', pady=10)

    ############
    ###################################################################
    def comeback_from_add():

        frame_delling.pack_forget()

        frame_add_things.pack(side=LEFT, padx=20, pady=(50, 10))
        frame_del_things_2.pack(side=LEFT, padx=20, pady=(50, 10))
        frame_modify_things_3.pack(side=LEFT, padx=20, pady=(50, 10))

    button_comeback = customtkinter.CTkButton(master=frame_delling, text="Powrót f ", font=custom_fontc,
                                              command=comeback_from_add, width=200, height=40)
    button_comeback.pack(side=BOTTOM, anchor='sw', padx=20, pady=20)

    #                      SMALL CHECKPOINT
    ###################################################################
    ###################################################################
    ###################################################################

    frame_modify_things_3 = customtkinter.CTkFrame(master=frame_things, width=350, height=200, fg_color='#323232')
    frame_modify_things_3.pack(side=LEFT, padx=20, pady=(50, 10))

    label_moding = customtkinter.CTkLabel(master=frame_modify_things_3, font=custom_font,
                                          text="Edytuj kolumne \n  Edytuj dane w kolumnie \n")
    label_moding.pack(side=TOP, pady=(20, 10), padx=40)

    button_go_to_mod = customtkinter.CTkButton(frame_modify_things_3, width=250, height=60, text='Edytuj',
                                               font=custom_fontc, command=go_to_dell)
    button_go_to_mod.pack(side=BOTTOM, padx=20, pady=(30, 20))

    #                             MODIFY COMMANDS CHENKPINT MORDO (polecał posłuchać CODE RED od NECROLIX)
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    def get_all_procedures():
        procedures = []
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sys.procedures")
            procedures = [row.name for row in cursor.fetchall()]

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex} get_all_procedure')

        finally:
            if connection:
                connection.close()

        return procedures

    def get_all_views():
        views = []
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sys.views")
            views = [row.name for row in cursor.fetchall()]

        except pyodbc.Error as ex:
            print(f'Błąd połączenia z bazą danych: {ex}')

        finally:
            if connection:
                connection.close()

        return views

    all_proc = get_all_procedures()
    all_vw = get_all_views()

    frame_things_sec = customtkinter.CTkFrame(master=frame_select_what_to_do, fg_color='transparent')
    frame_things_sec.pack(anchor='nw', pady=20)

    def go_to_add_proc_vw():
        messagebox.showinfo('Info', "Panel w budowie przepraszamy")
        # frame_add_things.pack_forget()
        # frame_del_things_2.pack_forget()
        # frame_modify_things_3.pack_forget()
        # frame_call_proc_vw.pack(side=TOP)

    frame_add_proc_vw = customtkinter.CTkFrame(frame_things_sec, width=350, height=200, fg_color='#323232')
    frame_add_proc_vw.pack(side=LEFT, padx=20, pady=(50, 10))

    label_adding = customtkinter.CTkLabel(frame_add_proc_vw, font=custom_font, text="Wywołaj procedure lub widok")
    label_adding.pack(side=TOP, pady=(20, 10), padx=40)

    button_go_to_add_proc_vw = customtkinter.CTkButton(frame_add_proc_vw, width=250, height=60, text='Przejdź',
                                                       font=custom_fontc, command=go_to_add_proc_vw)
    button_go_to_add_proc_vw.pack(side=BOTTOM, padx=20, pady=(30, 20))

    frame_call_proc_vw = customtkinter.CTkFrame(frame_things, width=1500, height=1000, fg_color='#323232')
    frame_call_proc_vw.pack_propagate(False)

    frame_call_proc_vw_to_store_frames = customtkinter.CTkFrame(frame_call_proc_vw, width=1000, height=600,
                                                                fg_color='transparent')
    frame_call_proc_vw_to_store_frames.pack(side=TOP, pady=(20, 0))

    frame_call_proc = customtkinter.CTkFrame(frame_call_proc_vw_to_store_frames, width=550, height=550,
                                             fg_color='transparent')
    frame_call_proc.pack_propagate(False)
    frame_call_proc.pack(side=LEFT, padx=(10, 10))

    def gui_with_vw_proc_call():
        def get_all_procedures_call():
            procedures = []
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                cursor.execute("SELECT name FROM sys.procedures")
                procedures = [row.name for row in cursor.fetchall()]

            except pyodbc.Error as ex:
                print(f'Błąd połączenia z bazą danych: {ex} get_all_procedures_call')

            finally:
                if connection:
                    connection.close()

            return procedures

        def get_proc_code(proc_name):
            proc_code = ""
            proc_result = None
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                cursor.execute(f"SELECT OBJECT_DEFINITION(OBJECT_ID('{proc_name}')) AS [Definition]")
                row = cursor.fetchone()
                if row:
                    proc_code = row.Definition



            except pyodbc.Error as ex:
                print(f'Błąd połączenia z bazą danych: {ex}')

            finally:
                if connection:
                    connection.close()

            return proc_code, proc_name

        def set_proc_vw_name_input(value):
            proc_code, proc_name = get_proc_code(value)
            label_proc_code.configure(text=proc_code)
            label_name_proc.configure(text=proc_name)

        def create_buttons(frame, items):
            for item in items:
                button = customtkinter.CTkButton(frame, text=item, font=custom_font, width=100, height=20,
                                                 command=lambda value=item: set_proc_vw_name_input(value))
                button.pack(side=TOP, pady=5)

        proc_names = get_all_procedures_call()

        vw_proc = customtkinter.CTk()
        vw_proc.title('App TechniSchools Lublin - Procedrury i Widoki ')
        vw_proc.geometry('300x500')
        vw_proc.iconbitmap("TechniFees.ico")

        vw_proc_frame1 = customtkinter.CTkScrollableFrame(vw_proc, width=300, height=250)
        vw_proc_frame1.pack(side=TOP)
        create_buttons(vw_proc_frame1, proc_names)

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        vw_proc.mainloop()

    label_proc = customtkinter.CTkLabel(frame_call_proc, font=custom_font_biggest, text='Pokarz procedure')
    label_proc.pack(anchor='nw')

    def show_all_proc_gui():
        gui_with_vw_proc_call()

    button_show_all_proc = customtkinter.CTkButton(frame_call_proc, width=200, height=50, font=custom_fontc,
                                                   text='Show all proc', command=show_all_proc_gui)
    button_show_all_proc.pack(anchor='nw', pady=20)

    label_name_proc = customtkinter.CTkLabel(frame_call_proc, font=custom_font_biggest, text="Last_Loged_Admin")
    label_name_proc.pack(anchor='nw')

    tabview_proc = customtkinter.CTkTabview(frame_call_proc, width=500, height=430)
    tabview_proc.pack(anchor='nw')

    tabview_proc.add("Code")
    tabview_proc.set("Code")
    tabview_proc.add("Result")
    tabview_proc.set("Result")

    ## poprawić nie działa wgl
    frame_label_proc_code_scroll = customtkinter.CTkScrollableFrame(tabview_proc.tab("Code"), orientation="horizontal",
                                                                    width=500, height=430)
    frame_label_proc_code_scroll.pack(anchor='nw')

    label_proc_code = customtkinter.CTkLabel(frame_label_proc_code_scroll, font=custom_font, text="""
    create procedure Last_Loged_Admin
    as 
    begin     
    update Student set LastLogin = getdate() 
    where StudentID = 30
    end 
    """, )
    label_proc_code.pack(anchor='nw')

    frame_label_proc_result_scroll = customtkinter.CTkScrollableFrame(tabview_proc.tab("Result"),
                                                                      orientation="horizontal", width=500, height=430)
    frame_label_proc_result_scroll.pack(anchor='nw')

    label_proc_result = customtkinter.CTkLabel(frame_label_proc_result_scroll, font=custom_font, text="""
    (1 rows affected)

    Completion time: 2024-04-13T13:57:40.2194155+02:00

    """, )
    label_proc_result.pack(anchor='nw')

    frame_call_vw = customtkinter.CTkFrame(frame_call_proc_vw_to_store_frames, width=550, height=550)
    frame_call_vw.pack_propagate(False)
    frame_call_vw.pack(side=LEFT, padx=(10, 10))

    def comeback_from_add_proc_vw():
        frame_call_proc_vw.pack_forget()

        frame_add_things.pack(side=LEFT, padx=20, pady=(50, 10))
        frame_del_things_2.pack(side=LEFT, padx=20, pady=(50, 10))
        frame_modify_things_3.pack(side=LEFT, padx=20, pady=(50, 10))

    button_comeback = customtkinter.CTkButton(frame_call_proc_vw, text="Powrót h", font=custom_fontc,
                                              command=comeback_from_add_proc_vw, width=200, height=40)
    button_comeback.pack(side=BOTTOM, anchor='sw', padx=20, pady=20)

    #                                      CHECKPOINT MORDO
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################
    ######################################################################################################

    display_columns()
    root.mainloop()

server = 'localhost'
database = 'Skladki_TechniSchools'
username = 'Login_Techni_Fees'
password = 'SuperHaslo123!'

# Ciąg połączenia
connection_string = (
    f"Driver={{ODBC Driver 17 for SQL Server}};"
    f"Server={server};"
    f"Database={database};"
    f"UID={username};"
    f"PWD={password};"
)





app = customtkinter.CTk()
app.title('App TechniSchools Lublin - Logowanie')
app.geometry('1920x1080')
app.iconbitmap("TechniFees.ico")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

custom_font_login = ("Helvetica", 40, "bold")
custom_font_pasy = ("Helvetica",25, "bold")
zaloguj_font = ("Helvetica",30, "bold")

text_log = customtkinter.CTkLabel(master=app,text="LOGOWANIE", fg_color="transparent",font=custom_font_login)
text_log.pack(side=TOP,pady=(250,10))




frame_login = customtkinter.CTkFrame(master=app,width=460,height=300)
frame_login.pack(side=TOP )



first_frame_pasy = customtkinter.CTkFrame(master=frame_login,fg_color="transparent")
first_frame_pasy.pack(side=TOP)

text_login = customtkinter.CTkLabel(master=first_frame_pasy,text="Login",font=custom_font_pasy)
text_login.pack(side=LEFT,pady=20,padx=(30,10))

input_Login = customtkinter.CTkEntry(master=first_frame_pasy, width=300, height=40)
input_Login.pack(side=RIGHT,pady=(20,20),padx=(10,30) )



second_frame_pasy = customtkinter.CTkFrame(master=frame_login,fg_color="transparent")
second_frame_pasy.pack(side=TOP)


text_pass = customtkinter.CTkLabel(master=second_frame_pasy,text="Hasło",font=custom_font_pasy)
text_pass.pack(side=LEFT,pady=(20,20),padx=(30,10))

input_pass = customtkinter.CTkEntry(master=second_frame_pasy, width=300, height=40)
input_pass.pack(side=RIGHT,pady=10,padx=(10,30) )




def generate_md5_hash(password):
    md5_hash = hashlib.md5()
    md5_hash.update(password.encode('utf-8'))
    hashed_password = md5_hash.hexdigest()

    return hashed_password

def get_Log_pass():
    Login = input_Login.get()
    Pass = input_pass.get()
    Pass = generate_md5_hash(Pass)
    print(Pass)
    logowanie(Login, Pass)


submit_button = customtkinter.CTkButton(master=frame_login, text="Zaloguj", font=zaloguj_font, width=300, height=50, command=get_Log_pass)
submit_button.pack(side=BOTTOM,pady=30)





app.mainloop()









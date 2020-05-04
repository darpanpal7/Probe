#===================================================================================================
#IMPORTS

""" 1. 'os' for accessing file system and hard drives
    2. 're' for pattern matching and substring search
    3. 'sys' for creating gui windows
    4. 'pickle' for serialization of object
    5. 'win32api' to get access to hard drives
    5. 'subprocess' to create and execute processes
    6. 'threading' for multithreading on different drives
    7. 'datetime' to monitor execution speed
    8. 'tkinter' for creating gui
"""

import os
import re
import sys
import pickle
import win32api
import subprocess
from threading import Thread
from datetime import datetime

#SEARCH CLASS
#==================================================================================================
class SearchScript :

    #CLASS ATTRIBUTES
    #==============================================================================================
    dictionary = {}
    dic = {}

    #BEHAVIOR METHODS
    #==============================================================================================

    def __init__(self) :

        """ Main function that will call other other functions """

        #if database exists then , deserialize it and if not then create database
        try:
            self.dic = self.dbload()
            self.dataexist()

        except IOError:
            self.create()
            self.dic = self.dbload()

        finally:
            print("Thanks.")
            
    #----------------------------------------------------------------------------------------------        
    def get_drives(self) :
    
        """ Function to get list of drives attached """
        
        response = os.popen("wmic logicaldisk get caption")
        total_drives = []
        for line in response.readlines() :
            line = line.strip("\n")
            line = line.strip("\r")
            line = line.strip(" ")
            if line == "Caption" or line == "" :
                continue
            total_drives.append(line)
        return total_drives

    #----------------------------------------------------------------------------------------------
    def make(self, drive) :

        """ Function that takes a drive as input and stores all files and folders in the database recursively """

        for root, dir, files in os.walk(drive, topdown=True) :

            # 'files' for list of files in the folder
            for file in files :
                file = file.lower()

                if file in self.dictionary :
                    while file in self.dictionary :
                        file = file + "_"
                    self.dictionary[file] = root

                else :
                    self.dictionary[file] = root

            # 'dir' for list of subfolders in the folder
            for dirs in dir :
                dirs = dirs.lower()

                if dirs in self.dictionary :
                    while dirs in self.dictionary :
                        dirs = dirs + "_"
                    self.dictionary[dirs] = root

                else :
                    self.dictionary[dirs] = root

    #----------------------------------------------------------------------------------------------
    def create(self) :

        """ Function to create and serialize the dictionary object """

        #top.modifyrightlabel("Creating Database...")

        t1 = datetime.now()
        total_drives = self.get_drives() #list of drives attached
        process_list = []
        print(total_drives)

        #creating one process for each drive

        for each in total_drives :
            process = Thread(target = self.make, args = (each,))
            process.start()
            process_list.append(process)

        for each in process_list :
            each.join()  #joining all threads

        #opening a file named database
        dbfile = open("database", "ab")

        #storing the dictionary object into file
        pickle.dump(self.dictionary, dbfile, protocol=pickle.HIGHEST_PROTOCOL)
        dbfile.close()
        t2 = datetime.now()
        total = t2 - t1
        print("Database created." )
        print("Total Files : ",len(self.dictionary))
        print("Time Taken : ", total)

    #----------------------------------------------------------------------------------------------
    def dbload(self) :

        """ Function to deserialize the dictionary object from database file """

        dbfile = open("database", "rb")
        self.dic = pickle.load(dbfile) #loading into RAM
        dbfile.close()
        return self.dic

    #----------------------------------------------------------------------------------------------
    def do_search(self,var) :

        """ Function to search the database """

        file_list = []
        for key in self.dic :
            if re.search(var, key) :  #substring matching in dic
                entry = self.dic[key] + "\\" + key
                file_list.append(entry)
        
        return file_list

    #----------------------------------------------------------------------------------------------
    def initialize (self) :

        """ Function to display all the files and folders which exist in database """

        files_list = []
        for item in dic :
            each = dic[item] + "\\" + item
            files_list.append(each)

        #top.create_items(files_list)

        #disabling the textbox to avoid further changes made by the user
        #top.statechangetextbox(0)

    #----------------------------------------------------------------------------------------------
    def dataexist(self) :

        """ Function that checks whether the database exists or not """

        if os.path.isfile("database"):
            #top.modifyrightlabel("Database Exists.")
            print("Database Exists.")
        else:
            #top.modifyrightlabel("No Database Exists.")
            print("No Database Exists")
    #----------------------------------------------------------------------------------------------
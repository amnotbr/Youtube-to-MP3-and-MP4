import tkinter
import customtkinter
import os
from pytube import YouTube
from moviepy.editor import *
from pydub import AudioSegment
import threading
from tkinter import ttk

def mp4(link, save_path=None):
    try:
        # Create a YouTube object
        yt = YouTube(link)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Display some information about the video
        print("Video Title:", yt.title)
        print("Video Duration:", yt.length, "seconds")

        # Get the user's 'Downloads' folder path
        save_path = os.path.join(os.path.expanduser("~"), "Downloads")

        # Download the video to the specified path
        stream.download(output_path=save_path)
        print("Download complete!")
    except Exception as e:
        print("Error:", e)

def mp3(link, save_path=None):
    try:
        # Create a YouTube object
        yt = YouTube(link)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Display some information about the video
        print("Video Title:", yt.title)
        print("Video Duration:", yt.length, "seconds")

        # Set the default save path if not provided
        if save_path is None:
            save_path = "downloads/" + yt.title

        # Create the directory if it doesn't exist
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Download the video to the specified path
        video_path = os.path.join(save_path, yt.title + ".mp4")
        stream.download(output_path=save_path)

        # Check if the video file was downloaded successfully
        if not os.path.exists(video_path):
            raise FileNotFoundError("Video file not found. Download failed.")

        # Convert video to audio using pydub
        audio_path = os.path.join(save_path, yt.title + ".mp3")
        audio = AudioSegment.from_file(video_path, format="mp4")
        audio.export(audio_path, format="mp3")

        # Clean up
        os.remove(video_path)

        print("Download and conversion complete! MP3 saved at:", audio_path)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print("Error:", e)

def main():
    # setting everthing as normal or some shit like idk bro im fucking 15 what do you want
    app = customtkinter.CTk()
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # setting the color theme to blue or something like that
    app.geometry("400x400")
    
    # making the title
    title = customtkinter.CTkLabel(app, text="Youtube to mp4/mp3", fg_color="transparent")
    
    # making the entry thing
    entry = customtkinter.CTkEntry(app, width=360)
    

    # functions for downloading the shiz
    def mpt_click():
        link = str(entry.get())
        mp3(link)        
            
    def mpf_click():
        link = str(entry.get())
        mp4(link)
        
    
    
    # buttons for either mp3 or mp4
    b_mpt = customtkinter.CTkButton(app, text="mp3", width=360, height=100, command=mpt_click)
    b_mpf = customtkinter.CTkButton(app, text="mp4", width=360, height=100, command=mpf_click)
    
    # place the title
    title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    
    # place the entry for the link
    entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    
    # placing the buttons
    b_mpt.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    b_mpf.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
    
    app.mainloop()

if __name__ == "__main__":
    main()

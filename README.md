# spaceWallpapers

## Setup instructions

1. Clone the project.
2. Go to the project directory and 
    i) start a virtual environment by running 
    ```
        python3 -m venv env.
    ```
    ii) activate the virtual environment as 
    ```
    source env/bin/activate
    ```
    
3. Install the required packages for the project as 
     ```
           pip3 install -r requirements.txt
     ```
4. To fetch the latest picture of the day from Astronomy.com gallery, run the webscraping script as 
      ```
            python3 webscraper.py
      ```
 5. Now for the wallpapers to be picked randomly from the scraped images and changed automatically at regualr intervals, we have to put a script to be run as a cron job.
 <ul>
   i) Open the list of cron jobs as 
    ```
        crontab -e
    ```
    ii) Add your own cron job in the list in the format ` m h  dom mon dow   command` as 

     ```
        * * * * * path/to/choose_wallpaper.sh
     ```
  </ul>
   This runs the bash script `choose_wallpaper.sh` and changes the wallpaper every minute.

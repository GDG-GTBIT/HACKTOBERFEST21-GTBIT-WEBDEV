# billboard-scrapper

## Billboard 🎵 Scrapping Using NodeJS modules
#### In this project we will be scrapping the Billboard's Hot 100 songs webpage and acquire the songs list and store it in different forms.
![billboard hot 100](https://raw.githubusercontent.com/Jas-Script/billboard-scrapper/master/pics%20for%20readme/billpic.PNG)

#### In order to generate an excel file and json file containing details of top 100 songs do the following steps:

#### 1. Open billboard.js in your editor (I used VS Code)
#### 2. Install the following libraries 

##### a. AXIOS
##### b. JSDOM
##### c. EXCEL4NODE
##### d. MINIMIST
#### Command for Installing these npm modules :
```
npm init -y
npm install minimist
npm install excel4node
npm install jsdom
npm install axios
```

#### After installation run the following command 
```
node billboard.js --src=https://www.billboard.com/charts/hot-100 --excel=100songs.csv
```
### RESULTS
#### JSON File
![billboard hot 100](https://raw.githubusercontent.com/Jas-Script/billboard-scrapper/master/pics%20for%20readme/jsopic.PNG)
#### EXCEL File
![billboard hot 100](https://raw.githubusercontent.com/Jas-Script/billboard-scrapper/master/pics%20for%20readme/exlpic.PNG)

### If you like this project ,some some love 💖 and star/fork this repository. Thanks for showing your interest 🙏

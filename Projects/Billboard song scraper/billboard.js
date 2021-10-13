let minimist= require("minimist");
let axios=require("axios");
let jsdom=require("jsdom");
let fs=require("fs");
let excel=require("excel4node");

args=minimist(process.argv);
let dld=axios.get(args.src);
dld.then(function(response){
    let html=response.data;
    let dom=new jsdom.JSDOM(html);
    let document=dom.window.document;
    let songs=[];
    let songdivs=document.querySelectorAll("ol.chart-list__elements>li");
    for(let i=0;i<songdivs.length;i++){
        let songdiv=songdivs[i];
       let song={
            rank:"",
            name:"",
            artist:"",
        };
        let artistpara=songdiv.querySelectorAll("span.chart-element__information>span");
        let rankpara=songdiv.querySelectorAll("span.chart-element__rank__number")
        song.name=artistpara[0].textContent;
        song.rank=rankpara[0].textContent;
        song.artist=artistpara[1].textContent;
        songs.push(song);
    }
    let songsJSON = JSON.stringify(songs); // done
    fs.writeFileSync("songs.json", songsJSON, "utf-8");
    createExcelFile(songs);

})

function createExcelFile(songs) {
    let wb = new excel.Workbook();
    let sheet = wb.addWorksheet("Hot 100");
    sheet.cell(1, 1).string("RANK");
        sheet.cell(1, 2).string("SONG");
        sheet.cell(1, 3).string("ARTIST");
    for (let i = 0; i < songs.length; i++) {
            sheet.cell(2 + i, 1).string(songs[i].rank);
            sheet.cell(2 + i, 2).string(songs[i].name);
            sheet.cell(2 + i, 3).string(songs[i].artist);
        }
    wb.write(args.excel);
}
let tagline=document.getElementById("title-tagline-content");
let cursorLine=document.getElementById("title-tagline-cursor");
let taglineContent="ONE STOP RESOURCE GUIDE FOR UNSTOPPABLE LEARNING".split("");
var i=0;

function inputTagline()
{ 
    if(i<taglineContent.length)
    {
    tagline.innerHTML+=taglineContent[i];
    i++;
    setTimeout(inputTagline,100);
    }
    else if(i===taglineContent.length)
    {
        cursorLine.style.display="none";
    }
}

inputTagline();





let navbar=document.getElementsByClassName("navbar");

window.addEventListener("scroll",function()
{
    if(window.scrollY>0)
    {
        navbar[0].style.borderBottom="1px solid #55FF1B";
    }
    else{
        navbar[0].style.borderBottom="none";
    }
    // console.log(window.scrollY);
});
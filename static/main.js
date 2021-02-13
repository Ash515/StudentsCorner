function educationplus(){
    document.getElementById('education-plus');
    document.querySelector('.education-model').style.display="flex";
};
function expplus(){
    document.getElementById('experience-plus');
    document.querySelector('.experience-model').style.display="flex";
    window.scrollTo(0,0);
};
function certifyplus(){
    document.getElementById('certify-plus');
    document.querySelector('.certify-model').style.display="flex";
    window.scrollTo(0,0);
};
function projectplus(){
    document.getElementById('project-plus');
    document.querySelector('.project-model').style.display="flex";
    window.scrollTo(0,0);
};
function volunteerplus(){
    document.getElementById('volunteer-plus');
    document.querySelector('.volunteer-model').style.display="flex";
    window.scrollTo(0,0);
};
function contactplus(){
    document.getElementById('contact-plus');
    document.querySelector('.contact-model').style.display="flex";
    window.scrollTo(0, 0);
};

function closing(){
    document.querySelector('.close');
    document.querySelector('.education-model').style.display="none";
}
function expclosing(){
    document.querySelector('.expclose');
    document.querySelector('.experience-model').style.display="none";
}
function certifyclosing(){
    document.querySelector('.certifyclose');
    document.querySelector('.certify-model').style.display="none";
}
function proclosing(){
    document.querySelector('.projectclose');
    document.querySelector('.project-model').style.display="none";
}
function volclosing(){
    document.querySelector('.volclose');
    document.querySelector('.volunteer-model').style.display="none";
}
function contactclosing(){
    document.querySelector('.contclose');
    document.querySelector('.contact-model').style.display="none";
}
function linktab(){
    var x=document.getElementById('link');
    if(x.style.display=="block"){
        x.style.display ="none";
    }else {
        x.style.display = "block";
      }
    
}
function checking(){
    var y=document.getElementById('ceryears');
    if(y.style.display=="block"){
        y.style.display ="none";
    }else {
        y.style.display = "block";
      }
}
function voladresstab(){
    var z=document.getElementById('link2');
    if(z.style.display=="block"){
        z.style.display ="none";
    }else {
        z.style.display = "block";
      }
}


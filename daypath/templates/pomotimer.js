let short_break_btn=document.getElementById('short_break-btn');
let long_break_btn=document.getElementById('long_break-btn');
let pomodoro_btn=document.getElementById('pomodoro-btn');

let pomotimer=document.getElementById('timer')

let time="{{time.work_time}}";

let start_btn=document.getElementById('start')
let running=false
let current_timer='pomodoro';
let active_btn=pomodoro_btn;


active_btn.style.backgroundColor="white";
active_btn.style.color='#B84495';

start_btn.addEventListener('click',function(){
start_stop();
});

displayTime();

short_break_btn.addEventListener('click',function(){

  if(current_timer=='short_break')return;

  current_timer='short_break';
 
  time="{{time.break_time}}";
  displayTime();
  stop();
  active_btn.style.backgroundColor="inherit";
  active_btn.style.color='white';

  active_btn=short_break_btn;

 active_btn.style.backgroundColor="white";
  active_btn.style.color='#B84495';

});

long_break_btn.addEventListener('click',()=>{

  if(current_timer=='long_break')return;

  current_timer='long_break';
 
  time="{{time.long_break_time}}";
  displayTime();
  stop();
  active_btn.style.backgroundColor="inherit";
  active_btn.style.color='white';
  active_btn=long_break_btn;
  active_btn.style.backgroundColor="white";
active_btn.style.color='#B84495';

});

pomodoro_btn.addEventListener('click',()=>{

  if(current_timer=='pomodoro')return;

  current_timer='pomodoro';
 
  time="{{time.work_time}}";
  displayTime();
  stop();
  active_btn.style.backgroundColor="inherit";
  active_btn.style.color='white';

  active_btn=pomodoro_btn;
  active_btn.style.backgroundColor="white";
active_btn.style.color='#B84495';

});


function start_stop(){

      if(running){

        start_btn.innerHTML='Start';
        running=false;

      }else{
        running=true
        start_btn.innerHTML='Stop';
        setInterval(CountDown,1000);

      }
}

function stop(){
  
 if(running){

        start_btn.innerHTML='Start';
        running=false;
 }
}

function CountDown(){

  if(running){

        displayTime();
        if(time>=0) time--;
  }

}


function displayTime(){

  if(time>=0){

    let minutes=Math.floor(time/60).toString();
      
    let seconds=(time%60).toString();
  
    if(minutes.length <2){
  
      minutes='0'.concat(minutes)
    
    }
  
    if(seconds.length <2){
      
      seconds='0'.concat(seconds)
    
    }
  
  pomotimer.innerHTML=`${minutes}:${seconds}`;
  }else{pomotimer.innerHTML=`00:00`;}

}

///////////////////////////////////////////////////////////////////////
//  MODAL 

var modal = document.getElementById("settings-modal");


var btn = document.getElementById("settings");


var span = document.getElementsByClassName("close")[0];


btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
} 





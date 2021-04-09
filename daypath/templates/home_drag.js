
function dragstart_handler(ev) {
    ev.dataTransfer.setData("text/html", ev.target.id );
    ev.dataTransfer.dropEffect = "move";
}

function dragover_handler(ev) {
    ev.preventDefault();
    ev.dataTransfer.dropEffect = "move"
}

function drop_handler(ev) {

    ev.preventDefault();

    var data = ev.dataTransfer.getData("text/html");
   
    var destiny= ev.target.querySelector('.only-tasks-container');
  
    var type=   ev.target.parentElement.className.split(' ')[1].split('-')[2];
  
    let element=document.getElementById(data);

    destiny.appendChild(element);

      $.getJSON($SCRIPT_ROOT + '/home/move', {
          task_id: data,
          task_type:type
      }, function() 
      {

      });

    let old_class=element.classList[1];

    element.classList.remove(old_class);
    element.classList.add(`task_${type}`);


}

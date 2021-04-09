
$(function() {
    $('.add-input-btn').bind('click', function() {
        
        let input=$(this).prev();
        let input_content= $(this).prev().val();

        if(input_content!==""){
        task_type=input.attr("id");

      $.getJSON($SCRIPT_ROOT + '/home/add', {
          content: input_content,
          task_type:task_type
      }, function(task_id) 
      {

            input.parent().before( `<div class="task__box task_${task_type}"
            id="${ task_id.task_id}"
            draggable="true"
            ondragstart="dragstart_handler(event)"
            >
            <input class="task__name"  value="${input_content}" type="text">
            <button class='update-input-btn task-btn' ><span><span>&#10003;</span></span></button>

            <button class="task-delete-btn task-btn">&#10005;</button>
            </div>`
            );
            input.val('');


      });
      return false;
    }

    });
  });



  $(function() {
    $('.task-delete-btn').bind('click', function() {
        
        let parent_div=$(this).parent();
        task_id=parent_div.attr('id');

      $.getJSON($SCRIPT_ROOT + '/home/del', {
          task_id:task_id
       
      }, function() 
      {

            parent_div.remove();


      });
      return false;
    

    });
  });





 update_btns= document.querySelectorAll('.update-input-btn');


 update_btns.forEach(element => {
   element.addEventListener('click',function(){

    let task_id=element.parentNode.id;
    let new_value=element.previousElementSibling.value;

      $.getJSON($SCRIPT_ROOT + '/home/update', {
        task_id: task_id,
        task_content:new_value
    }, function() 
    {

    });


   },false);

   
 });
